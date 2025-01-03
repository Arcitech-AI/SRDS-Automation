import pandas as pd
import requests
import json

df = pd.read_excel('C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\schoology.xlsx', engine='openpyxl')


# Function to make the API request
def make_api_request(row):
    url = row['API URL']
    method = row['Method'].upper()
    headers = {
        'Authorization': f"Bearer {row['Token']}",
        'Content-Type': 'application/json',
        'x-api-key': row['Key']  # Assuming the Key goes here as a custom header
    }
    data = row['Data']

    response = None
    if method == 'POST':
        response = requests.post(url, json=json.loads(data), headers=headers)

    return response


# Loop through each row and make the API request
for index, row in df.iterrows():
    response = make_api_request(row)
    if response:
        # Update the Excel file with the response and status
        df.at[index, 'Response'] = response.text
        df.at[index, 'Status'] = response.status_code

# Save the updated Excel file with responses
df.to_excel('C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\apis_with_respons.xlsx', index=False)

print("API requests completed and responses saved.")
