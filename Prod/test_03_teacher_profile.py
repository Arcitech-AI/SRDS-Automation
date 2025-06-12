import time

from selenium.webdriver.support.ui import Select
from Utilities.baseclass import *
from Object.homepage import Paths


class TestLoginTeacher(Baseclass):

    def test_teacher_login(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        file_path = "C:\\Users\\Admin\\PycharmProjects\\SRDS-Automation\\Prod\\last_teacher_email_index.txt"
        self.driver.refresh()

        # Read a file
        def read_file(path_file):
            with open(path_file, 'r') as file:
                data = file.read()
            return data

        file_data = read_file(file_path)
        self.clear_field(obj.enter_email())
        time.sleep(0.2)
        obj.enter_email().send_keys(file_data)
        obj.click_code_button().click()

        # Verification code

        otp_sequence = [2, 8, 0, 5, 9, 9]
        otp_inputs = obj.enter_code()

        for otp_inp, otp in zip(otp_inputs, otp_sequence):
            time.sleep(0.2)
            otp_inp.send_keys(str(otp))

        obj.final_login_btn().click()
        time.sleep(2)
        self.getLogger().info(f"Login attempt successful with email: {file_data}")

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
        time.sleep(10)

    def test_signup_user(self):
        self.open_profile().click()
        self.logout_button().click()
