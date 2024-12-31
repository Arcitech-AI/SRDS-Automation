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
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj, options=options)
    # env = request.config.getoption('--env', default='validation')
    # urls = {
    #     'validation': 'https://mycro.news/',
    #     'production': 'https://proschool.ai/'
    # }
    # return urls.get(env, urls['validation'])
    time.sleep(5)
    driver.get("https://qat.srds.ai/")
    driver.implicitly_wait(50)
    driver.maximize_window()
    time.sleep(1)
    # driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    driver.refresh()
    yield
    driver.quit()


@pytest.mark.skip
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
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


@pytest.mark.skip
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
