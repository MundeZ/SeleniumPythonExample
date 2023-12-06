import json
import allure
from allure_commons.types import AttachmentType


def check_status_code(logs, browser):
    for i in get_status_codes(logs):
        if i > 399:
            print("Status on page: ", i)
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True


def get_status_codes(logs):
    statuses = []
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            if d['message'].get('method') == "Network.responseReceived":
                statuses.append(d['message']['params']['response']['status'])
    return statuses


def get_status_code(logs):
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            try:
                content_type = 'text/html' in d['message']['params']['response']['headers']['content-type']
                response_received = d['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    return d['message']['params']['response']['status']
            except:
                pass
