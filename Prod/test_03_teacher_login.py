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


class TestSignUp(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://qat.srds.ai/" == self.get_url()

    def test_empty_username(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        assert "Please enter"

    def test_negative_login(self, username_field):
        obj = Paths(self.driver)
        self.clear_field(obj.enter_email())
        obj.enter_email().send_keys(username_field['user_name'])
        showing_error_msg = obj.show_validation_message().text
        assert "Please enter" in showing_error_msg
        time.sleep(0.2)

    def test_positive_login(self, username_field):
        file_path = "C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\Prod\\last_teacher_email_index.txt"
        obj = Paths(self.driver)
        self.driver.refresh()

        def read_file(path_file):
            with open(path_file, 'r') as file:
                data = file.read()
            return data

        file_data = read_file(file_path)
        self.clear_field(obj.enter_email())
        time.sleep(0.2)
        print(f"Entering email: {file_data}")
        obj.enter_email().send_keys(file_data)
        obj.click_code_button().click()

        # Verification code

        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        obj.final_login_btn().click()
        self.getLogger().info(f"Login attempt successful with email: {file_data}")

    @pytest.fixture(params=Data.getTestData("user", "../testcases/login.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
