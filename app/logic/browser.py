import sys
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.logic.ads import AdsService


class Browser:
    D = None
    selenium_address = ""
    chrome_driver_path = ""

    def __init__(self, profile_id, chrome_driver_path, selenium_address):
        if profile_id is not None:
            ads_service = AdsService()

            chrome_driver_path, selenium_address, err_message = ads_service.start_browser(profile_id)
            if err_message is not None:
                print(err_message)
                sys.exit()
            self.chrome_driver_path = chrome_driver_path
            self.selenium_address = selenium_address
            self.save_selenium_creds()

        chrome_options = Options()
        chrome_options.debugger_address = selenium_address
        chrom_driver_service = Service(chrome_driver_path)
        self.D = webdriver.Chrome(service=chrom_driver_service, options=chrome_options)

    def save_selenium_creds(self):
        port = self.selenium_address.split(":")[1]
        version = self.chrome_driver_path.rsplit("\\", 2)[1].split("_")[1]
        port_version = f"{port}:{version}"
        pyperclip.copy(port_version)

    def send_keys_to_element(self, path, key):
        self.D.find_element(By.XPATH, path).send_keys(key)

    def press_key(self, key):
        actions = ActionChains(self.D)
        actions.send_keys(key)
        actions.perform()

    def click_element_class_starts(self, tag, class_name, secs=1):
        element = self.D.find_element(By.XPATH, f"//{tag}[starts-with(@class, '{class_name}')]")
        self.click_element(element, secs)

    def click_element_class_contains(self, tag, class_name, secs=1):
        element = self.D.find_element(By.XPATH, f"//{tag}[contains(@class, '{class_name}')]")
        self.click_element(element, secs)

    def click_element(self, element, secs=1):
        element.click()
        time.sleep(secs)

    def wait_presence_located(self, by, value, secs=120) -> Exception:
        try:
            WebDriverWait(self.D, secs).until(
                EC.presence_of_element_located((by, value))
            )
            return None
        except Exception as e:
            return e

    def get_element(self, by, value):
        return self.D.find_element(by, value)

    def get_elements(self, tag, class_name):
        return self.D.find_elements(By.XPATH, f"//{tag}[starts-with(@class, '{class_name}')]")

    def get_elements_universal(self, by, value):
        return self.D.find_elements(by, value)

    def hold_key_for_time(self, key, seconds):
        actions = ActionChains(self.D)
        actions.key_down(key)
        actions.perform()
        time.sleep(seconds)
        actions.key_up(key)
        actions.perform()
        time.sleep(0.05)

    def hold_keys_for_time(self, key_1, key_2, seconds):
        actions = ActionChains(self.D)
        actions.key_down(key_1)
        actions.key_down(key_2)
        actions.perform()
        time.sleep(seconds)
        actions.key_up(key_1)
        actions.key_up(key_2)
        actions.perform()
        time.sleep(0.05)

    def wait_for_opacity(self, tag, class_name, opacity, timeout=60):
        def _check_opacity(driver):
            element = driver.find_element(By.XPATH, f"//{tag}[starts-with(@class, '{class_name}')]")
            return element.value_of_css_property('opacity') == str(opacity)

        return WebDriverWait(self.D, timeout).until(_check_opacity)

    def focus(self):
        self.D.execute_script("window.focus();")
