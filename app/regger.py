import sys
import time

from logic.bot import Bot
from logic.browser import Browser
from logic.tkinter import request_and_set_coordinates, can_i_continue, get_chrome_version_and_selenium_port

selenium_port, chrome_version = get_chrome_version_and_selenium_port()

selenium_address = f"127.0.0.1:{selenium_port}"
chrome_driver_path = f"C:\\Users\\Desspex\\AppData\\Roaming\\adspower_global\\cwd_global\\chrome_{chrome_version}\\chromedriver.exe"
browser = Browser(None, chrome_driver_path, selenium_address)
bot = Bot(browser)

# Wait 3 seconds ...
time.sleep(3)

# Configure screen size
request_and_set_coordinates()

# Main menu page
bot.open_main_menu()

can_continue = can_i_continue('Убедись что экран браузер стоит в нужном месте и что он полноэкранный(F11)...')
if not can_continue:
    sys.exit()

# Main menu connect the ronin
bot.main_menu_connect_ronin()

# Create New Account
bot.create_new_account()
