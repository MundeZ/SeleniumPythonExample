import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.GuidesModule.PageGuides.guides_page import GuidesPage


@pytest.mark.usefixtures("setup")
class TestNewComersMenu:
    driver: WebDriver

    def setup_method(self):
        self.main_page = "https://worldoftanks.com/en/content/guide/"

    @allure.title("test link in button")
    @pytest.mark.dependency()  # if need can add dependency
    def test_newcomers_guide_href(self):
        page = GuidesPage(self.driver)
        self.driver.get(self.main_page)
        actual_result = page.newcomers_guide().get_attribute("href")
        expected_result = "https://worldoftanks.com/en/content/guide/newcomers-guide/"
        assert actual_result == expected_result

    @allure.title("test title after redirect")
    @pytest.mark.dependency(depends=["TestNewComersMenu::test_newcomers_guide_href"])
    def test_newcomers_guide_title(self):
        page = GuidesPage(self.driver)
        self.driver.get(self.main_page)
        page.newcomers_guide().click()
        assert self.driver.title == "World of Tanks Newcomers Guide"

    @allure.title("test text in button")
    def test_newcomers_text(self):
        page = GuidesPage(self.driver)
        self.driver.get(self.main_page)
        actual_result = page.newcomers_guide().text
        assert actual_result == "  NEWCOMER’S GUIDE"

    @allure.title("test for fail")
    def test_failure(self):
        page = GuidesPage(self.driver)
        self.driver.get(self.main_page)
        page.newcomers_guide().click()
        assert self.driver.title == "fail"
