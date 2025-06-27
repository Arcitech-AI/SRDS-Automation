import time
import pytest

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Object.homepage import Paths
from Utilities.baseclass import *


class TestAssignmentSubmission(Baseclass):

    # Existing Teacher Login
    # @pytest.mark.skip
    def test_student_login(self):
        email = "omkarhundre+01@arcitech.ai"
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        self.driver.refresh()
        self.clear_field(obj.enter_email())
        time.sleep(0.2)
        obj.enter_email().send_keys(email)
        time.sleep(0.2)
        obj.click_code_button().click()

        # Verification code

        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        obj.final_login_btn().click()
        time.sleep(2)
        self.getLogger().info(f"Login attempt successful with email: {email}")

    def test_submissions(self):
        obj = Paths(self.driver)
        obj.click_on_my_courses().click()
        obj.click_active_course().click()
        obj.click_go_to_courses().click()
        time.sleep(10)
        # obj.click_start_lesson().click()
        obj.click_on_the_assignments().click()
        obj.click_mcq_assignment().click()
        obj.click_start_assignment().click()
