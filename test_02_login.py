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

    def test_login(self):
        obj = Paths(self.driver)
        # obj.start_button().click()
        # obj.login_verification_code().click()

        for i in range(1, 3):
            obj.start_button().click()
            obj.login_verification_code().click()
            email = f"omkarhundre+{i:03d}@arcitech.ai"
            obj.enter_email().send_keys(email)
            time.sleep(2)
            obj.click_code_button().click()
            time.sleep(2)
            otp_sequence = [2, 8, 0, 5, 9, 9]
            otp_inputs = obj.enter_code()

            for otp_inp, otp in zip(otp_inputs, otp_sequence):
                time.sleep(0.2)
                otp_inp.send_keys(str(otp))

            obj.final_login_btn().click()



            # def test_login_with_verfication_code(self):
            #     obj = Paths(self.driver)
            #     otp_sequence = [2, 8, 0, 5, 9, 9]
            #     otp_inputs = obj.enter_code()
            #
            #     for otp_inp, otp in zip(otp_inputs, otp_sequence):
            #         time.sleep(0.2)
            #         otp_inp.send_keys(str(otp))
            #
            #     obj.final_login_btn().click()
            #     time.sleep(10)
