import time
import pytest

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Object.homepage import Paths
from Utilities.baseclass import *


class TestCreateCourse(Baseclass):

    # Existing Teacher Login
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
        obj.enter_email().send_keys(file_data)
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
        obj.course_name().send_keys("Software Testing")

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
        obj.generate_image().click()
        # A = obj.upload_image()
        # file_path = r"C:\\Users\\Admin\\Pictures\\Course_image\\Course_image.png"
        # A.send_keys(file_path)
        # obj.save_image().click()
        time.sleep(50)
        obj.complete_course_button().click()
        time.sleep(2)

    # Create a Lesson
    # @pytest.mark.skip
    def test_add_lesson(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_down(0, 800)
        time.sleep(5)
        obj.add_lesson().click()
        obj.enter_lesson_name().send_keys("Manual Testing")
        self.scroll_down(0, 500)
        obj.enter_prompt_for_lesson().send_keys("Create a lesson on Manual Testing in 5 lines")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(15)
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 800)
        time.sleep(2)
        self.lesson_proceed_button().click()
        self.back_to_course().click()
        time.sleep(5)

    """ create a Assignment with default rubric """
    """ create a mcq assignment """

    @pytest.mark.skip
    def test_add_mcq(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.mcq().click()
        # time.sleep(5)
        # self.clear_field(self.input_assignment_prompt())
        time.sleep(1)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(5)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_right_arrow_1().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

    """ create a true or false assignment"""

    @pytest.mark.skip
    def test_add_tf(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_1().click()
        time.sleep(2)
        self.add_new().click()
        time.sleep(2)
        self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_name().send_keys("TF")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.tf().click()
        time.sleep(5)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(5)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(15)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_2().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

    """ create a fill in the blanks assignment """

    @pytest.mark.skip
    def test_add_fitb(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_2().click()
        time.sleep(2)
        self.add_new().click()
        time.sleep(2)
        # self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("FITB")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.fitb().click()
        time.sleep(5)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(5)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(15)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_3().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

    """ create a short answer assignment """

    @pytest.mark.skip
    def test_add_short(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_3().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        # self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Short Ans")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.short().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(15)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_4().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

    """ create a essay assignment """

    @pytest.mark.skip
    def test_add_essay(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_4().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        # self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Essay")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.essay().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(15)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_5().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

    """ create a mixed assignment """

    @pytest.mark.skip
    def test_add_mixed(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_5().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        # self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Mixed")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.mixed().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(15)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_6().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        self.back_to_course().click()
        time.sleep(2)

    """ create a 2nd lesson """

    # @pytest.mark.skip
    def test_add_lesson2(self):
        obj = Paths(self.driver)
        self.add_lesson2().click()
        obj.enter_lesson_name().send_keys("Automation Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("Create a lesson on Automation Testing in 5 lines")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(25)
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(2)
        self.lesson_proceed_button().click()
        # self.back_to_course().click()
        time.sleep(2)

    """ create a mcq with custom rubric """

    def test_add_mcq_with_custom_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.mcq().click()
        time.sleep(1)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_right_arrow_1().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_mcq_rubric().click()
        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 2 marks")
        time.sleep(2)
        self.scroll_down(0, 1000)
        self.save_rubric_button().click()
        time.sleep(5)

    # @pytest.mark.skip
    def test_add_tf_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_1().click()
        time.sleep(2)
        self.add_new().click()
        time.sleep(2)
        # self.assignment_rubric_continue_btn().click()
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_name().send_keys("TF")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.tf().click()
        time.sleep(2)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_2().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(4)
        try:
            self.add_tf_rubric().click()

        except:
            self.assignment_rubric_continue_btn().click()

        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 2 marks")
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.save_rubric_button().click()
        time.sleep(5)

    # @pytest.mark.skip
    def test_add_fitb_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_2().click()
        time.sleep(2)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("FITB")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.fitb().click()
        time.sleep(5)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(5)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_3().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(4)
        try:
            self.add_fitb_rubric().click()

        except:
            self.assignment_rubric_continue_btn().click()
        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 2 marks")
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.save_rubric_button().click()
        time.sleep(5)

    # @pytest.mark.skip
    def test_add_short_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_3().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Short Ans")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.short().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_4().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(4)
        try:
            self.add_short_rubric().click()

        except:
            self.assignment_rubric_continue_btn().click()
        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 7.9 marks")
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.save_rubric_button().click()
        time.sleep(5)

    """ create a essay assignment """

    # @pytest.mark.skip
    def test_add_essay_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_4().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Essay")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.essay().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_5().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(4)
        try:
            self.add_essay_rubric().click()

        except:
            self.assignment_rubric_continue_btn().click()
        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 12.13 marks")
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.save_rubric_button().click()
        time.sleep(2)

    """ create a mixed assignment """

    # @pytest.mark.skip
    def test_add_mixed_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(2)
        self.add_new_assignment_5().click()
        time.sleep(2)
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 700)
        self.assignment_name().send_keys("Mixed")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.mixed().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 1 questions")
        self.assignment_create_button().click()
        time.sleep(60)
        obj.generator_left_body()
        self.scroll_down(0, 700)
        self.assignment_right_arrow_6().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(5)
        self.assignment_save_button().click()
        time.sleep(2)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(4)
        try:
            self.add_mixed_rubric().click()

        except:
            self.assignment_rubric_continue_btn().click()
        time.sleep(4)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 9 marks")
        time.sleep(2)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.save_rubric_button().click()
        time.sleep(2)
        self.back_to_course().click()
        time.sleep(50)


    """Add, Edit, Delete(Course, Lesson, Assignment)"""

    @pytest.mark.skip
    def test_add_course1(self):
        obj = Paths(self.driver)
        obj.create_course().click()
        obj.course_name().send_keys("Testing Course")
        self.test_select_start_std()
        self.test_select_end_std()
        self.test_select_start_date()

        obj.select_course_subject_dropdown().click()
        subject_list = (obj.select_course_subject_list())

        for subject in subject_list:
            if subject.text == "English":
                subject.click()
                break
        time.sleep(5)

        self.test_ai_course_description()
        self.test_course_image()
        time.sleep(2)

    """ Add lesson """

    @pytest.mark.skip
    def test_add_lesson1(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_down(0, 200)
        time.sleep(5)
        obj.add_lesson().click()
        obj.enter_lesson_name().send_keys("Manual Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("Create a lesson on Manual Testing in 5 lines")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(5)
        self.lesson_right_arrow().click()
        self.lesson_proceed_button().click()
        self.back_to_course().click()

    """ Add assignment """

    @pytest.mark.skip
    def test_add_assignment1(self):
        obj = Paths(self.driver)
        self.all_page()
        time.sleep(1)
        self.scroll_up(1000, 0)
        time.sleep(1)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        time.sleep(1)
        self.scroll_down(0, 500)
        time.sleep(1)
        self.assignment_name().send_keys("MCQ")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(1)
        self.mcq().click()
        time.sleep(1)
        self.clear_field(self.input_assignment_prompt())
        time.sleep(2)
        self.input_assignment_prompt().send_keys("Create 1 question for Assignment.")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(7)
        obj.generator_left_body()
        time.sleep(1)
        self.scroll_down(0, 700)
        time.sleep(1)
        self.assignment_right_arrow_1().click()
        time.sleep(1)
        self.assignment_save_button().click()
        print("Assignment creating successfully")
        self.back_to_course().click()

    """ Edit the Assignment """

    @pytest.mark.skip
    def test_edit_assignment1(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.edit_assignment2().click()
        self.add_new_assignment_1().click()
        self.select_assignment1().click()
        obj.edit_assignment().send_keys("Thank You")
        self.scroll_down(0, 800)
        time.sleep(2)
        self.assignment_save_button().click()
        self.back_to_course().click()

    """ Delete the assignment """

    @pytest.mark.skip
    def test_delete_assignment1(self):
        obj = Paths(self.driver)
        time.sleep(2)
        obj.delete_select_assignment().click()
        time.sleep(2)
        obj.delete_assignment().click()
        obj.confirm_delete_assignment().click()
        self.back_to_lesson().click()
        time.sleep(2)

    """ Edit the lesson """

    @pytest.mark.skip
    def test_edit_lesson1(self):
        obj = Paths(self.driver)
        self.preview_lesson().click()
        time.sleep(4)
        self.remove_to_chatbot().click()
        self.cut_chatbot().click()
        # self.clear_field(obj.enter_lesson_name())
        # time.sleep(2)
        # obj.enter_lesson_name().send_keys("Automation Testing")
        time.sleep(2)
        self.write_lesson().send_keys(" Thank You")
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        self.back_to_course().click()

    """ Delete the lesson """

    @pytest.mark.skip
    def test_delete_lesson1(self):
        obj = Paths(self.driver)
        self.delete_to_lesson().click()
        obj.confirm_delete_assignment().click()

    """ Edit the course """

    @pytest.mark.skip
    def test_edit_course1(self):
        obj = Paths(self.driver)
        self.edit_to_course().click()
        self.edit_to_description().click()
        time.sleep(7)
        self.edit_to_update_course().click()
        self.back_to_dashboard().click()

    """ Delete the course """

    @pytest.mark.skip
    def test_delete_course1(self):
        obj = Paths(self.driver)
        time.sleep(2)
        # self.remove_to_chatbot().click()
        self.cut_chatbot().click()
        self.scroll_down(0, 300)
        time.sleep(2)
        self.delete_option_course().click()
        self.delete_to_course().click()
        obj.confirm_delete_assignment().click()
