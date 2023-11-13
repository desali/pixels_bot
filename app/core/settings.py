import os

from dotenv import load_dotenv

load_dotenv()

# ADS
ADS_URL = "http://local.adspower.net:50325"
ADS_API = "api/v1"
ADS_BROWSER_START_URL = "browser/start"

# PIXELS
PIXELS_MAIN_URL = "https://play.pixels.xyz/"

# SCREEN SIZE
SCREEN_TL_X = 0
SCREEN_TL_Y = 0
SCREEN_BR_X = 0
SCREEN_BR_Y = 0

DEVICE_NAME = ""

USER = os.getenv('USER')

devices = {
    "Выберите": (),
    "Первый ноут из 2 мониторов": (-2560, 0, -960, 1000),
    "Ноут отдельно": (0, 0, 2560, 1600),
    "Ноут Yerkebulan": (0, 0, 1920, 1080),
}


def set_screen_size(device_name, tl_x, tl_y, br_x, br_y):
    global SCREEN_TL_X, SCREEN_TL_Y, SCREEN_BR_X, SCREEN_BR_Y, DEVICE_NAME
    DEVICE_NAME = device_name

    SCREEN_TL_X = tl_x
    SCREEN_TL_Y = tl_y
    SCREEN_BR_X = br_x
    SCREEN_BR_Y = br_y


def get_screen_size():
    global SCREEN_TL_X, SCREEN_TL_Y, SCREEN_BR_X, SCREEN_BR_Y

    return SCREEN_TL_X, SCREEN_TL_Y, SCREEN_BR_X, SCREEN_BR_Y


def get_device_name():
    global DEVICE_NAME

    return DEVICE_NAME
