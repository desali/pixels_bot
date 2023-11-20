import sys
import time

from app.core.constants import SIDES, LeftSide, RightSide, LDirections, RDirections
from app.logic.bot import Bot
from app.logic.browser import Browser
from app.logic.tkinter import get_ads_profile_id, left_right_checker

# Указать Id аккаунта в Ads Power
profile_id = get_ads_profile_id()

browser = Browser(profile_id, None, None)
bot = Bot(browser)

# Открыть главное меню
bot.open_main_menu()

side, countdown = left_right_checker('Проверка', 'Зайди на нужный сервер, left-right локацию, и помести меня в центре нужной стороны и продолжай когда таймер будет 00:00')
if side not in SIDES:
    sys.exit()

# Выбрать направление
side_directions_map = {
    LeftSide: LDirections,
    RightSide: RDirections
}

# Ежеминутный цикл
time.sleep(countdown)
while True:
    bot.left_right_one_minute(side_directions_map[side])
