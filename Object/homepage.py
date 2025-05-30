from selenium.webdriver.common.by import By


class Paths:

    def __init__(self, driver):
        self.driver = driver

    # SignUp Paths

    click_button = (By.XPATH, "//a[normalize-space()='Login']")
    click_signup = (By.XPATH, "//a[normalize-space()='Sign up']")
    click_role_option = (By.XPATH, "//div[@id='role-select']")
    click_teacher_option_role = (By.XPATH, "//li[normalize-space()='I am a Teacher']")
    click_student_option_role = (By.XPATH, "//li[normalize-space()='I am a Student']")
    click_signup_option = (By.XPATH, "//p[normalize-space()='Sign Up with Verification Code']")
    click_enter_email = (By.XPATH, "//input[@name='email']")
    click_error_message = (By.XPATH, "//div[@class='signup-input edit-email']/div/p")
    click_code = (By.XPATH, "//button[normalize-space()='Send Code']")
    click_enter_code = (By.XPATH, "//div[@label='6-Digit Code']/div/div/input")
    otp_confirmation = (By.XPATH, "//button[normalize-space()='Sign Up']")

    # Login Paths

    click_login_verification_code = (By.XPATH, "//p[normalize-space()='Login with Verification Code']")
    click_login_button = (By.XPATH, "//button[normalize-space()='Login']")

    # create teacher profile

    setup_teacher_profile = (By.XPATH, "//button[normalize-space()='Setup Profile']")
    setup_title = (By.XPATH, "//div[4]//div[2]//div[1]//div[1]//div[1]//div[2]//select[1]")
    setup_title_dropdown = (By.XPATH, "//select[@name='title']")
    setup_name = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
                            "/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/input[1]")
    setup_select_calendar = (By.XPATH, "//div[4]//div[2]//div[1]//div[3]//input[1]")
    setup_click_calendar = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                      "1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/table["
                                      "1]/tbody[1]/tr[1]/td[1]")
    setup_gender_dropdown = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                       "1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/select[1]")
    setup_select_location = (By.XPATH, "//div[4]//div[2]//div[1]//div[5]//input[1]")
    setup_select_location_dropdown = (By.XPATH, "//div[@class='pac-item']")
    setup_select_linkedin = (By.XPATH, "//div[4]//div[2]//div[1]//div[6]//input[1]")
    setup_select_language = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                       "1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/a[1]")

    # Teacher about
    setup_teacher_about = (By.XPATH, "((//textarea[contains(@class,'introduce-yourself-text')]))[1]")

    # Subject You Teach
    enter_subject_name = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                    "1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/input[1]")
    select_subject_dropdown = (By.XPATH, "//div[4]//div[2]//div[3]//div[1]//a[1]")
    click_add_button = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[4]")

    # Personalize_your_ai_assistant
    enter_ai_name = (By.XPATH, "((//input[contains(@name,'ai_name')]))[1]")
    select_ai_tone = (By.XPATH, "(//input[@placeholder='Select response'])[4]")
    select_ai_tone_checkbox = (By.XPATH, "(//label[@for='0'][normalize-space()='Formal'])[4]")
    select_ai_msg = (By.XPATH, "(//input[@placeholder='E.g. Hi! This is Ms. Synthia’s assistant, how may I help "
                               "you?'])[4]")
    select_ai_msg_checkbox = (By.XPATH, "(//input[@name='options'])[13]")
    click_add_image_button = (By.XPATH, "(//input[@type='file'])[4]")
    click_save_image_button = (By.XPATH, "//a[@class='save_btn']")
    click_image_dragger = (By.XPATH, "//span[@class='cropper-face cropper-move']")
    click_profile_button = (By.XPATH, "//div[4]//div[3]//button[2]")

    # create a course

    course_create_button = (By.XPATH, "//button[normalize-space()='Create Course']")
    course_enter_name = (By.XPATH, "//input[@name='name']")
    course_error_name = (By.XPATH,
                         "//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium "
                         "MuiFormHelperText-contained css-v7esy']")
    course_select_subject_dropdown = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium "
                                                "css-vubbuv'])[1]")

    course_enter_subject_name = (By.XPATH, "//input[@placeholder='E.g. Math, science, geography']")
    course_subject_submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    course_subject_list = (By.XPATH, "//ul[@role='listbox']/li")
    course_selected_subject = (By.XPATH, "//li[@id='subjects-autocomplete-option-2']")
    course_back_button = (By.XPATH, "//button[normalize-space()='Back']")
    course_next_button = (By.XPATH, "//button[normalize-space()='Submit']")
    course_start_std_dropdown = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium "
                                           "css-vubbuv'])[2]")
    course_start_std_list = (By.XPATH, "//ul[@id='from-grade-autocomplete-listbox']/li")
    course_end_std_dropdown = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium "
                                         "css-vubbuv'])[3]")
    course_end_std_list = (By.XPATH, "//ul[@id='to-grade-autocomplete-listbox']/li")
    course_select_calendar = (By.XPATH, "//div[4]//div[1]//div[1]//div[1]//div[1]//button[1]//*[name()='svg']")
    course_select_end_calendar = (By.XPATH, "//div[5]//div[1]//div[1]//div[1]//div[1]//button[1]")
    course_select_current_date = (By.XPATH, "//div[@role='rowgroup']/div/button")
    course_select_end_date = (By.XPATH, "//button[normalize-space()='28']")
    course_enhance_description = (By.XPATH, "//button[@class='Course-description-inner-ai-feilds']")
    course_generate_image = (By.XPATH, "//div[@class='Create-Course-uisng-ai']")
    course_regenerate_image = (By.XPATH, "//button[normalize-space()='Regenerate']")
    course_upload_image = (By.XPATH, "//label/input[@type='file']")
    course_final_button = (By.XPATH, "//div[@class='create-course-enhance-course-folder']//button["
                                     "@type='submit'][normalize-space()='Create Course']")

    # Edit Course
    course_edit_button = (By.XPATH, "//button[@class='view-course-details-edit-and-share-folder']")
    course_edit_course_name = (By.XPATH, "//input[@name='name']")
    course_edit_level_start_dropdown = (By.XPATH,
                                        "(//body[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")
    course_edit_level_start_list = (By.XPATH, "//li[normalize-space()='Grade 2']")
    course_edit_level_end_dropdown = (By.XPATH,
                                      "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
    course_edit_level_end_list = (By.XPATH, "//li[normalize-space()='Corporate']")
    course_edit_submit = (By.XPATH, "(//button[normalize-space()='Update and Publish'])[1]")

    # Add Lesson
    lesson_new_add = (By.XPATH, "//button[normalize-space()='Create Lesson']")
    lesson_new_lesson_name = (By.XPATH, "//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root "
                                        "custom-text-field css-feqhe6']/div/input")
    lesson_enter_prompt = (By.XPATH, "//div[@class='promote_part_sec']/div/div/textarea[@name='chat_query']")

    # Add Assignment
    assignment_type_list = (By.XPATH, "//div[@role='presentation']/div/ul")
    assignment_generator_left_body = (By.XPATH, "//div[@class='lesson_generator_body_sec_left_body']")

    # Edit assignment

    # edit_assignment1 = (By.XPATH, "//div[@class='editor-input']/h3")
    edit_assignment1 = (By.XPATH, "// div[ @ role = 'textbox']")

    # Delete assignment

    select_assignment = (By.XPATH, "(//div[@class='assignments_count_details'])[1]")
    delete_assignment1 = (By.XPATH, "(//i[@class='fa-solid fa-trash'])[1]")
    delete_confirm = (By.XPATH, "//button[normalize-space()='Delete']")

    # Schoology

    open_schoology = (By.XPATH, "//div[@class='dashborad-Courses-container']//div[5]//div[2]")
    refresh_schoology_btn = (By.XPATH, "//button[normalize-space()='Refresh Course']")
    all_select_schoology = (By.XPATH, "//input[@id='select-all']")
    next_schoology = (By.XPATH, "//button[normalize-space()='Next']")
    start_sync_schoology = (By.XPATH, "//button[normalize-space()='Start Sync']")
    confirm_schoology = (By.XPATH, "//div[@class='Conformatio-popup-btn']/button[1]")


    # open the course

    open_course = (By.XPATH, "//div[@class='created-my-courses-container']//div[1]//div[2]//button[1]")
    open_assignment = (By.XPATH, "(//button[@type='button'][normalize-space()='Edit Lesson'])[2]")
    scroll_generator = (By.XPATH, "//button[@class='scroll-to-bottom-btn']")
    # sign up functions

    def open_previous_course(self):
        return self.driver.find_element(*Paths.open_course)

    def open_previous_assignment(self):
        return self.driver.find_element(*Paths.open_assignment)

    def scroller(self):
        return self.driver.find_element(*Paths.scroll_generator)

    def start_button(self):
        return self.driver.find_element(*Paths.click_button)

    def signup_button(self):
        return self.driver.find_element(*Paths.click_signup)

    def role_option(self):
        return self.driver.find_element(*Paths.click_role_option)

    def select_teacher_role(self):
        return self.driver.find_element(*Paths.click_teacher_option_role)

    def select_student_role(self):
        return self.driver.find_element(*Paths.click_student_option_role)

    def select_signup_option(self):
        return self.driver.find_element(*Paths.click_signup_option)

    def enter_email(self):
        return self.driver.find_element(*Paths.click_enter_email)

    def show_validation_message(self):
        return self.driver.find_element(*Paths.click_error_message)

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

    # setup teacher profile

    def create_teacher_profile(self):
        return self.driver.find_element(*Paths.setup_teacher_profile)

    def set_title(self):
        return self.driver.find_element(*Paths.setup_title)

    def select_setup_title(self):
        return self.driver.find_element(*Paths.setup_title)

    def select_title_dropdown(self):
        return self.driver.find_element(*Paths.setup_title_dropdown)

    def setup_enter_name(self):
        return self.driver.find_element(*Paths.setup_name)

    def select_calendar(self):
        return self.driver.find_element(*Paths.setup_select_calendar)

    def select_date(self):
        return self.driver.find_element(*Paths.setup_click_calendar)

    def select_gender(self):
        return self.driver.find_element(*Paths.setup_gender_dropdown)

    def select_location(self):
        return self.driver.find_element(*Paths.setup_select_location)

    def location_dropdown(self):
        return self.driver.find_element(*Paths.setup_select_location_dropdown)

    def enter_linkedin_url(self):
        return self.driver.find_element(*Paths.setup_select_linkedin)

    def select_language(self):
        return self.driver.find_element(*Paths.setup_select_language)

    def write_teacher_about(self):
        return self.driver.find_element(*Paths.setup_teacher_about)

    def subject_name(self):
        return self.driver.find_element(*Paths.enter_subject_name)

    def select_subject(self):
        return self.driver.find_element(*Paths.select_subject_dropdown)

    def subject_add(self):
        return self.driver.find_element(*Paths.click_add_button)

    def ai_name(self):
        return self.driver.find_element(*Paths.enter_ai_name)

    def ai_tone(self):
        return self.driver.find_element(*Paths.select_ai_tone)

    def ai_tone_checkbox(self):
        return self.driver.find_element(*Paths.select_ai_tone_checkbox)

    def ai_msg(self):
        return self.driver.find_element(*Paths.select_ai_msg)

    def ai_msg_checkbox(self):
        return self.driver.find_element(*Paths.select_ai_msg_checkbox)

    def add_teacher_image(self):
        return self.driver.find_element(*Paths.click_add_image_button)

    def save_image(self):
        return self.driver.find_element(*Paths.click_save_image_button)

    def image_drag(self):
        return self.driver.find_element(*Paths.click_image_dragger)

    def profile_submit(self):
        return self.driver.find_element(*Paths.click_profile_button)

    # Create course

    def create_course(self):
        return self.driver.find_element(*Paths.course_create_button)

    def course_name(self):
        return self.driver.find_element(*Paths.course_enter_name)

    def error_msg_course_name(self):
        return self.driver.find_element(*Paths.course_error_name)

    def select_course_subject_dropdown(self):
        return self.driver.find_element(*Paths.course_select_subject_dropdown)

    def select_course_subject_list(self):
        return self.driver.find_elements(*Paths.course_subject_list)

    def enter_add_subject_name(self):
        return self.driver.find_element(*Paths.course_enter_subject_name)

    def enter_subject_list(self):
        return self.driver.find_element(*Paths.course_selected_subject)

    def click_back_button(self):
        return self.driver.find_element(*Paths.course_back_button)

    def click_next_button(self):
        return self.driver.find_element(*Paths.course_next_button)

    def click_start_std_dropdown(self):
        return self.driver.find_element(*Paths.course_start_std_dropdown)

    def select_start_std(self):
        return self.driver.find_elements(*Paths.course_start_std_list)

    def click_end_std_dropdown(self):
        return self.driver.find_element(*Paths.course_end_std_dropdown)

    def select_end_std(self):
        return self.driver.find_elements(*Paths.course_end_std_list)

    def click_select_calendar(self):
        return self.driver.find_element(*Paths.course_select_calendar)

    def select_current_date(self):
        return self.driver.find_elements(*Paths.course_select_current_date)

    def click_select_end_calendar(self):
        return self.driver.find_element(*Paths.course_select_end_calendar)

    def click_select_end_date(self):
        return self.driver.find_element(*Paths.course_select_end_date)

    def enhanced_course_description(self):
        return self.driver.find_element(*Paths.course_enhance_description)

    def generate_image(self):
        return self.driver.find_element(*Paths.course_generate_image)

    def regenerate_image(self):
        return self.driver.find_element(*Paths.course_regenerate_image)

    def upload_image(self):
        return self.driver.find_element(*Paths.course_upload_image)

    def click_subject_submit_button(self):
        return self.driver.find_element(*Paths.course_subject_submit_button)

    def complete_course_button(self):
        return self.driver.find_element(*Paths.course_final_button)

    # Edit Course

    def edit_button(self):
        return self.driver.find_element(*Paths.course_edit_button)

    def edit_course_name(self):
        return self.driver.find_element(*Paths.course_edit_course_name)

    def edit_level_start_dropdown(self):
        return self.driver.find_element(*Paths.course_edit_level_start_dropdown)

    def edit_level_start_list(self):
        return self.driver.find_elements(*Paths.course_edit_level_start_list)

    def edit_level_end_dropdown(self):
        return self.driver.find_element(*Paths.course_edit_level_end_dropdown)

    def edit_level_end_list(self):
        return self.driver.find_elements(*Paths.course_edit_level_end_list)

    def edit_submit_btn(self):
        return self.driver.find_element(*Paths.course_edit_submit)

    # Add Lesson

    def add_lesson(self):
        return self.driver.find_element(*Paths.lesson_new_add)

    def enter_lesson_name(self):
        return self.driver.find_element(*Paths.lesson_new_lesson_name)

    def enter_prompt_for_lesson(self):
        return self.driver.find_element(*Paths.lesson_enter_prompt)

    def assignment_list(self):
        return self.driver.find_elements(*Paths.assignment_type_list)

    def generator_left_body(self):
        return self.driver.find_element(*Paths.assignment_generator_left_body)

    # Edit assignment

    def edit_assignment(self):
        return self.driver.find_element(*Paths.edit_assignment1)

    # Delete assignment

    def delete_select_assignment(self):
        return self.driver.find_element(*Paths.select_assignment)

    def delete_assignment(self):
        return self.driver.find_element(*Paths.delete_assignment1)

    def confirm_delete_assignment(self):
        return self.driver.find_element(*Paths.delete_confirm)

    # Schoology

    def open_schoology_courses(self):
        return self.driver.find_element(*Paths.open_schoology)

    def refresh_schoology(self):
        return self.driver.find_element(*Paths.refresh_schoology_btn)

    def select_all_schoology(self):
        return self.driver.find_element(*Paths.all_select_schoology)

    def next_btn_schoology(self):
        return self.driver.find_element(*Paths.next_schoology)

    def start_sync_schoology_btn(self):
        return self.driver.find_element(*Paths.start_sync_schoology)

    def confirm_schoology_sync(self):
        return self.driver.find_element(*Paths.confirm_schoology)

