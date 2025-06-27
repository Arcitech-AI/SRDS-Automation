import os
import time
import uuid
from datetime import datetime

import pytest
from selenium.common import StaleElementReferenceException

from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Object.homepage
from Object.homepage import Paths
from Utilities.baseclass import *
from testdata.testcase_data import *


class TestSignUpTeacher(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://pre.srds.ai/" == self.get_url()
        # assert "https://srds.ai/" == self.get_url()

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

    def test_generate_unique_email(self):
        timestamp = int(time.time())
        unique_id = str(uuid.uuid4().hex[:6])
        # assert '@arcitech.ai' in generated_email, f"Expected an email with '@arcitech.ai', but got {generated_email}"
        return f"test_{timestamp}_{unique_id}@arcitech.ai"

    def test_student_positive_signup(self):
        obj = Paths(self.driver)
        email = self.test_generate_unique_email()
        print(f"Generated Email: {email}")
        self.getLogger().info(f"Signup with email: {email}")
        save_new_teacher_email_index(email)
        self.driver.refresh()
        obj.enter_email().send_keys(email)
        obj.click_code_button().click()

        # Verification code
        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        time.sleep(1)
        obj.signup_otp_confirm_btn().click()
        self.getLogger().info(f"Congratulation {email} has been registered")
        time.sleep(5)

    def test_teacher_negative_profile(self):
        obj = Paths(self.driver)
        obj.create_student_profile().click()
        obj.profile_next_button().click()
        time.sleep(5)
        validation = obj.check_to_name_validation().text
        assert 'This field is required' in validation

    def test_teacher_positive_profile(self):
        obj = Paths(self.driver)
        obj.student_name().send_keys("Student")
        obj.student_grades_dropdown().click()
        A = obj.student_select_grade()

        while True:
            try:
                for i in A:
                    if i.text == "Grade 7" and i.is_displayed():
                        i.click()
                        print("Std is selected successfully")
                        break
                break

            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Re-fetching the standard list.")
                A = obj.student_select_grade()
                time.sleep(12)

        obj.student_gender_dropdown().click()
        obj.student_selected_gender().click()
        time.sleep(5)

        obj.open_calender().click()
        obj.select_year().click()

        while True:
            year_text = obj.select_year().text
            if year_text == "2017":
                break
            obj.back_year().click()

        obj.birth_year().click()
        obj.birth_month().click()

        obj.language_dropdown().click()
        obj.select_student_language().click()
        obj.location().send_keys('Thane')
        obj.location_dropdown().click()
        time.sleep(2)
        obj.profile_next_button().click()

        # Enter the descriptions of profile
        obj.enter_msg().send_keys(" I am brave student. my fav subject is English. ")
        time.sleep(2)
        obj.profile_next_button().click()

        # Select Interested subject
        obj.selected_interested_subject().click()
        obj.click_finish_btn().click()
        time.sleep(2)

    @pytest.fixture(params=Data.getTestData("user", "../testcases/sign_up.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
