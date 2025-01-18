import os
import time
import pytest

from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Object.homepage import Paths
from Utilities.baseclass import *
from testdata.testcase_data import *


class TestSignUpTeacher(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://qat.srds.ai/" == self.get_url()

    def test_student_empty_username(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.signup_button().click()
        time.sleep(0.2)
        obj.role_option().click()
        obj.select_student_role().click()
        time.sleep(0.2)
        obj.select_signup_option().click()
        time.sleep(0.2)
        obj.enter_email().click()
        assert "Enter Email"

    def test_student_signup(self, username_field):
        obj = Paths(self.driver)
        self.clear_field(obj.enter_email())
        obj.enter_email().send_keys(username_field['user_name'])
        showing_error_msg = obj.show_validation_message().text
        assert "Please enter" in showing_error_msg
        time.sleep(0.2)

    def test_student_positive_signup(self):
        obj = Paths(self.driver)
        last_email = get_last_student_email_index()
        if last_email:
            try:
                last_index = int(last_email.split('+')[1].split('@')[0])
                new_index = last_index + 1
            except (IndexError, ValueError) as e:
                print(f"Error processing last email: {e}")
                new_index = 2000
        else:
            new_index = 2000
        email = generate_sequential_email(start=new_index)
        print(f"Generated Email: {email}")
        save_new_student_email_index(email)
        self.driver.refresh()
        obj.enter_email().send_keys(email)
        obj.click_code_button().click()

        # verification code

        obj = Paths(self.driver)
        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        obj.signup_otp_confirm_btn().click()
        time.sleep(10)
        self.getLogger().info(f"Congratulation {email} has been registered")

    @pytest.fixture(params=Data.getTestData("user", "../testcases/sign_up.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
