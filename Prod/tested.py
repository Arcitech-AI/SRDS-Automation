# import os
# import time
# import pytest
#
# from concurrent.futures import ThreadPoolExecutor
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from Object.homepage import Paths
# from Utilities.baseclass import *
# from testdata.testcase_data import *
#
#
# class TestSignUp(Baseclass):
#
#     def read_excel_data(self):
#         """Read email data from Excel file"""
#         try:
#             current_dir = os.path.dirname(os.path.abspath(__file__))
#             excel_path = os.path.join(current_dir, "testcases", "usernames.xlsx")
#
#             df = pd.read_excel(excel_path)
#             email_list = df['user_name'].tolist()
#             print(f"Found {len(email_list)} emails to process")
#             return email_list
#
#         except Exception as e:
#             print(f"Error reading Excel file: {e}")
#             return []
#
#     def signup_user(self, email, user_data=None):
#         obj = Paths(self.driver)
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         options.add_argument("--disable-notifications")
#         driver = webdriver.Chrome(options=options)
#
#         try:
#             # Open website
#             driver.get("https://qat.srds.ai/")
#             time.sleep(2)
#
#             # Click Login
#             obj.start_button().click()
#             time.sleep(1)
#
#             # Click Sign up
#             obj.signup_button().click()
#             time.sleep(1)
#
#             # Select Teacher role
#             obj.role_option().click()
#             time.sleep(1)
#
#             obj.select_role().click()
#             time.sleep(1)
#
#             obj.select_signup_option().click()
#             time.sleep(1)
#
#             # Enter email
#
#             email = user_data['user_name']
#             obj.enter_email().send_keys(email)
#             email.clear()
#             time.sleep(1)
#
#             # Send verification code
#             obj.click_code_button().click()
#             time.sleep(2)
#
#             # Enter OTP
#             otp_sequence = [2, 8, 0, 5, 9, 9]
#             otp_inputs = obj.enter_code()
#
#             # Fill OTP digits with delay
#             for input_field, digit in zip(otp_inputs, otp_sequence):
#                 input_field.send_keys(str(digit))
#                 time.sleep(0.5)
#
#             # Complete signup
#             obj.signup_otp_confirm_btn().click()
#             time.sleep(2)
#
#             print(f"✓ Successfully signed up: {email}")
#
#         except Exception as e:
#             print(f"✗ Error processing {email}: {str(e)}")
#
#         finally:
#             try:
#                 driver.quit()
#             except:
#                 pass
#
#
# def main(read_excel_data, signup_user):
#     # Read emails from Excel
#     email_list = read_excel_data()
#     if not email_list:
#         print("No emails found to process")
#         return
#
#     # Use ThreadPoolExecutor for concurrent signup
#     with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust the number of workers as needed
#         executor.map(signup_user, email_list)
#
#
# if __name__ == "__main__":
#     main()


import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


class Paths:
    # Define the methods (start_button, signup_button, etc.) based on your element locators.
    pass


@pytest.fixture(scope="module")
def driver():
    """Fixture for setting up the WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


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


def signup_user(driver, email):
    obj = Paths(driver)  # Assuming you pass the driver into the Paths object
    try:
        driver.get("https://qat.srds.ai/")
        time.sleep(2)
        obj.start_button().click()
        time.sleep(1)
        obj.signup_button().click()
        time.sleep(1)
        obj.role_option().click()
        time.sleep(1)
        obj.select_role().click()
        time.sleep(1)
        obj.select_signup_option().click()
        time.sleep(1)

        # Enter email
        obj.enter_email().send_keys(email)
        time.sleep(1)

        # Send verification code
        obj.click_code_button().click()
        time.sleep(2)

        # Enter OTP
        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        # Fill OTP digits with delay
        for input_field, digit in zip(otp_inputs, otp_sequence):
            input_field.send_keys(str(digit))
            time.sleep(0.5)

        # Complete signup
        obj.signup_otp_confirm_btn().click()
        time.sleep(2)

        print(f"✓ Successfully signed up: {email}")
    except Exception as e:
        print(f"✗ Error processing {email}: {str(e)}")


def test_signup_users(driver):
    """Test case for signing up users using the read_excel_data and signup_user methods."""
    email_list = read_excel_data()
    if not email_list:
        print("No emails found to process")
        return

    # Use ThreadPoolExecutor for concurrent signup
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(lambda email: signup_user(driver, email), email_list)
