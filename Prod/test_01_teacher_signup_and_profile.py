import os
import time
import pytest
import uuid

from Object.homepage import Paths
from selenium.webdriver.support.ui import Select
from Utilities.baseclass import *
from testdata.testcase_data import *


class TestSignUpStudent(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://pre.srds.ai/" == self.get_url()
        # assert "https://srds.ai/" == self.get_url()

    def test_teacher_empty_username(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.signup_button().click()
        time.sleep(0.2)
        obj.role_option().click()
        obj.select_teacher_role().click()
        time.sleep(0.2)
        obj.select_signup_option().click()
        time.sleep(0.2)
        obj.enter_email().click()
        assert "Enter Email"

    def test_teacher_negative_signup(self, username_field):
        obj = Paths(self.driver)
        self.clear_field(obj.enter_email())
        obj.enter_email().send_keys(username_field['user_name'])
        showing_error_msg = obj.show_validation_message().text
        assert "Please enter" in showing_error_msg
        time.sleep(0.2)

    # @pytest.mark.skip
    def test_generate_unique_email(self):
        timestamp = int(time.time())
        unique_id = str(uuid.uuid4().hex[:6])
        return f"test_{timestamp}_{unique_id}@arcitech.ai"

    def test_teacher_positive_signup(self):
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

    def test_teacher_positive_profile(self):
        obj = Paths(self.driver)
        obj.create_teacher_profile().click()
        dropdown_element = obj.select_title_dropdown()
        select_title = Select(dropdown_element)
        select_title.select_by_visible_text('Mr.')
        obj.setup_enter_name().send_keys("Teacher")
        obj.select_calendar().click()
        obj.select_date().click()
        dropdown_gender = obj.select_gender()
        select_gender = Select(dropdown_gender)
        select_gender.select_by_visible_text('Male')
        obj.select_location().send_keys('Thane')
        obj.location_dropdown().click()
        obj.enter_linkedin_url().send_keys("abc")
        obj.select_language().click()
        self.next_button().click()

    def test_negative_about_teacher(self):
        time.sleep(1)
        self.back_button().click()
        time.sleep(0.2)
        self.next_button().click()
        time.sleep(0.2)
        self.next_button2().click()
        time.sleep(0.2)

    def test_positive_about_teacher(self):
        obj = Paths(self.driver)
        obj.write_teacher_about().send_keys("I am Teacher")
        self.next_button2().click()

    def test_negative_subject_you_teach(self):
        self.next_button2().click()

    def test_positive_subject_tou_teach(self):
        obj = Paths(self.driver)
        obj.subject_name().send_keys("Maths")
        obj.select_subject().click()
        obj.subject_add().click()
        self.next_button2().click()

    def test_negative_personalize_your_ai_assistant(self):
        obj = Paths(self.driver)
        self.clear_field(obj.ai_name())
        obj.profile_submit().click()

    def test_positive_personalize_your_ai_assistant(self):
        obj = Paths(self.driver)
        obj.ai_tone().click()
        obj.ai_tone_checkbox().click()
        obj.ai_tone().click()
        obj.ai_msg().click()
        obj.ai_msg_checkbox().click()
        # file_path = "C:\\Users\\Admin\\Downloads\\Teacher_image.png"
        file_path = r"C:\\Users\\Admin\\Pictures\\Teacher_image\\Teacher_image.jpg"
        obj.add_teacher_image().send_keys(file_path)
        obj.save_image().click()
        obj.profile_submit().click()
        print("Teacher Profile successfully created.")
        time.sleep(10)

    def test_signup_user(self):
        self.open_profile().click()
        self.logout_button().click()

    @pytest.fixture(params=Data.getTestData("user", "../testcases/sign_up.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
