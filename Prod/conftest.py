import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="class")
def Invoke_Browser(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-application-cache")
    options.add_argument("--incognito")
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj, options=options)
    time.sleep(5)
    driver.get("https://qat.srds.ai/")
    driver.implicitly_wait(50)
    driver.maximize_window()
    time.sleep(1)
    # driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    # driver.refresh()
    yield
    driver.quit()


"""For getlogger"""


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


"""For screenshot"""


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
#
# driver = None
#
#
# @pytest.fixture(scope="class")
# def Invoke_Browser(request, browser="chrome"):  # Add browser parameter with default value
#     global driver
#
#     if browser.lower() == "chrome":
#         options = ChromeOptions()
#         options.add_experimental_option("detach", True)
#         options.add_argument('ignore-certificate-errors')
#         options.add_argument("--disable-application-cache")
#         options.add_argument("--incognito")
#         service_obj = ChromeService()
#         driver = webdriver.Chrome(service=service_obj, options=options)
#
#     elif browser.lower() == "firefox":
#         options = FirefoxOptions()
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--private')
#         service_obj = FirefoxService()
#         driver = webdriver.Firefox(service=service_obj, options=options)
#
#     elif browser.lower() == "edge":
#         options = EdgeOptions()
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--inprivate')
#         service_obj = EdgeService()
#         driver = webdriver.Edge(service=service_obj, options=options)
#
#     else:
#         raise ValueError(f"Browser {browser} is not supported")
#
#     driver.implicitly_wait(50)
#     driver.get("https://qat.srds.ai/")
#     driver.maximize_window()
#     request.cls.driver = driver
#     driver.refresh()
#
#     yield
#     driver.quit()
