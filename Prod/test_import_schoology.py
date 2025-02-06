import time

from Object.homepage import Paths
from Utilities.baseclass import *


class TestLoginTeacher(Baseclass):

    def test_teacher_login(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        file_path = "C:\\Users\\Admin\\PycharmProjects\\SRDS\\Prod\\last_teacher_email_index.txt"
        self.driver.refresh()

        # Read a file
        def read_file(path_file):
            with open(path_file, 'r') as file:
                data = file.read()
            return data

        file_data = read_file(file_path)
        self.clear_field(obj.enter_email())
        time.sleep(0.2)
        # obj.enter_email().send_keys(file_data)
        obj.enter_email().send_keys("omkarhundre@arcitech.ai")
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

    def test_schoology(self):
        obj = Paths(self.driver)
        obj.open_schoology_courses().click()
        time.sleep(1)
        self.scroll_down(0, 500)
        time.sleep(1)
        obj.refresh_schoology().click()
        obj.select_all_schoology().click()
        obj.next_btn_schoology().click()
        obj.start_sync_schoology_btn().click()
        time.sleep(5)
        obj.confirm_schoology_sync().click()
        time.sleep(10)