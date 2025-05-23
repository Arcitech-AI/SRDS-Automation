import time

from Object.homepage import Paths
from Utilities.baseclass import *
from testdata.testcase_data import *


class TestLoginTeacher(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://pre.srds.ai/" == self.get_url()

    def test_teacher_empty_username(self):
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        assert "Please enter"

    def test_teacher_negative_login(self, username_field):
        obj = Paths(self.driver)
        self.clear_field(obj.enter_email())
        obj.enter_email().send_keys(username_field['user_name'])
        showing_error_msg = obj.show_validation_message().text
        assert "Please enter" in showing_error_msg
        time.sleep(0.2)

    def test_teacher_positive_login(self):
        file_path = "C:\\Users\\Admin\\PycharmProjects\\SRDS\\Prod\\last_teacher_email_index.txt"
        obj = Paths(self.driver)
        self.driver.refresh()

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

    @pytest.fixture(params=Data.getTestData("user", "../testcases/login.xlsx"))
    def username_field(self, request):
        return request.param

    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self):
        yield
        self.driver.quit()
