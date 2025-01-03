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

    def test_login(self, username_field):
        obj = Paths(self.driver)
        # obj.start_button().click()
        # obj.login_verification_code().click()

        for i in range(1, 3):
            obj.start_button().click()
            obj.login_verification_code().click()
            # email = f"omkarhundre+{i:03d}@arcitech.ai"
            obj.enter_email().send_keys(username_field['user_name'])
            # obj.enter_email().send_keys("omkarhundre@arcitech.ai")
            time.sleep(2)
            obj.click_code_button().click()
            time.sleep(2)
            otp_sequence = [2, 8, 0, 5, 9, 9]
            otp_inputs = obj.enter_code()

            for otp_inp, otp in zip(otp_inputs, otp_sequence):
                time.sleep(0.2)
                otp_inp.send_keys(str(otp))

            obj.final_login_btn().click()

    @pytest.fixture(params=Data.getTestData("../testcases/usernames.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
