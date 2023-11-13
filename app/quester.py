import sys
import time

from app.core.settings import USER
from logic.bot import Bot
from logic.browser import Browser
from logic.tkinter import request_and_set_coordinates, can_i_continue, get_chrome_version_and_selenium_port

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
# bot.open_main_menu()

can_continue = can_i_continue('Выбери сервер и запусти...')
if not can_continue:
    sys.exit()

# Main menu page (start game)
# bot.main_menu_start_game()

# Terms and conditions accept
bot.terms_of_service_accept()

# Barney
bot.barney_quest()

# Danger Dale
bot.danger_dale_quest()

# Buck Galore
bot.buck_galore_quest()

# Lumber Jill
bot.lumber_jill_quest()

# Sticks Planks
bot.sticks_planks_quest()

# Karen Cooking
bot.karen_cooking_quest()

# Return to Buck Galore
bot.return_to_back_galore()
