import time
import pytest
import openai

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Object.homepage import Paths
from Utilities.baseclass import *


class TestAssignmentSubmission(Baseclass):

    def test_open_openai(self, question_text, question_type):
        openai.api_key = "AIzaSyDEmudkyMD8dHCsL3IWfJJnKSDS8TLbMqU"

        if question_type == "MCQ":
            prompt = f"Answer this multiple choice question: {question_text}"
        elif question_type == "FITB":
            prompt = f"Fill in the blanks: {question_text}"
        elif question_type == "TF":
            prompt = f"True or False: {question_text}"
        elif question_type == "Essay":
            prompt = f"Write an essay based on the following question: {question_text}"
        elif question_type == "Short":
            prompt = f"Provide a short answer for the following question: {question_text}"
        elif question_type == "Mixed":
            prompt = f"Answer the following mixed question: {question_text}"
        else:
            prompt = f"Answer the following question: {question_text}"

            # Send the prompt to OpenAI and get the response
        response = openai.Completion.create(
            model="gemini-2.0-flash-exp",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        answer = response.choices[0].text.strip()
        print(f"Answer from ChatGPT: {answer}")
        return answer

    # Existing Teacher Login
    # @pytest.mark.skip
    def test_student_login(self):
        email = "omkarhundre+01@arcitech.ai"
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

    def test_submissions(self):
        obj = Paths(self.driver)
        time.sleep(10)
        obj.click_on_my_courses().click()
        obj.click_active_course().click()
        self.scroll_down(0, 300)
        time.sleep(0.2)
        obj.click_go_to_courses().click()
        time.sleep(30)
        # obj.click_start_lesson().click()
        obj.click_on_the_assignments().click()
        time.sleep(1)
        self.scroll_down(0, 900)
        time.sleep(5)
        obj.click_mcq_assignment().click()
        obj.click_start_assignment().click()

    def test_mcq_submission(self):
        obj = Paths(self.driver)

        while True:

            question_element = obj.mcq_first_question()
            question_text = question_element.text
            print(f"Question extracted: {question_text}")

            generated_answer = self.test_open_openai(question_text, "MCQ")

            mcq_options = obj.mcq_first_question()

            for option in mcq_options:
                if option.text.strip() == generated_answer:
                    option.click()
                    print(f"Selected the correct answer: {generated_answer}")
                    break

            submit_button = obj.get_submit_button()
            submit_button.click()

            time.sleep(2)
            next_button = self.next_question()
            if next_button:
                next_button.click() 
                print("Moved to the next question.")
            else:
                print("No more questions or next button not found.")
                break

        print("All questions processed and submitted successfully.")
