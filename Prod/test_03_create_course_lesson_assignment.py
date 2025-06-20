import time
import pytest

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Object.homepage import Paths
from Utilities.baseclass import *


class TestCreateCourse(Baseclass):

    # Existing Teacher Login
    # @pytest.mark.skip
    def test_teacher_login(self):
        email = "omkarh@arcitech.ai"
        obj = Paths(self.driver)
        obj.start_button().click()
        obj.login_verification_code().click()
        obj.enter_email().click()
        self.driver.refresh()
        self.clear_field(obj.enter_email())
        time.sleep(0.2)
        obj.enter_email().send_keys(email)
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
        self.getLogger().info(f"Login attempt successful with email: {email}")

    # create a course
    # @pytest.mark.skip
    def test_create_course(self):
        obj = Paths(self.driver)
        time.sleep(2)
        obj.create_course().click()

    # @pytest.mark.skip
    def test_empty_course_name(self):
        obj = Paths(self.driver)
        obj.course_name().send_keys(Keys.ENTER)

    # @pytest.mark.skip
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

    # @pytest.mark.skip
    def test_negative_and_positive_subject_name(self):
        obj = Paths(self.driver)
        obj.select_course_subject_dropdown().click()
        subject_list = (obj.select_course_subject_list())

        for subject in subject_list:
            if subject.text == "English":
                subject.click()
                break
        time.sleep(5)

    # @pytest.mark.skip
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

    # @pytest.mark.skip
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

    # @pytest.mark.skip
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

    # @pytest.mark.skip
    def test_ai_course_description(self):
        obj = Paths(self.driver)
        time.sleep(10)
        obj.enhanced_course_description().click()
        time.sleep(30)

    # @pytest.mark.skip
    def test_course_image(self):
        obj = Paths(self.driver)
        obj.generate_image().click()
        # A = obj.upload_image()
        # file_path = r"C:\\Users\\Admin\\Pictures\\Course_image\\Course_image.png"
        # A.send_keys(file_path)
        # obj.save_image().click()
        time.sleep(60)
        obj.complete_course_button().click()
        print("Successfully created the Software Testing course")
        time.sleep(2)

    "Create a Lesson"
    # @pytest.mark.skip
    def test_add_lesson(self):
        obj = Paths(self.driver)
        time.sleep(5)
        self.scroll_down(0, 900)
        time.sleep(5)
        obj.add_lesson().click()
        obj.enter_lesson_name().send_keys("Manual Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("I want the lesson of Manual Testing.")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(40)
        obj.scroller().click()
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(2)
        self.lesson_proceed_button().click()
        print("Successfully added the Manual Testing lesson.")
        # self.back_to_course().click()
        time.sleep(2)

    """ create a Assignment with default rubric """
    """ create a mcq assignment """

    # @pytest.mark.skip
    def test_add_mcq(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_down(0, 1000)
        time.sleep(10)
        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(2)
        self.mcq().click()
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the advanced questions")
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_1().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the MCQ assignment.")
        time.sleep(10)

    """ create a true or false assignment"""

    # @pytest.mark.skip
    def test_add_tf(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_1().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.assignment_rubric_continue_btn().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("TF")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.tf().click()
        self.input_assignment_prompt().send_keys(". give me the advanced level questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_2().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the True or False assignment.")
        time.sleep(10)

    """ create a fill in the blanks assignment """

    # @pytest.mark.skip
    def test_add_fitb(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_2().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("FITB")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.fitb().click()
        self.input_assignment_prompt().send_keys(". give me the advanced level questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_3().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the FITB assignment.")
        time.sleep(10)

    """ create a short answer assignment """

    # @pytest.mark.skip
    def test_add_short(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_3().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Short Answer")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.short().click()
        self.input_assignment_prompt().send_keys(". give me the advanced level questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_4().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the short answer assignment.")
        time.sleep(10)

    """ create a essay assignment """

    # @pytest.mark.skip
    def test_add_essay(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_4().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Essay")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.essay().click()
        self.input_assignment_prompt().send_keys(". give me the advanced level questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_5().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Essay assignment.")
        time.sleep(10)

    """ create a mixed assignment """

    # @pytest.mark.skip
    def test_add_mixed(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_5().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Mixed questions")
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.mixed().click()
        self.input_assignment_prompt().send_keys(". give me the advanced level questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_6().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Mixed assignment.")
        self.back_to_course().click()
        time.sleep(10)

    @pytest.mark.skip
    def test_example_course(self):
        obj = Paths(self.driver)
        self.scroll_down(0, 300)
        time.sleep(2)
        obj.open_previous_course().click()
        time.sleep(20)
        # obj.open_previous_first_lesson().click()
        # obj.open_previous_lesson().click()
        # time.sleep(2)
        # self.scroll_down(0, 900)
        # time.sleep(2)
        # obj.open_previous_third_lesson().click()

    """ create a 2nd lesson """

    # @pytest.mark.skip
    def test_add_lesson2(self):
        obj = Paths(self.driver)
        self.add_lesson_extra().click()
        obj.enter_lesson_name().send_keys("Automation Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("I want the basic knowledge of Automation Testing.")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(40)
        obj.scroller().click()
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(2)
        self.lesson_proceed_button().click()
        print("Successfully added the Automation Testing lesson.")
        # self.back_to_course().click()
        time.sleep(2)

    """ create a mcq with custom rubric """

    # @pytest.mark.skip
    def test_add_mcq_with_custom_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_down(0, 1000)
        time.sleep(10)
        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(2)
        self.mcq().click()
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_1().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the MCQ assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_mcq_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 2 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the MCQ custom rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_tf_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_1().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("TF")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.tf().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_2().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the True or False assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_tf_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 2.2 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the True or False custom rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_fitb_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_2().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("FITB")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.fitb().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_3().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the FITB assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_fitb_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 3.2 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the FITB custom rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_short_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_3().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Short Answer")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.short().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_4().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the short answer assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_short_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 12 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the Short answer rubric.")
        time.sleep(10)

    """ create a essay assignment """

    # @pytest.mark.skip
    def test_add_essay_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_4().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Essay")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.essay().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_5().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Essay assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_essay_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys("Each questions was 17 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the Essay custom rubric.")
        time.sleep(50)

    # @pytest.mark.skip
    def test_add_mixed_with_custom_rubric(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_5().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Mixed questions")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.mixed().click()
        self.input_assignment_prompt().send_keys(". give me the 14 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_6().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Mixed assignment.")
        time.sleep(10)

        """Add the custom rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_mixed_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        self.enter_rubric_instruction().send_keys(
            "MCQ is 3 marks. TF is 4 marks. FITB is 5 marks. Short answer is 7 marks. Essay is 9 marks")
        time.sleep(5)
        self.scroll_down(0, 500)
        time.sleep(10)
        self.save_rubric_button().click()
        print("Successfully added the Mixed custom rubric.")
        self.back_to_course().click()
        time.sleep(5)

    """Add on the 3rd Lesson"""

    # @pytest.mark.skip
    def test_add_lesson3(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -900)
        time.sleep(10)
        self.add_lesson_extra().click()
        obj.enter_lesson_name().send_keys("Performance Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("I want the deep knowledge for Performance Testing.")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(40)
        obj.scroller().click()
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(2)
        self.lesson_proceed_button().click()
        print("Successfully added the Performance Testing lesson.")
        # self.back_to_course().click()
        time.sleep(2)

    # @pytest.mark.skip
    def test_add_mcq_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_down(0, 1000)
        time.sleep(10)
        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(2)
        self.mcq().click()
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_1().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the MCQ assignment.")
        time.sleep(10)

        """Add the AI rubric"""
        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_mcq_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys(" and Each questions is 2 marks")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_2().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the MCQ ai rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_tf_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_1().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("TF")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.tf().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_3().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the True or False assignment.")
        time.sleep(10)

        """Add the ai rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_tf_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys(" and Each questions is 5 marks")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_4().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the True or False ai rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_fitb_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_2().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("FITB")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.fitb().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_5().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the FITB assignment.")
        time.sleep(10)

        """Add the ai rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_fitb_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys(" and based on previous questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_6().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the FITB ai rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_short_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_3().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Short")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.short().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_7().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Short answer assignment.")
        time.sleep(10)

        """Add the ai rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_short_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys(" and overall the 100 marks")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_8().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Short answer rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_essay_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_4().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Essay")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.essay().click()
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_9().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Essay assignment.")
        time.sleep(10)

        """Add the ai rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_essay_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys(" and each questions is 12 marks")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_10().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Essay ai rubric.")
        time.sleep(10)

    # @pytest.mark.skip
    def test_add_mixed_with_ai_rubric(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.scroll_up(0, -500)
        time.sleep(5)
        self.add_new_assignment_5().click()
        time.sleep(5)
        self.add_new().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(7)
        self.assignment_name().send_keys("Quiz")
        time.sleep(5)
        self.assignment_timer_add().click()
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        self.mixed().click()
        self.input_assignment_prompt().send_keys(". i want the 2 MCQ, 2 TF, 2 FITB, 2 Short, 2 Essay questions. ")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_11().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Mixed assignment.")
        time.sleep(10)

        """Add the ai rubric"""

        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_mixed_rubric().click()
        time.sleep(5)
        self.add_popup_rubric_button().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.input_assignment_prompt().send_keys("and MCQ is 3 marks, TF is 3.5 marks, FITB is 4 marks, Short answer "
                                                 "is 8, Essay is 9.9 marks.")
        time.sleep(2)
        self.assignment_create_button().click()
        time.sleep(40)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_12().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully added the Mixed ai rubric.")
        time.sleep(2)
        self.scroll_up(0, -700)
        self.back_to_course().click()
        # self.back_to_dashboard().click()
        time.sleep(10)

    "Student Invite flow"

    # @pytest.mark.skip
    def test_student_invite(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -700)
        time.sleep(2)
        obj.invite_student().click()
        obj.enter_mail_id().send_keys("ajay+27@arcitech.ai")
        obj.add_mail().click()
        obj.invite().click()
        print("Invited successfully")
        self.scroll_up(0, -700)
        self.back_to_dashboard().click()
        time.sleep(10)

    """Add, Edit, Delete(Course, Lesson, Assignment)"""

    # @pytest.mark.skip
    def test_add_course1(self):
        obj = Paths(self.driver)
        obj.create_course().click()
        obj.course_name().send_keys("API Course")
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
        print("Successfully created the API Course.")
        time.sleep(2)

    """ Add lesson """

    # @pytest.mark.skip
    def test_add_lesson1(self):
        obj = Paths(self.driver)
        self.scroll_down(0, 800)
        time.sleep(5)
        obj.add_lesson().click()
        time.sleep(2)
        obj.enter_lesson_name().send_keys("API Testing")
        self.scroll_down(0, 500)
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys("I want the deep knowledge for API Testing.")
        time.sleep(2)
        obj.enter_prompt_for_lesson().send_keys(Keys.ENTER)
        time.sleep(40)
        obj.scroller().click()
        time.sleep(2)
        self.lesson_right_arrow().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        time.sleep(2)
        self.lesson_proceed_button().click()
        print("Successfully added the API Testing Lesson.")
        # self.back_to_course().click()
        time.sleep(2)

    """ Add assignment """

    # @pytest.mark.skip
    def test_add_assignment1(self):
        obj = Paths(self.driver)
        # self.all_page()
        # time.sleep(1)
        self.scroll_up(0, -500)
        time.sleep(10)
        self.add_new_assignment().click()
        self.pop_up_assignment().click()
        time.sleep(2)
        self.scroll_down(0, 500)
        self.assignment_name().send_keys("MCQ")
        time.sleep(5)
        self.assignment_timer_add().click()
        time.sleep(2)
        self.assignment_type_dropdown().send_keys(Keys.ENTER)
        time.sleep(2)
        self.mcq().click()
        time.sleep(2)
        self.input_assignment_prompt().send_keys(". give me the 10 questions")
        self.assignment_create_button().click()
        time.sleep(45)
        obj.scroller().click()
        time.sleep(5)
        self.assignment_right_arrow_1().click()
        time.sleep(5)
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        time.sleep(10)
        print("Successfully added MCQ assignment.")
        self.back_to_course().click()

    """ Edit the Assignment """

    # @pytest.mark.skip
    def test_edit_assignment1(self):
        obj = Paths(self.driver)
        time.sleep(2)
        self.open_all_assignments().click()
        time.sleep(2)
        self.edit_assignment1().click()
        time.sleep(5)
        self.scroll_up(0, -700)
        time.sleep(5)
        self.add_new_assignment_1().click()
        time.sleep(2)
        self.select_assignment1().click()
        self.scroll_down(0, 800)
        time.sleep(5)
        obj.edit_assignment().send_keys("Thank You")
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully Edited MCQ assignment.")
        self.back_to_course().click()

    """ Delete the assignment """

    # @pytest.mark.skip
    def test_delete_assignment1(self):
        obj = Paths(self.driver)
        time.sleep(10)
        obj.delete_select_assignment().click()
        time.sleep(2)
        obj.delete_assignment().click()
        print("Deleted the MCQ assignment.")
        # obj.confirm_delete_assignment().click()
        self.back_to_lesson().click()
        time.sleep(2)

    """ Edit the lesson """

    # @pytest.mark.skip
    def test_edit_lesson1(self):
        obj = Paths(self.driver)
        self.preview_lesson().click()
        time.sleep(2)
        self.write_lesson().send_keys(" Thank You")
        self.scroll_down(0, 700)
        time.sleep(2)
        self.assignment_save_button().click()
        print("Successfully Edited the API Testing lesson.")
        self.back_to_course().click()
        time.sleep(2)

    """ Delete the lesson """

    # @pytest.mark.skip
    def test_delete_lesson1(self):
        obj = Paths(self.driver)
        self.delete_lesson_option().click()
        self.delete_to_lesson().click()
        obj.confirm_delete_assignment().click()
        print("Successfully deleted the API Testing lesson")
        time.sleep(2)

    """ Edit the course """

    # @pytest.mark.skip
    def test_edit_course1(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -900)
        time.sleep(5)
        self.edit_to_course().click()
        time.sleep(20)
        self.edit_to_description().click()
        time.sleep(40)
        self.edit_to_update_course().click()
        print("Successfully edited the course.")
        time.sleep(5)

    """ Delete the course """

    # @pytest.mark.skip
    def test_delete_course1(self):
        obj = Paths(self.driver)
        self.scroll_up(0, -900)
        time.sleep(5)
        self.back_to_dashboard().click()
        time.sleep(2)
        self.delete_option_course().click()
        self.delete_to_course().click()
        obj.confirm_delete_assignment().click()
        print("Successfully Deleted the API Testing Course.")
        time.sleep(20)
