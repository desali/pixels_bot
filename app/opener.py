from logic.bot import Bot
from logic.browser import Browser
from logic.tkinter import get_ads_profile_id

profile_id = get_ads_profile_id()

browser = Browser(profile_id, None, None)
bot = Bot(browser)
