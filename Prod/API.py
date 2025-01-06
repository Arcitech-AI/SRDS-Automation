import pandas as pd
import requests
import json

# df = pd.read_excel('C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\schoology.xlsx', engine='openpyxl')
#
#
# # Function to make the API request
# def make_api_request(row):
#     url = row['API URL']
#     method = row['Method'].upper()
#     headers = {
#         'Authorization': f"Bearer {row['Token']}",
#         'Content-Type': 'application/json',
#         'x-api-key': row['Key']  # Assuming the Key goes here as a custom header
#     }
#     data = row['Data']
#
#     response = None
#     if method == 'POST':
#         response = requests.post(url, json=json.loads(data), headers=headers)
#
#     return response
#
#
# # Loop through each row and make the API request
# for index, row in df.iterrows():
#     response = make_api_request(row)
#     if response:
#         # Update the Excel file with the response and status
#         df.at[index, 'Response'] = response.text
#         df.at[index, 'Status'] = response.status_code
#
# # Save the updated Excel file with responses
# df.to_excel('C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\apis_with_respons.xlsx', index=False)
#
# print("API requests completed and responses saved.")


import pandas as pd
import requests
import json
from datetime import datetime
import os

df = pd.read_excel('C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\schoology.xlsx', engine='openpyxl')

# Initialize counter for API hits
api_hit_count = 1000

if 'Timestamp' not in df.columns:
    df['Timestamp'] = None


# Function to make the API request
def make_api_request(row, index):
    global api_hit_count
    url = row['API URL']
    method = row['Method'].upper()
    headers = {
        'Authorization': f"Bearer {row['Token']}",
        'Content-Type': 'application/json',
        'x-api-key': row['Key']
    }
    data = row['Data']
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = None
    try:
        if method == 'POST':
            print(f"Making API call at: {current_time}")

            response = requests.post(url, json=json.loads(data), headers=headers)
            api_hit_count += 1  # Increment counter for successful API call

        # Add timestamp for the API call
        df.at[index, 'Timestamp'] = current_time
        print(f"API call {api_hit_count} completed. Status: {response.status_code}")

    except Exception as e:
        print(f"Error making API request at : {current_time}: {str(e)}")

    return response


# Loop through each row and make the API request
for index, row in df.iterrows():
    response = make_api_request(row, index)
    if response:
        # Update the Excel file with the response and status
        df.at[index, 'Response'] = response.text
        df.at[index, 'Status'] = response.status_code

# Add total API hits to the DataFrame
df['API_Hit_Count'] = api_hit_count

# Save the updated Excel file with responses
df.to_excel = 'C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\testcases\\apis_with_respons.xlsx'

print(f"\nSummary:")
print(f"Total number of successful API hits: {api_hit_count}")
print(f"Final API call completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Responses saved to Excel file.")
