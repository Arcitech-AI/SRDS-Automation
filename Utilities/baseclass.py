import inspect
import logging
import os
import pytest
import tensorflow as tf

from selenium.webdriver.common.by import By

from Prod.current_date_time import get_current_date


def generate_sequential_email(base="omkarhundre", domain="arcitech.ai", start=850):
    email = f"{base}+{start:03d}@{domain}"
    return email


def get_last_teacher_email_index(filename="last_teacher_email_index.txt"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        last_index = file.read().strip()
        return last_index


def save_new_teacher_email_index(email, filename="last_teacher_email_index.txt"):
    with open(filename, "w") as file:
        file.write(email)


def get_last_student_email_index(filename="last_student_email_index.txt"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        last_index = file.read().strip()
        return last_index


def save_new_student_email_index(email, filename="last_student_email_index.txt"):
    with open(filename, "w") as file:
        file.write(email)


@pytest.mark.usefixtures("Invoke_Browser")
class Baseclass:

    def get_url(self):
        return self.driver.current_url

    def clear_field(self, inp):
        self.driver.execute_script("arguments[0].value = '';", inp)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def next_button(self):
        return self.driver.find_element(By.XPATH, "//div[4]//div[3]//button[1]")

    def next_button2(self):
        return self.driver.find_element(By.XPATH, "//div[4]//div[3]//button[2]")

    def back_button(self):
        return self.driver.find_element(By.XPATH, "//div[4]//div[3]//button[1]")

    def logout_button(self):
        return self.driver.find_element(By.XPATH, "//ul[@role='menu']/li[2]")

    def open_profile(self):
        return self.driver.find_element(By.XPATH, "//div[@class='profile-wrapper']/div/div")

    def visible_error_msg(self):
        return self.driver.find_element(By.XPATH, "//div[@class='FieldError-container']/span/span[@role='alert']")

    def scroll_down(self, x, y):
        return self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x, y)

    def scroll_up(self, x, y):
        return self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x, y)

    def select_current_date(self):
        current_year, current_month, current_day = get_current_date()
        return str(current_day)

    def lesson_right_arrow(self):
        return self.driver.find_element(By.XPATH, "//i[@class='fa-solid fa-arrow-right']")

    def lesson_proceed_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']")

    def add_new_assignment(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment']")

    def add_new(self):
        return self.driver.find_element(By.XPATH, "//div[@id='add-assignment']")

    def add_new_assignment_1(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment 1']")

    def add_new_assignment_2(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment 2']")

    def add_new_assignment_3(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment 3']")

    def add_new_assignment_4(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment 4']")

    def add_new_assignment_5(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Assignment 5']")

    def pop_up_assignment(self):
        return self.driver.find_element(By.XPATH, "//div[@id='add-assignment']")

    def assignment_name(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MuiFormControl-root MuiTextField-root "
                                                  "custom-text-field css-i44wyl']/div/input")

    def assignment_timer_add(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='+']")

    def assignment_type_dropdown(self):
        return self.driver.find_element(By.XPATH, "//div[@role='combobox']")

    def assignment_create_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']//img")

    def mcq(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='Multiple Choice Questions']")

    def tf(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='True/False']")

    def fitb(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='Fill-In-The-Blanks']")

    def short(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='Short-Answer-Questions']")

    def essay(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='Essay-Questions']")

    def mixed(self):
        return self.driver.find_element(By.XPATH, "//li[normalize-space()='Mixed Questions']")

    def add_mcq_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric']")

    def add_tf_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric 1']")

    # def add_tf_rubric(self):
    #     return self.driver.find_element(By.XPATH, "//div[@class='tab-dropdown'][3]/button")

    def add_fitb_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric 2']")

    def add_short_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric 3']")

    def add_essay_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric 4']")

    def add_mixed_rubric(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Rubric 5']")

    def add_popup_rubric_button(self):
        return self.driver.find_element(By.XPATH, "//div[@id='add-assignment']")

    def enter_rubric_instruction(self):
        return self.driver.find_element(By.XPATH, "//div[@role='textbox']")

    def save_rubric_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def assignment_right_arrow_1(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[2]")

    def assignment_right_arrow_2(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[3]")

    def assignment_right_arrow_3(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[4]")

    def assignment_right_arrow_4(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[5]")

    def assignment_right_arrow_5(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[6]")

    def assignment_right_arrow_6(self):
        return self.driver.find_element(By.XPATH, "(//i[@data-tooltip-id='update-plugin'])[7]")

    def assignment_save_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def assignment_rubric_continue_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")

    def all_page(self):
        return self.driver.find_element(By.XPATH, "//div[@class='App']")

    def back_to_lesson(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Lesson Generator']")

    def back_to_course(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back to Course']")

    def back_to_dashboard(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='logo']")

    def add_lesson2(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Lesson']")

    def edit_assignment2(self):
        return self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Preview Lesson'])[1]")

    def select_assignment1(self):
        return self.driver.find_element(By.XPATH, "//div[@class='assignment-item']")

    def input_assignment_prompt(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='lesson_promote_flexible']")

    def left_body(self):
        return self.driver.find_element(By.XPATH, "//div[@class='lesson_generator_body_sec_left_body'] ")

    def right_body(self):
        return self.driver.find_element(By.XPATH, "//div[@class='lesson_generator_body_sec_right_body']")

    def cut_chatbot(self):
        return self.driver.find_element(By.XPATH, "//i[@class='fa-solid fa-x']")

    def back_to_dashboard(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Back']")

    def preview_lesson(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Preview Lesson']")

    def edit_lesson(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Manual Testing']")

    def write_lesson(self):
        return self.driver.find_element(By.XPATH, "//p[@class='editor-paragraph ltr']")

    def back_to_lesson(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Back']")

    def remove_to_chatbot(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@id='chatbot-widget-message-bubbles-container']/button[@id='chatbot-widget-messages-close-icon']/img")

    def delete_to_lesson(self):
        return self.driver.find_element(By.XPATH, "//i[@class='fa-solid fa-trash']")

    def edit_to_course(self):
        return self.driver.find_element(By.XPATH, "//button[@class='view-course-details-edit-and-share-folder']")

    def edit_to_description(self):
        return self.driver.find_element(By.XPATH, "//button[@class='Course-description-inner-ai-feilds']")

    def edit_to_update_course(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Update and Publish']")

    def delete_option_course(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='created-my-courses-container']//div[1]//div[2]//div[1]//div[2]//div[1]//i[1]")

    def delete_to_course(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='Delete']")
