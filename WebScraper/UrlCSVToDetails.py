import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import re

output_csv = 'commercial_court_judgment_data.csv'

gemini_api_keys = [
    'API_KEY_1',
    'API_KEY_2',
    'API_KEY_3',
    'API_KEY_4',
    'API_KEY_5',
]

gemini_api_endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='

api_key_index = 0
max_retries = 5

def get_next_api_key():
    global api_key_index
    api_key = gemini_api_keys[api_key_index]
    api_key_index = (api_key_index + 1) % len(gemini_api_keys)
    return api_key

def clean_text(text):
    return re.sub(r'\*+', '', text).strip()

def scrape_judgment_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    judgments_div = soup.find('div', class_='judgments')
    full_text = judgments_div.get_text() if judgments_div else 'No judgments found.'
    return {
        'url': url,
        'full_text': clean_text(full_text)
    }

def send_to_gemini_api(scraped_data, field):
    retries = 0
    while retries < max_retries:
        api_key = get_next_api_key()

        content_to_extract = (
            f"You are an expert in Indian Commercial Court Law. "
            f"From the following data, extract only the '{field}':\n"
            f"{scraped_data['full_text']}"
        )

        api_url = f'{gemini_api_endpoint}{api_key}'
        body = json.dumps({
            "contents": [
                {
                    "role": "user",
                    "parts": [{ "text": content_to_extract }]
                }
            ]
        })

        try:
            response = requests.post(api_url, headers={'Content-Type': 'application/json'}, data=body)
            if response.status_code == 200:
                data = response.json()
                extracted_field = data['candidates'][0]['content']['parts'][0]['text'] if data['candidates'] else 'No data found.'
                return clean_text(extracted_field)
            else:
                retries += 1
                time.sleep(1)
        except Exception as e:
            retries += 1
            time.sleep(1)

    return None

fields_to_extract = ['title', 'body text', 'date', 'parties involved', 'decision', 'legal citations', 'legal sections', 'category']

urls_csv = 'url.csv'

with open(urls_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    urls = [row[0] for row in reader]

for input_url in urls:
    scraped_data = scrape_judgment_data(input_url)
    extracted_data = {'url': input_url, 'full_content': scraped_data['full_text']}

    for field in fields_to_extract:
        extracted_value = send_to_gemini_api(scraped_data, field)
        extracted_data[field.replace(' ', '_')] = extracted_value if extracted_value else 'N/A'

        time.sleep(1)

    with open(output_csv, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'title', 'body_text', 'date', 'parties_involved', 'decision', 'legal_citations', 'legal_sections', 'category', 'full_content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csvfile.seek(0)
        if csvfile.tell() == 0:
            writer.writeheader()

        cleaned_data = {key: clean_text(value) for key, value in extracted_data.items()}
        writer.writerow(cleaned_data)