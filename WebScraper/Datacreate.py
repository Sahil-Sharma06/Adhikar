import requests
import itertools
import random
import time
import pandas as pd
import os

# Multiple Gemini API keys for rotation
api_keys = [
    'AIzaSyCCOBbxvCzN-IgcNA_hKOpW8uzz7ZNtJoo',
    'AIzaSyA5YLmLnj3cT6Y8TZoSaaRgfyHN40im8Eo',
    'AIzaSyCHbttLGGP0LozqL20C7qXB7Nhj9PGtdh0',
    'AIzaSyBTj0pBfoNi_dD5XdGlj_L4g1AM13cKqXM',
    'AIzaSyB2YgbELf-glJzXDOhH5-y8YSOFiVsNVmk'
]

# Cycle through the API keys
api_key_cycle = itertools.cycle(api_keys)

# Base URL for Gemini API (Google Gemini API endpoint)
gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="

# Sample applicable laws for commercial cases (one law for each generated case)
applicable_laws = [
    "Indian Contract Act, 1872 - Section 73: Compensation for loss or damage caused by breach of contract",
    "Specific Relief Act, 1963 - Section 10: Specific performance of contracts",
    "Sale of Goods Act, 1930 - Section 39: Delivery of goods in installments",
    "Competition Act, 2002 - Section 4: Abuse of dominant position",
    "Arbitration and Conciliation Act, 1996 - Section 34: Setting aside arbitral award",
    "Indian Contract Act, 1872",
    "Sale of Goods Act, 1930",
    "Companies Act, 2013",
    "Negotiable Instruments Act, 1881",
    "Competition Act, 2002",
    "Consumer Protection Act, 2019",
    "Insolvency and Bankruptcy Code (IBC), 2016",
    "Arbitration and Conciliation Act, 1996",
    "Limited Liability Partnership (LLP) Act, 2008",
    "Foreign Exchange Management Act (FEMA), 1999",
    "Partnership Act, 1932",
    "The Securities Contracts (Regulation) Act, 1956",
    "Micro, Small and Medium Enterprises Development (MSMED) Act, 2006",
    "Information Technology Act, 2000",
    "The Intellectual Property Rights (Imported Goods) Enforcement Rules, 2007",
    "Factories Act, 1948",
    "Industrial Disputes Act, 1947"
]

# Function to generate the prompt for Gemini API
def generate_prompt():
    # Randomly select an applicable law for each case
    selected_law = random.choice(applicable_laws)
    
    # Construct the simple prompt
    prompt = f"Generate a unique commercial court case where ABC Ltd. is suing XYZ Corp. based on {selected_law}. Provide a brief summary of the case."
    
    return prompt, selected_law

# Function to call the Gemini API and get a response
def generate_gemini_response(prompt, api_key):
    api_url = f'{gemini_base_url}{api_key}'
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(api_url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return content.strip() if content else None
    except Exception as e:
        print(f"API key {api_key} failed: {e}")
        return None

# Function to generate cases and retry with different API keys if an error occurs
def generate_case_with_retry(prompt, max_retries=5):
    for attempt in range(max_retries):
        current_api_key = next(api_key_cycle)
        response = generate_gemini_response(prompt, current_api_key)
        if response:
            return response
        print(f"Retrying with a different API key (attempt {attempt + 1}/{max_retries})...")
        time.sleep(2)  # Sleep between retries
    return None

# Save the brief and applicable law to the CSV file immediately after generation
def save_case_to_csv(small_brief, applicable_law, csv_file_path):
    # Prepare the row with small brief and applicable law
    case_data = {
        'small_brief': small_brief,
        'applicable_law': applicable_law
    }
    
    # Convert the case data to a DataFrame
    df = pd.DataFrame([case_data])
    
    # Check if the CSV file exists, if it does append without header, otherwise create new file
    if not os.path.isfile(csv_file_path):
        df.to_csv(csv_file_path, index=False)
        print(f"CSV file created at {csv_file_path}.")
    else:
        df.to_csv(csv_file_path, mode='a', header=False, index=False)
        print(f"Case appended to {csv_file_path}.")

# Function to generate multiple cases and save only the small brief and applicable law
def generate_cases(num_cases, csv_file_path):
    for i in range(num_cases):
        print(f"Generating case {i + 1} of {num_cases}...")
        
        # Generate the prompt for the current case
        prompt, applicable_law = generate_prompt()
        
        # Get the response from Gemini with retry logic
        small_brief = generate_case_with_retry(prompt)
        
        if small_brief:
            print(f"Case {i + 1} generated successfully.")
            # Save the brief and applicable law to the CSV file immediately after generation
            save_case_to_csv(small_brief, applicable_law, csv_file_path)
        else:
            print(f"Failed to generate case {i + 1} after multiple attempts.")
        
        # Delay to avoid hitting rate limits
        time.sleep(1)

# Ask the user for the number of cases to generate
try:
    num_cases = int(input("Enter the number of cases to generate: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit(1)

# Define the path for the output CSV file
csv_file_path = 'commercial_cases_output.csv'

# Generate the specified number of cases and append to CSV after each generation
generate_cases(num_cases, csv_file_path)

print(f"Data generation complete. {num_cases} case(s) generated and appended to {csv_file_path}.")