from selenium.webdriver.common.by import By


class Paths:

    def __init__(self, driver):
        self.driver = driver

    # SignUp Paths

    click_button = (By.XPATH, "//a[normalize-space()='Login']")
    click_signup = (By.XPATH, "//a[normalize-space()='Sign up']")
    click_role_option = (By.XPATH, "//div[@id='role-select']")
    click_option_role = (By.XPATH, "//li[normalize-space()='I am a Teacher']")
    click_signup_option = (By.XPATH, "//p[normalize-space()='Sign Up with Verification Code']")
    click_enter_email = (By.XPATH, "//input[@name='email']")
    click_code = (By.XPATH, "//button[normalize-space()='Send Code']")
    click_enter_code = (By.XPATH, "//div[@label='6-Digit Code']/div/div/input")
    otp_confirmation = (By.XPATH, "//button[normalize-space()='Sign Up']")

    # Login Paths

    click_login_verification_code = (By.XPATH, "//p[normalize-space()='Login with Verification Code']")
    click_login_button = (By.XPATH, "//button[normalize-space()='Login']")

    # sign up functions

    def start_button(self):
        return self.driver.find_element(*Paths.click_button)

    def signup_button(self):
        return self.driver.find_element(*Paths.click_signup)

    def role_option(self):
        return self.driver.find_element(*Paths.click_role_option)

    def select_role(self):
        return self.driver.find_element(*Paths.click_option_role)

    def select_signup_option(self):
        return self.driver.find_element(*Paths.click_signup_option)

    def enter_email(self):
        return self.driver.find_element(*Paths.click_enter_email)

    def click_code_button(self):
        return self.driver.find_element(*Paths.click_code)

    def enter_code(self):
        return self.driver.find_elements(*Paths.click_enter_code)

    def signup_otp_confirm_btn(self):
        return self.driver.find_element(*Paths.otp_confirmation)

    # Login functions

    def login_verification_code(self):
        return self.driver.find_element(*Paths.click_login_verification_code)

    def final_login_btn(self):
        return self.driver.find_element(*Paths.click_login_button)
