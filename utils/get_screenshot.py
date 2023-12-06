import allure
from allure_commons.types import AttachmentType
from base.page_base import PageBase


class GetScreenshot(PageBase):
    def get_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)
