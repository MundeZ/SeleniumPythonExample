import allure
from base.page_base import PageBase
from tests.GuidesModule.PageGuides.locators import *


class GuidesPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("newcomers guide button")
    def newcomers_guide(self):
        return self.find_visible_element(NewcomersMenu.newcomers_guide)

    @allure.step("")
    def button_one(self):
        pass

    @allure.step("")
    def button_two(self):
        pass
