import os
import time
import pytest

from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Object.homepage import Paths
from Utilities.baseclass import *
from testdata.testcase_data import *


class TestLogin(Baseclass):
    def test_login(self):
        # Get all test data first
        test_data = Data.getTestData("../testcases/usernames.xlsx")

        for user_data in test_data:
            try:
                # Initialize driver for each iteration
                options = Options()
                options.add_experimental_option("detach", True)
                options.add_argument('ignore-certificate-errors')
                options.add_argument("--disable-application-cache")

                service_obj = Service()
                self.driver = webdriver.Chrome(service=service_obj, options=options)
                self.driver.get("https://qat.srds.ai/")
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)

                obj = Paths(self.driver)
                obj.start_button().click()
                obj.login_verification_code().click()
                email = user_data['user_name']
                obj.enter_email().send_keys(email)
                obj.click_code_button().click()
                otp_sequence = [2, 8, 0, 5, 9, 9]
                otp_inputs = obj.enter_code()

                for otp_inp, otp in zip(otp_inputs, otp_sequence):
                    time.sleep(0.2)
                    otp_inp.send_keys(str(otp))
                obj.final_login_btn().click()
                time.sleep(2)
                print(f"Successfully login with email: {email}")

            except Exception as e:
                print(f"Error during login for {user_data['user_name']}: {str(e)}")

            finally:
                # Close browser after each iteration
                if hasattr(self, 'driver'):
                    self.driver.quit()
                time.sleep(2)  # Wait before starting next iteration
