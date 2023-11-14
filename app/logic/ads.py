import requests

from app.core import settings as S


class AdsService:

    def __init__(self):
        pass

    def start_browser(self, ads_id):
        start_url = f"{S.ADS_URL}/{S.ADS_API}/{S.ADS_BROWSER_START_URL}?user_id={ads_id}&open_tabs=1&ip_tab=0"
        response = requests.get(start_url)

        response_json = response.json()
        if response_json["code"] != 0:
            return None, None, response_json["msg"]

        chrome_driver_path = response_json["data"]["webdriver"]
        selenium_address = response_json["data"]["ws"]["selenium"]

        return chrome_driver_path, selenium_address, None
