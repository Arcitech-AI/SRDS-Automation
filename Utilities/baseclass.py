import inspect
import logging
import os
import pytest
import tensorflow as tf

from selenium.webdriver.common.by import By


# from Production.currentdate import get_current_date


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
