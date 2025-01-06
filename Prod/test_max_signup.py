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


class TestSignUp(Baseclass):
    def test_signup(self):
        # Get all test data first
        test_data = Data.getTestData("../testcases/usernames.xlsx")

        for user_data in test_data:
            try:
                options = Options()
                options.add_experimental_option("detach", True)
                options.add_argument('ignore-certificate-errors')
                options.add_argument("--disable-application-cache")

                service_obj = Service()
                self.driver = webdriver.Chrome(service=service_obj, options=options)
                self.driver.get("https://srds.ai/")
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)

                obj = Paths(self.driver)

                # Perform signup steps
                obj.start_button().click()
                obj.signup_button().click()
                time.sleep(1)

                obj.role_option().click()
                obj.select_role().click()
                time.sleep(1)

                obj.select_signup_option().click()
                time.sleep(1)

                # Enter email from Excel
                email = user_data['user_name']
                self.getLogger().info(f"Signing up with email: {email}")
                obj.enter_email().send_keys(email)
                # obj.enter_email().send_keys("omkarhundre+031@arcitech.ai")
                obj.click_code_button().click()
                otp_sequence = [2, 8, 0, 5, 9, 9]
                otp_inputs = obj.enter_code()

                for otp_inp, otp in zip(otp_inputs, otp_sequence):
                    time.sleep(0.2)
                    otp_inp.send_keys(str(otp))

                obj.signup_otp_confirm_btn().click()
                time.sleep(20)
                print(f"Successfully signed up with email: {email}")

            except Exception as e:
                print(f"Error during signup for {user_data['user_name']}: {str(e)}")

            finally:
                if hasattr(self, 'driver'):
                    self.driver.quit()
                time.sleep(2)
