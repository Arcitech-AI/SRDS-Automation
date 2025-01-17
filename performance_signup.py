import requests
from h11._abnf import status_code
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def read_excel_data():
    """Read email data from Excel file"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        excel_path = os.path.join(current_dir, "testcases", "usernames.xlsx")

        df = pd.read_excel(excel_path)
        email_list = df['user_name'].tolist()
        print(f"Found {len(email_list)} emails to process")
        return email_list

    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []


def signup_user(email):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)

    try:
        # Open website
        driver.get("https://qat.srds.ai/")
        time.sleep(2)

        # Click Login
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(1)

        # Click Sign up
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign up']").click()
        time.sleep(1)

        # Select Teacher role
        driver.find_element(By.XPATH, "//div[@id='role-select']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//li[normalize-space()='I am a Teacher']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//p[normalize-space()='Sign Up with Verification Code']").click()
        time.sleep(1)

        # Enter email

        email_field = driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.clear()
        email_field.send_keys(email)
        time.sleep(1)

        # Send verification code
        send_code_button = driver.find_element(By.XPATH, "//button[normalize-space()='Send Code']")
        send_code_button.click()
        time.sleep(2)

        # Enter OTP
        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = driver.find_elements(By.XPATH, "//div[@label='6-Digit Code']/div/div/input")

        # Fill OTP digits with delay
        for input_field, digit in zip(otp_inputs, otp_sequence):
            input_field.send_keys(str(digit))
            time.sleep(0.5)

        # Complete signup
        signup_final = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']")
        signup_final.click()
        time.sleep(2)

        print(f"✓ Successfully signed up: {email}")

    except Exception as e:
        print(f"✗ Error processing {email}: {str(e)}")

    finally:
        try:
            driver.quit()
        except:
            pass


def main():
    # Read emails from Excel
    email_list = read_excel_data()
    if not email_list:
        print("No emails found to process")
        return

    # Use ThreadPoolExecutor for concurrent signup
    with ThreadPoolExecutor(max_workers=50) as executor:  # Adjust the number of workers as needed
        executor.map(signup_user, email_list)


if __name__ == "__main__":
    main()

# second code
# # options = webdriver.ChromeOptions()
# # options.add_argument("--start-maximized")
# # options.add_argument("--disable-notifications")
# # driver = webdriver.Chrome(options=options)
# #
# # driver.get("https://qat.srds.ai/")
# # time.sleep(2)  # Allow page to fully load
# #
# #         # Click Login
# # driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
# # time.sleep(1)
# #
# #         # Click Sign up
# # driver.find_element(By.XPATH, "//a[normalize-space()='Sign up']").click()
# # time.sleep(1)
# #
# #         # Select Teacher role
# # driver.find_element(By.XPATH, "//div[@id='role-select']").click()
# # time.sleep(1)
# #
# # driver.find_element(By.XPATH, "//li[normalize-space()='I am a Teacher']").click()
# # time.sleep(1)
# #
# # driver.find_element(By.XPATH, "//p[normalize-space()='Sign Up with Verification Code']").click()
# #         # Enter email
# # time.sleep(10)
# # email_field = driver.find_element(By.XPATH, "//input[@name='email']")
# # email_field.clear()
# # email_field.send_keys("omkar@arcitech.ai")
# # time.sleep(1)
# #
# #
# #
# #         # Send verification code
# # send_code_button = driver.find_element(By.XPATH, "//button[normalize-space()='Send Code']")
# # send_code_button.click()
# # time.sleep(2)
# #
# #         # Enter OTP
# # otp_sequence = [2, 8, 0, 5, 9, 9]
# # otp_inputs = driver.find_elements(By.XPATH, "//div[@label='6-Digit Code']/div/div/input")
# #
# #         # Fill OTP digits with delay
# # for input_field, digit in zip(otp_inputs, otp_sequence):
# #     input_field.send_keys(str(digit))
# #     time.sleep(0.5)
# #
# #         # Complete signup
# # signup_final = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']")
# # signup_final.click()
# # time.sleep(2)


# def api_performance_test():
#     url = "https://qat.srds.ai/api/auth/login-user/v2/"
#     payload = {"param1": "{email: 'omkarhundre@arcitech.ai'}"}
#     # headers = {"Authorization": "Bearer your_token"}
#     try:
#         response = requests.post(url, data=payload)
#         if response.status_code == 200:
#             print(f"API call successful with response time: {response.elapsed.total_seconds()} seconds")
#         else:
#             print(f"API call failed with status code {response.status_code}")
#     except Exception as e:
#         print(f"Error in API test: {e}")


# import requests
#
# # Define the API URL
# url = "https://qat.srds.ai/api/auth/login-user/v2/"
#
# # Define the payload for the POST request (email and OTP)
# payload = {
#     "email": "omkarhundre@arcitech.ai",
#     "otp": "280599"
# }
#
# # Define headers (if needed, based on Postman setup)
# headers = {
#     'Content-Type': 'application/json',  # Define the content type
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
# }
#
# # Make the POST request
# response = requests.post(url, json=payload, headers=headers)
#
# # Check if the response was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     response_data = response.json()
#
#     # Output the response data
#     print(f"Status: {response_data['status']}")
#     print(f"Message: {response_data['message']}")
#     print(f"Role: {response_data['role']}")
#     print(f"Token: {response_data['token']}")
# else:
#     # If the request failed, print the error
#     print(f"Request failed with status code {response.status_code}")
#     print(f"Error: {response.text}")
