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

    def test_signup(self, username_field):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.signup_button().click()
        time.sleep(1)
        obj.role_option().click()
        obj.select_role().click()
        time.sleep(1)
        obj.select_signup_option().click()
        time.sleep(1)
        obj.enter_email().send_keys(username_field['user_name'])
        obj.click_code_button().click()

    def test_verfication_code(self):
        obj = Paths(self.driver)
        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        obj.signup_otp_confirm_btn().click()
        self.driver.quit()
        time.sleep(2)

    @pytest.fixture(params=Data.getTestData("../testcases/usernames.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
