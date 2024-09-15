import csv
import time
import requests
import pdfplumber

def generate_qna_from_text(text_chunk, api_key, retry_count=3):
    prompt = f"""
    Your task is to read and understand the following text from a book and generate a relevant question and a clear, concise answer based on the content. The question should focus on testing the understanding of key concepts or information from the text.

    Text: "{text_chunk}"

    Please provide the question and answer in the following format:
    Question: [Generated question based on the text]
    Answer: [Clear and concise answer based on the text]
    """
    api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    for attempt in range(retry_count):
        try:
            response = requests.post(api_url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            if "Question:" in content and "Answer:" in content:
                question, answer = content.split("Answer:")
                return question.replace("Question:", "").strip(), answer.strip()
            else:
                return None, None
        except Exception as e:
            time.sleep(2)
    return None, None

def generate_context_for_answer(answer, api_key, retry_count=3):
    prompt = f'Your task is to generate a context based on the following answer to help train a model.\n\nAnswer: "{answer}"\n\nPlease provide a relevant context for the given answer.'
    api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    for attempt in range(retry_count):
        try:
            response = requests.post(api_url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            return content.strip() if content else None
        except Exception as e:
            time.sleep(2)
    return None

def rewrite_answer(answer, api_key, retry_count=3):
    prompt = f'Your task is to rewrite the following answer to make it clearer and more concise for training purposes.\n\nAnswer: "{answer}"\n\nPlease rewrite the answer in a more concise and clear way.'
    api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    for attempt in range(retry_count):
        try:
            response = requests.post(api_url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            return content.strip() if content else None
        except Exception as e:
            time.sleep(2)
    return None

def read_pdf(file_path, start_page, num_pages):
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        total_pages = len(pdf.pages)
        if start_page + num_pages - 1 > total_pages:
            num_pages = total_pages - start_page + 1
        for page_num in range(start_page - 1, start_page - 1 + num_pages):
            page = pdf.pages[page_num]
            full_text += page.extract_text() + "\n"
    return full_text

def chunk_text(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def write_to_csv(qna_pairs, output_file, append=True):
    mode = 'a' if append else 'w'
    with open(output_file, mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not append:
            writer.writerow(['Question', 'Answer', 'Context', 'Rewritten Answer'])
        writer.writerows(qna_pairs)

def process_pdf_to_qna(pdf_path, output_csv, api_keys, start_page, num_pages, chunk_size=500):
    text = read_pdf(pdf_path, start_page, num_pages)
    chunks = chunk_text(text, chunk_size)
    qna_pairs = []
    total_chunks = len(chunks)
    total_keys = len(api_keys)
    if total_keys == 0:
        raise ValueError("No API keys provided.")

    current_page = start_page
    for idx, chunk in enumerate(chunks):
        current_key_index = idx % total_keys
        current_api_key = api_keys[current_key_index]

        question, answer = generate_qna_from_text(chunk, current_api_key)

        if question is None or answer is None:
            question, answer = generate_qna_from_text(chunk, current_api_key)

        if question and answer:
            context = generate_context_for_answer(answer, current_api_key)
            rewritten_answer = rewrite_answer(answer, current_api_key)
            qna_pairs.append([question, answer, context, rewritten_answer])

        time.sleep(1)

        if (idx + 1) % 10 == 0 or (idx + 1) == total_chunks:
            write_to_csv(qna_pairs, output_csv, append=True)
            qna_pairs.clear()

        if (idx + 1) % 20 == 0:
            current_page += 1

if __name__ == "__main__":
    pdf_path = "book.pdf"
    output_csv = "book_qna.csv"
    
    api_keys = [
        "API_KEY_1",
        "API_KEY_2",
        "API_KEY_3",
        "API_KEY_4",
        "API_KEY_5"
    ]
    
    start_page = int(input("Enter the starting page number: "))
    num_pages = int(input("Enter the number of pages to process for QnA: "))

    process_pdf_to_qna(pdf_path, output_csv, api_keys, start_page, num_pages)