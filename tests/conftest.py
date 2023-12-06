import pytest
import os
from selenium.webdriver.chrome.options import Options as Option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.file_detector import LocalFileDetector
from utils.get_screenshot import GetScreenshot


@pytest.fixture
def get_chrome_options():
    options = Option()
    options.add_argument('chrome')  # Use headless if you do not need UI.If you need use chrome
    options.add_argument('--window-size=1920,1080')  # --start-maximized or --window-size=1300,900
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-cache")
    options.add_argument("--profile-directory=Default")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    script_directory = os.path.dirname(os.path.abspath(__file__))
    chrome_driver_path = os.path.join(script_directory, "chromedriver")
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(options=options, service=service)  # for local setup
    # this can be added code for remote setup
    driver.file_detector = LocalFileDetector()
    return driver


@pytest.fixture(scope='function')  # browser will be open every time after test
def setup(request, get_webdriver):
    driver = get_webdriver
    driver.set_page_load_timeout(60)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    get_screenshot = GetScreenshot(driver)
    get_screenshot.get_screenshot()
    driver.quit()
