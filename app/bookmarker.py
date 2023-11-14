import sys
import time

from app.core.settings import USER
from logic.bot import Bot
from logic.browser import Browser
from logic.tkinter import request_and_set_coordinates, can_i_continue, get_chrome_version_and_selenium_port

# selenium_port, chrome_version = get_chrome_version_and_selenium_port()
selenium_port, chrome_version = 58802, 118
# 57853:116
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

can_continue = can_i_continue('Убедись что я нахожусь внутри магазина, и очисти все закладки...')
if not can_continue:
    sys.exit()

farm_1000 = 1000
farm_2123 = 2123
farm_4717 = 4717

bot.bookmarker_walk_from_in_bg_to_farms()
bot.bookmarker_farms_visit_farm(farm_1000)
bot.bookmarker_bookmark_farm(farm_1000)
bot.bookmarker_go_from_farm_to_sauna(farm_1000)

bot.bookmarker_walk_from_in_sauna_to_farms()
bot.bookmarker_farms_visit_farm(farm_2123)
bot.bookmarker_bookmark_farm(farm_2123)
bot.bookmarker_go_from_farm_to_sauna(farm_2123)

bot.bookmarker_walk_from_in_sauna_to_farms()
bot.bookmarker_farms_visit_farm(farm_4717)
bot.bookmarker_bookmark_farm(farm_4717)
bot.bookmarker_go_from_farm_to_sauna(farm_4717)
bot.bookmarker_walk_from_in_sauna_to_buck_galore()
