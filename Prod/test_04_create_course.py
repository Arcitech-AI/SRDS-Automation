import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Object.homepage import Paths
from Utilities.baseclass import *


class TestCreateCourse(Baseclass):

    def test_teacher_login(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        file_path = "C:\\Users\\Admin\\PycharmProjects\\QAT_SRDS\\Prod\\last_teacher_email_index.txt"
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

    # create a course

    def test_create_course(self):
        obj = Paths(self.driver)
        time.sleep(2)
        obj.create_course().click()

    def test_empty_course_name(self):
        obj = Paths(self.driver)
        obj.course_name().send_keys(Keys.ENTER)

    def test_negative_course_name(self):
        obj = Paths(self.driver)
        negative_data = ["!@#$qwer", "!#$%^asdfg1234", "!@#$%^&*()_+=<>?,./"]

        for i in negative_data:
            obj.course_name().send_keys(i)
            obj.course_name().send_keys(Keys.ENTER)
            A = obj.error_msg_course_name().text

            if "Course name should only contain letters, numbers, and hyphen." in A:
                self.clear_field(obj.course_name())
                time.sleep(2)
            else:
                print("Please enter correct data")
        self.clear_field(obj.course_name())
        time.sleep(2)
        obj.course_name().send_keys("Performance Testing")

    def test_negative_and_positive_subject_name(self):
        obj = Paths(self.driver)
        obj.select_course_subject_dropdown().click()
        subject_list = (obj.select_course_subject_list())

        for subject in subject_list:
            if subject.text == "English":
                subject.click()
                break
        time.sleep(5)

    def test_select_start_std(self):
        obj = Paths(self.driver)
        obj.click_start_std_dropdown().click()

        while True:
            try:
                std = obj.select_start_std()
                for i in std:
                    if i.text == "Grade 1":
                        i.click()
                        print("Std is selected successfully")
                        return
                break

            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Re-fetching the standard list.")

    def test_select_end_std(self):
        obj = Paths(self.driver)
        obj.click_end_std_dropdown().click()

        while True:
            try:
                std = obj.select_end_std()
                for i in std:
                    if i.text == "Grade 10":
                        i.click()
                        print("Std is selected successfully")
                        return
                break

            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Re-fetching the standard list.")

    def test_select_start_date(self):
        obj = Paths(self.driver)
        obj.click_select_calendar().click()
        lst = obj.select_current_date()
        for i in lst:
            if self.select_current_date() == i.text:
                time.sleep(1)
                i.click()
                break

    @pytest.mark.skip
    def test_select_end_date(self):
        obj = Paths(self.driver)
        obj.click_select_end_calendar().click()
        obj.click_select_end_date().click()

    def test_ai_course_description(self):
        obj = Paths(self.driver)
        time.sleep(10)
        obj.enhanced_course_description().click()
        time.sleep(10)

    def test_course_image(self):
        obj = Paths(self.driver)
        A = obj.upload_image()
        file_path = r"C:\\Users\\Admin\\Pictures\\Course_image\\Course_image.png"
        A.send_keys(file_path)
        obj.save_image().click()
        time.sleep(10)
        obj.complete_course_button().click()


