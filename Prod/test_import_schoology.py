import time
from Object.homepage import Paths
from Utilities.baseclass import *
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver


class TestLoginTeacher(Baseclass):

    def test_teacher_login(self, driver):
        obj = Paths(driver)
        obj.start_button().click()
        obj.login_verification_code().click()
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

    def test_schoology(self, driver):
        obj = Paths(driver)
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

    def run_in_parallel(self):
        # Use ThreadPoolExecutor for concurrent execution of tests
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(self._run_test_teacher_login),
                executor.submit(self._run_test_schoology)
            ]
            for future in futures:
                future.result()

    def _run_test_teacher_login(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)

        try:
            self.test_teacher_login(driver)
        finally:
            driver.quit()

    def _run_test_schoology(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)

        try:
            self.test_schoology(driver)
        finally:
            driver.quit()


if __name__ == "__main__":
    test = TestLoginTeacher()
    test.run_in_parallel()
