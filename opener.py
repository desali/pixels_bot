from app.logic.bot import Bot
from app.logic.browser import Browser
from app.logic.tkinter import get_ads_profile_id

profile_id = get_ads_profile_id()

browser = Browser(profile_id, None, None)
