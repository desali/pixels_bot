import pyautogui
from app.logic.utils import sleep_randomly, sleep_exact
import time


def press_key(key):
    pyautogui.press(key)


def hold_mouse_for_time(x, y, seconds):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(seconds)
    pyautogui.mouseUp()


def move_to_coordinates_and_click(x, y, secs=1):
    pyautogui.moveTo(x, y)
    pyautogui.click()

    sleep_exact(secs)


def window_is_active(title="pixels: an infinite"):
    windows = pyautogui.getWindowsWithTitle(title)
    if not windows:
        return False

    return windows[0].isActive
