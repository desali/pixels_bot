import sys
import time

from app.core.settings import USER
from app.logic.bot import Bot
from app.logic.browser import Browser
from app.logic.tkinter import request_and_set_coordinates, can_i_continue, get_chrome_version_and_selenium_port

selenium_port, chrome_version = get_chrome_version_and_selenium_port()
selenium_address = f"127.0.0.1:{selenium_port}"
chrome_driver_path = f"C:\\Users\\{USER}\\AppData\\Roaming\\adspower_global\\cwd_global\\chrome_{chrome_version}\\chromedriver.exe"
browser = Browser(None, chrome_driver_path, selenium_address)
bot = Bot(browser)

# Wait 3 seconds ...
time.sleep(3)

# Configure screen size
request_and_set_coordinates()

# Main menu page
bot.open_main_menu()

can_continue = can_i_continue('Убедись что я нахожусь внутри магазина...')
if not can_continue:
    sys.exit()

# Calculate need seeds
seed_title, seed_count = bot.planter_calculate_need_seeds()
print()
print(seed_title, seed_count)

if seed_count == 0:
    sys.exit()

# Buy seeds
bot.planter_buy_seeds(seed_title, seed_count)

# Plant seeds
farms = bot.planter_plant_in_farms(seed_count)
