from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class PageBase:
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=30, poll_frequency=1.5)

    def find_visible_element(self, xpath: str):
        try:
            obj = self.wait.until(ec.element_to_be_clickable((By.XPATH, xpath)) and
                                  ec.visibility_of_element_located((By.XPATH, xpath)))
            return obj
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def find_visible_elements(self, xpath: str):
        try:
            elements = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, xpath)))
            visible_elements = [element for element in elements if element.is_displayed()]
            clickable_elements = [element for element in visible_elements if element.is_enabled()]
            return clickable_elements
        except NoSuchElementException as e:
            print(f"Elements not found: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            raise e
