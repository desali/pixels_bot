import random
import sys
import time

import pyautogui as pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from app.core import settings as S
from app.core.constants import DEVICE_LOCATIONS, POPBERRY_SEED_TYPE, BUTTERBERRY_SEED_TYPE, GRAINBOW_SEED_TYPE, \
    SEED_NEED_ENERGY, SEED_NEED_BERRY, LDir, RDir, TDir, BDir, TLDir, TRDir, BLDir, BRDir
from app.core.settings import get_device_name, PIXELS_MAIN_TEXT
from app.core.utils import get_coordinates
from app.logic.pyautogui import move_to_coordinates_and_click, hold_mouse_for_time, press_key, window_is_active, \
    just_click
from app.logic.tkinter import can_i_continue
from app.logic.utils import sleep_randomly, sleep_exact


class Bot:
    browser = None

    def __init__(self, browser):
        self.browser = browser

    def open_main_menu(self):
        if PIXELS_MAIN_TEXT not in self.browser.D.current_url:
            self.browser.D.get(f"{S.PIXELS_MAIN_URL}")

    def wait_location_change(self):
        self.browser.wait_for_opacity("div", "GameContainer_gameCover_", 1)
        self.browser.wait_for_opacity("div", "GameContainer_gameCover_", 0)
        sleep_randomly(1, 3)

    def main_menu_start_game_wait_loading(self):
        err = self.browser.wait_presence_located(By.XPATH, "//button[starts-with(@class, 'commons_pushbutton')]")
        if err is not None:
            print(err)
            sys.exit()

    def main_menu_start_game(self):
        self.main_menu_start_game_wait_loading()
        self.browser.click_element_class_starts("button", "commons_pushbutton")

    def terms_of_service_accept_wait_loading(self):
        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'TermsOfService_')]")
        if err is not None:
            print(err)
            sys.exit()

    def terms_of_service_accept(self):
        self.terms_of_service_accept_wait_loading()
        self.browser.click_element_class_starts("label", "clickable")
        self.browser.click_element_class_starts("button", "commons_pushbutton")

    def dialogue_wait_loading(self):
        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'GameDialog_content_')]")
        if err is not None:
            print(err)
            sys.exit()

    def dialogue_skip(self):
        self.dialogue_wait_loading()

        is_there_skip = False

        buttons = self.browser.get_elements("button", "GameDialog_skip_")
        if len(buttons) > 0:
            is_there_skip = True

        while is_there_skip:
            self.browser.click_element_class_starts("button", "GameDialog_skip_", 0.3)
            buttons = self.browser.get_elements("button", "GameDialog_skip_")
            if len(buttons) == 0:
                is_there_skip = False

    def barney_quest_plant_seed(self):
        sleep_randomly(1, 2)
        # Take poppery_seed
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Plant
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def barney_quest_talk(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def barney_quest_water_seed(self):
        sleep_randomly(1, 2)
        # Take water
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Water
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Take off water
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def barney_quest_fertilize_seed(self):
        sleep_randomly(1, 2)

        # Take fertilizer
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Fertilize
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def barney_quest_cut_seed(self):
        sleep_randomly(1, 2)

        # Take shears
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Cut
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_SEED_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Take off shears
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def barney_quest_eat_seed(self):
        sleep_randomly(1, 2)

        # Take fertilizer
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_THIRD_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_THIRD_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Fertilize
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_MY_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BARNEY_MY_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def barney_quest(self):
        self.dialogue_skip()
        self.barney_quest_plant_seed()
        self.barney_quest_talk()
        self.dialogue_skip()
        self.barney_quest_water_seed()
        self.barney_quest_talk()
        self.dialogue_skip()
        self.barney_quest_fertilize_seed()
        self.barney_quest_talk()
        self.dialogue_skip()
        self.barney_quest_cut_seed()
        self.barney_quest_talk()
        self.dialogue_skip()
        self.barney_quest_eat_seed()
        self.barney_quest_talk()
        self.dialogue_skip()

    def danger_dale_quest_walk_to_dd(self):
        self.browser.hold_key_for_time(Keys.RIGHT, 2.94)

    def danger_dale_quest_talk(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['DANGER_DALE_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['DANGER_DALE_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def danger_dale_quest_go_out_from_dd(self):
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, 2)
        self.browser.hold_key_for_time(Keys.LEFT, 1.25)
        self.browser.hold_key_for_time(Keys.DOWN, 0.5)

    def danger_dale_quest(self):
        self.dialogue_skip()
        self.danger_dale_quest_walk_to_dd()
        self.danger_dale_quest_talk()
        self.dialogue_skip()
        self.danger_dale_quest_go_out_from_dd()

    def walk_from_farm_to_buck_galore(self):
        self.browser.hold_key_for_time(Keys.RIGHT, 2.5)
        self.browser.hold_keys_for_time(Keys.RIGHT, Keys.DOWN, 0.25)
        self.browser.hold_key_for_time(Keys.RIGHT, 2.1)
        self.browser.hold_keys_for_time(Keys.RIGHT, Keys.UP, 0.3)
        self.browser.hold_key_for_time(Keys.RIGHT, 2.8)
        self.browser.hold_keys_for_time(Keys.RIGHT, Keys.DOWN, 0.2)
        self.browser.hold_key_for_time(Keys.RIGHT, 2)
        self.browser.hold_keys_for_time(Keys.RIGHT, Keys.UP, 0.2)
        self.browser.hold_key_for_time(Keys.RIGHT, 1)

    def walk_to_hazel_in_bg(self):
        self.browser.hold_keys_for_time(Keys.RIGHT, Keys.UP, 3)

    def buck_galore_quest_talk(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['HAZEL_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['HAZEL_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def buck_galore_quest_go_out_from_bg(self, secs):
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, secs)

    def buck_galore_quest(self):
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть перед фермой...')
            if not can_continue:
                sys.exit()
        self.walk_from_farm_to_buck_galore()
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть внутри Buck Galore...')
            if not can_continue:
                sys.exit()
        self.walk_to_hazel_in_bg()
        self.buck_galore_quest_talk()
        self.dialogue_skip()
        self.buck_galore_quest_go_out_from_bg(4)

    def image_point_travel(self, image):
        location = pyautogui.locateCenterOnScreen(f"images/{image}.png", confidence=0.8)
        if not location:
            return
        while location:
            x, y = location
            hold_mouse_for_time(x, y, 0.5)

            location = pyautogui.locateCenterOnScreen(f"images/{image}.png", confidence=0.8)

    def walk_from_buck_galore_to_jill(self):
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, 1.15)
        self.browser.hold_key_for_time(Keys.DOWN, 3.7)
        self.browser.hold_key_for_time(Keys.LEFT, 4.2)
        self.browser.hold_key_for_time(Keys.DOWN, 7.2)
        self.browser.hold_key_for_time(Keys.LEFT, 1.8)
        can_continue = can_i_continue('Убедись что персонаж в яме...')
        if not can_continue:
            sys.exit()

    def lumber_jill_quest_talk(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def lumber_jill_quest_axe_woods(self):
        sleep_randomly(1, 2)

        # Take axe
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FOURTH_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FOURTH_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        for i in range(6):
            x_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_WOOD_1_X']
            y_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_WOOD_1_Y']
            x, y = get_coordinates(x_cf, y_cf)
            move_to_coordinates_and_click(x, y)

        for i in range(6):
            x_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_WOOD_2_X']
            y_cf = DEVICE_LOCATIONS[get_device_name()]['LUMBER_JILL_WOOD_2_Y']
            x, y = get_coordinates(x_cf, y_cf)
            move_to_coordinates_and_click(x, y)

        # UnTake axe
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FOURTH_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FOURTH_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def lumber_jill_quest_collect_woods(self):
        self.browser.hold_key_for_time(Keys.UP, 0.4)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.2)
        self.browser.hold_key_for_time(Keys.UP, 0.4)
        self.browser.hold_key_for_time(Keys.LEFT, 0.6)
        self.browser.hold_key_for_time(Keys.DOWN, 0.3)
        self.browser.hold_key_for_time(Keys.LEFT, 0.3)
        self.browser.hold_key_for_time(Keys.UP, 0.2)
        self.browser.hold_key_for_time(Keys.LEFT, 0.3)
        self.browser.hold_key_for_time(Keys.DOWN, 0.2)
        self.browser.hold_key_for_time(Keys.LEFT, 0.5)
        self.browser.hold_key_for_time(Keys.DOWN, 0.6)
        self.browser.hold_key_for_time(Keys.RIGHT, 0.5)
        self.browser.hold_key_for_time(Keys.DOWN, 0.23)
        self.browser.hold_key_for_time(Keys.RIGHT, 0.2)
        can_continue = can_i_continue('Убедись что персонаж в яме...')
        if not can_continue:
            sys.exit()

    def lumber_jill_quest(self):
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть перед Buck Galore...')
            if not can_continue:
                sys.exit()
        self.walk_from_buck_galore_to_jill()
        self.lumber_jill_quest_talk()
        self.dialogue_skip()
        self.lumber_jill_quest_axe_woods()
        self.lumber_jill_quest_collect_woods()
        self.lumber_jill_quest_talk()
        self.dialogue_skip()

    def walk_from_jill_to_stan(self):
        self.browser.hold_key_for_time(Keys.RIGHT, 2.2)
        self.browser.hold_key_for_time(Keys.UP, 2.5)
        self.browser.hold_key_for_time(Keys.RIGHT, 10.5)
        self.browser.hold_key_for_time(Keys.UP, 2.05)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.2)
        can_continue = can_i_continue('Убедись что персонаж в цветочке...')
        if not can_continue:
            sys.exit()

    def sticks_planks_quest_talk_stan(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_STAN_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_STAN_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def sticks_planks_quest_make_sticks(self):
        # Open saw
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_SAW_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_SAW_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        # Sticks
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_STICK_RECIPE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_STICK_RECIPE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        for i in range(8):
            # Create
            x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_X']
            y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_Y']
            x, y = get_coordinates(x_cf, y_cf)
            move_to_coordinates_and_click(x, y)
            # Wait craft
            sleep_randomly(13, 14)
            # Collect
            x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_X']
            y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_Y']
            x, y = get_coordinates(x_cf, y_cf)
            move_to_coordinates_and_click(x, y)

        # Close
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_CLOSE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_CLOSE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def sticks_planks_quest_make_wooden_stool(self):
        # Open saw
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_SAW_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_SAW_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        # Sticks
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_WOODEN_STOOL_RECIPE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_WOODEN_STOOL_RECIPE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Create
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        # Wait craft
        sleep_exact(33)
        # Collect
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_ACTION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Close
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_CLOSE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_CLOSE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def sticks_planks_quest_old_man_deliver(self):
        self.browser.hold_key_for_time(Keys.LEFT, 1.2)
        self.browser.hold_key_for_time(Keys.UP, 1.5)
        self.browser.hold_key_for_time(Keys.LEFT, 3.8)
        self.browser.hold_key_for_time(Keys.UP, 0.8)
        self.browser.hold_key_for_time(Keys.LEFT, 13.8)
        self.browser.hold_key_for_time(Keys.UP, 1)
        can_continue = can_i_continue('Убедись что персонаж в уголке море...')
        if not can_continue:
            sys.exit()

    def sticks_planks_quest_talk_old_man(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_OLD_MAN_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['STICKS_PLANKS_OLD_MAN_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def sticks_planks_quest_from_old_to_stan(self):
        self.browser.hold_key_for_time(Keys.DOWN, 0.9)
        self.browser.hold_key_for_time(Keys.RIGHT, 14)
        self.browser.hold_key_for_time(Keys.DOWN, 0.8)
        self.browser.hold_key_for_time(Keys.RIGHT, 3.6)
        self.browser.hold_key_for_time(Keys.DOWN, 1.45)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.3)

        can_continue = can_i_continue('Убедись что персонаж в цветочке...')
        if not can_continue:
            sys.exit()

    def sticks_planks_quest(self):
        self.walk_from_jill_to_stan()
        self.sticks_planks_quest_talk_stan()
        self.dialogue_skip()
        self.sticks_planks_quest_make_sticks()
        self.sticks_planks_quest_talk_stan()
        self.dialogue_skip()
        self.sticks_planks_quest_make_wooden_stool()
        self.sticks_planks_quest_talk_stan()
        self.dialogue_skip()
        self.sticks_planks_quest_old_man_deliver()
        self.sticks_planks_quest_talk_old_man()
        self.dialogue_skip()
        self.sticks_planks_quest_from_old_to_stan()
        self.sticks_planks_quest_talk_stan()
        self.dialogue_skip()

    def walk_from_stan_to_karen(self):
        self.browser.hold_key_for_time(Keys.LEFT, 1.2)
        self.browser.hold_key_for_time(Keys.UP, 13)
        self.browser.hold_key_for_time(Keys.LEFT, 8.4)
        self.browser.hold_key_for_time(Keys.UP, 4.5)

    def karen_cooking_quest_talk_karen(self):
        # Talk
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_KAREN_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_KAREN_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def karen_cooking_quest_wood_cooker(self):
        # Take Wood
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIFTH_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIFTH_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Fire
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Take off Wood
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIFTH_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIFTH_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def karen_cooking_quest_cook(self):
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_POPBERRY_RECIPE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_COOKER_POPBERRY_RECIPE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Create
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_ACTION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_ACTION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)
        # Wait craft
        sleep_exact(26)
        # Collect
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_ACTION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_ACTION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Close
        x_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_CLOSE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['KAREN_COOKING_CLOSE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def karen_cooking_quest_go_out_from_cooking(self):
        self.browser.hold_key_for_time(Keys.DOWN, 1)

    def karen_cooking_quest(self):
        self.walk_from_stan_to_karen()
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть внутри Karen Cooking...')
            if not can_continue:
                sys.exit()
        self.karen_cooking_quest_talk_karen()
        self.dialogue_skip()
        self.karen_cooking_quest_wood_cooker()
        self.karen_cooking_quest_cook()
        self.karen_cooking_quest_talk_karen()
        self.dialogue_skip()
        self.karen_cooking_quest_go_out_from_cooking()

    def return_to_back_galore(self):
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть перед Karen Cooking...')
            if not can_continue:
                sys.exit()
        self.browser.hold_key_for_time(Keys.DOWN, 7.7)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.6)
        self.browser.hold_key_for_time(Keys.DOWN, 0.3)
        self.browser.hold_key_for_time(Keys.RIGHT, 1)
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть внутри Back Galore...')
            if not can_continue:
                sys.exit()

    def main_menu_connect_ronin(self):
        connect_variants = self.browser.get_elements('button', 'Intro_connectButton')
        ronin_button = connect_variants[1]
        self.browser.click_element(ronin_button)

        ronin_variants = self.browser.get_elements('button', 'Intro_connectButton')
        ronin_extension_button = ronin_variants[0]
        self.browser.click_element(ronin_extension_button)

        sleep_randomly(2, 3)

        ronin_window_handle = self.browser.D.window_handles[-1]
        self.browser.D.switch_to.window(ronin_window_handle)
        self.browser.send_keys_to_element("//input[@id='password-input']", "4JILgi9e2dmgDb")

        self.browser.click_element_class_contains('button', 'ronin-button-default')

        err = self.browser.wait_presence_located(By.XPATH, "//button[contains(@class, 'ronin-button-default')]", 10)
        if err is not None:
            print(err)
        else:
            self.browser.click_element_class_contains('button', 'ronin-button-default')

        err = self.browser.wait_presence_located(By.XPATH, "//button[contains(@class, 'ronin-button-default')]", 10)
        if err is not None:
            print(err)
        else:
            self.browser.click_element_class_contains('button', 'ronin-button-default')
        sleep_randomly(2, 3)

        window_handles = self.browser.D.window_handles
        if len(window_handles) > 1:
            self.browser.D.close()
        self.browser.D.switch_to.window(window_handles[0])

    def ronin_sign(self):
        # Wait ronin sign_page
        window_handles = self.browser.D.window_handles
        is_there_ronin_page = len(window_handles) > 1
        while not is_there_ronin_page:
            window_handles = self.browser.D.window_handles
            is_there_ronin_page = len(window_handles) > 1
            sleep_randomly(1, 2)

        ronin_window_handle = self.browser.D.window_handles[-1]
        self.browser.D.switch_to.window(ronin_window_handle)

        err = self.browser.wait_presence_located(By.XPATH, "//button[contains(@class, 'ronin-button-default')]", 10)
        if err is not None:
            print(err)
        else:
            self.browser.click_element_class_contains('button', 'ronin-button-default')

        sleep_randomly(2, 3)

        window_handles = self.browser.D.window_handles
        if len(window_handles) > 1:
            self.browser.D.close()
        self.browser.D.switch_to.window(window_handles[0])

    def create_new_account(self):
        err = self.browser.wait_presence_located(By.XPATH, "//button[text()='Create New Account!']")
        if err is not None:
            print(err)
            sys.exit()

        element = self.browser.get_element(By.XPATH, "//button[text()='Create New Account!']")
        self.browser.click_element(element)

        self.ronin_sign()

    def get_my_level(self):
        level = 0

        skills_button = self.browser.get_element(By.XPATH, "//button[.//img[@aria-label='Skills']]")
        self.browser.click_element(skills_button)

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'Skills_skillPopup')]")
        if err is not None:
            print(err)
            return level

        levels = self.browser.get_elements_universal(By.XPATH,
                                                     "(//div[contains(@class, 'Skills_skillSlot')])[1]//span[not(contains(@class, 'skillDivider'))]")
        level = int(levels[0].text)

        self.browser.click_element_class_contains('button', 'commons_closeBtn')

        return level

    def get_my_berry(self):
        berry_span = self.browser.get_element(By.XPATH,
                                              "//div[contains(@class, 'Hud_berry__')]//span[contains(@class, 'commons_coinBalance__')]")
        berry = int(berry_span.text.split(',')[0].replace('.', ''))

        return berry

    def get_my_energy(self):
        energy_span = self.browser.get_element(By.XPATH,
                                               "//div[contains(@class, 'Hud_energy__')]//span[contains(@class, 'commons_coinBalance__')]")
        energy = int(energy_span.text.split(',')[0].replace('.', ''))

        return energy

    def get_optimal_seed_for_level(self, level):
        if level <= 1:
            seed = POPBERRY_SEED_TYPE
        elif 2 <= level <= 4:
            seed = BUTTERBERRY_SEED_TYPE
        else:
            seed = GRAINBOW_SEED_TYPE

        return seed

    def get_optimal_count_for_buy(self, need_seed, my_berry, my_energy):
        farm_3 = 180
        farm_2 = 120
        farm_1 = 60

        if farm_3 * SEED_NEED_BERRY[need_seed] <= my_berry and farm_3 * SEED_NEED_ENERGY[need_seed] <= my_energy:
            return farm_3
        elif farm_2 * SEED_NEED_BERRY[need_seed] <= my_berry and farm_2 * SEED_NEED_ENERGY[need_seed] <= my_energy:
            return farm_2
        elif farm_1 * SEED_NEED_BERRY[need_seed] <= my_berry and farm_1 * SEED_NEED_ENERGY[need_seed] <= my_energy:
            return farm_1

        count_for_energy = my_energy // SEED_NEED_ENERGY[need_seed]
        count_for_berry = my_berry // SEED_NEED_BERRY[need_seed]

        return min(count_for_energy, count_for_berry)

    def planter_calculate_need_seeds(self):
        my_level = self.get_my_level()
        my_berry = self.get_my_berry()
        my_energy = self.get_my_energy()
        print('my_level', my_level)
        print('my_berry', my_berry)
        print('my_energy', my_energy)

        need_seed = self.get_optimal_seed_for_level(my_level)
        need_count = self.get_optimal_count_for_buy(need_seed, my_berry, my_energy)

        return need_seed, need_count

    def planter_buy_seeds(self, seed_title, count):
        self.walk_to_hazel_in_bg()

        # Open shop
        x_cf = DEVICE_LOCATIONS[get_device_name()]['BG_SHOP_LOCATION_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['BG_SHOP_LOCATION_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        # Search seed
        time.sleep(1)
        search_input = self.browser.get_element(By.XPATH,
                                                "//input[@type='text' and contains(@class, 'Store_filter__')]")
        search_input.send_keys(seed_title)
        time.sleep(1)
        need_seed = self.browser.get_element(By.XPATH, "(//div[contains(@class, 'Store_store-item-container__')])[1]")
        self.browser.click_element(need_seed)
        time.sleep(1)
        # Buy
        time.sleep(1)
        quantity_input = self.browser.get_element(By.XPATH,
                                                  "//input[@type='number' and contains(@class, 'Store_quantity-input')]")
        quantity_input.clear()
        quantity_input.send_keys(count)
        time.sleep(1)
        buy_button = self.browser.get_element(By.XPATH,
                                              "//button[contains(@class, 'Store_buy-btn__') and contains(text(), 'Buy')]")
        self.browser.click_element(buy_button)
        time.sleep(1)
        close_button = self.browser.get_element(By.XPATH, "//button[contains(@class, 'commons_closeBtn__')]")
        self.browser.click_element(close_button)
        time.sleep(1)
    def planter_plant_in_farms(self, seed_count):
        if seed_count >= 121:
            need_farms = 3
        elif seed_count >= 61:
            need_farms = 2
        else:
            need_farms = 1

        bookmarks_button = self.browser.get_element(By.XPATH, "//button[.//img[@aria-label='Land and Bookmarks']]")
        self.browser.click_element(bookmarks_button)

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'LandAndTravel_container__')]")
        if err is not None:
            print(err)

        travel_buttons = self.browser.get_elements_universal(By.XPATH,
                                                             "//button[starts-with(@class, 'LandAndTravel_tab__')]")
        self.browser.click_element(travel_buttons[-1])

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'LandAndTravel_mapSquare')]")
        if err is not None:
            print(err)

        farm_numbers = self.browser.get_elements_universal(By.XPATH, "//div[contains(@class, 'LandAndTravel_mapsSquare')]//div[contains(@class, 'LandAndTravel_mapSquare')]/div[1]")
        need_farm_numbers = farm_numbers[:need_farms]

        farms_to_visit = []
        for need_farm in need_farm_numbers:
            need_farm = need_farm.text.replace('#', '')
            farms_to_visit.append(need_farm)

        close_button = self.browser.get_element(By.XPATH, "//button[contains(@class, 'commons_closeBtn__')]")
        self.browser.click_element(close_button)

        for farm in farms_to_visit:
            farm_number = int(farm)
            self.planter_plant_in_farm(farm_number)

    def planter_visit_farm(self, farm_number):
        bookmarks_button = self.browser.get_element(By.XPATH, "//button[.//img[@aria-label='Land and Bookmarks']]")
        self.browser.click_element(bookmarks_button)

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'LandAndTravel_container__')]")
        if err is not None:
            print(err)

        travel_buttons = self.browser.get_elements_universal(By.XPATH,
                                                             "//button[starts-with(@class, 'LandAndTravel_tab__')]")
        self.browser.click_element(travel_buttons[-1])

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'LandAndTravel_mapSquare')]")
        if err is not None:
            print(err)

        need_farm_button = self.browser.get_element(By.XPATH,
                                                    f"//div[contains(@class, 'LandAndTravel_mapSquare') and div[1][contains(text(), '#{farm_number}')]]//button")
        self.browser.click_element(need_farm_button)

        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть перед Buck Galore...')
            if not can_continue:
                sys.exit()

    def planter_farm_clicker(self, xl=0.432, xr=0.596, yt=0.286, yb=0.707, x_bs=8, y_bs=12):
        x_width = xr - xl
        y_height = yb - yt
        x_blocks = x_bs
        y_blocks = y_bs
        for i in range(x_blocks):
            for j in range(y_blocks):
                x_cf = xl + (x_width / x_blocks * i)
                y_cf = yt + (y_height / y_blocks * j)
                x, y = get_coordinates(x_cf, y_cf)
                just_click(x, y)

    def planter_plant_water_1000(self):
        self.browser.hold_key_for_time(Keys.UP, 5)
        self.browser.hold_key_for_time(Keys.LEFT, 2.3)

        # Take seed
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_FIRST_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        self.planter_farm_clicker()

        self.browser.hold_key_for_time(Keys.LEFT, 1)

        self.planter_farm_clicker()

        self.browser.hold_key_for_time(Keys.LEFT, 1)

        self.planter_farm_clicker()

        # Take Water
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        self.planter_farm_clicker()

        self.browser.hold_key_for_time(Keys.RIGHT, 1)

        self.planter_farm_clicker()

        self.browser.hold_key_for_time(Keys.RIGHT, 1)

        self.planter_farm_clicker()

        # Untake Water
        x_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['SLOT_SECOND_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

    def planter_plant_water_2123(self):
        pass

    def planter_plant_water_4717(self):
        pass

    def planter_plant_water(self, farm_number):
        if farm_number == 1000:
            self.planter_plant_water_1000()
        elif farm_number == 2123:
            self.planter_plant_water_2123()
        elif farm_number == 4717:
            self.planter_plant_water_4717()

    def planter_plant_in_farm(self, farm_number):
        self.planter_visit_farm(farm_number)
        self.planter_plant_water(farm_number)

    def bookmarker_walk_from_bg_to_farms(self):
        self.browser.hold_key_for_time(Keys.LEFT, 1)
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, 0.2)
        self.browser.hold_key_for_time(Keys.LEFT, 2)
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.UP, 0.2)
        self.browser.hold_key_for_time(Keys.LEFT, 2.8)
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, 0.3)
        self.browser.hold_key_for_time(Keys.LEFT, 2.1)
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.UP, 0.25)
        self.browser.hold_key_for_time(Keys.LEFT, 1.7)
        self.browser.hold_key_for_time(Keys.UP, 0.6)

    def bookmarker_walk_from_in_bg_to_farms(self):
        self.buck_galore_quest_go_out_from_bg(1)
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть перед Buck Galore...')
            if not can_continue:
                sys.exit()
        self.bookmarker_walk_from_bg_to_farms()

    def bookmarker_farms_visit_farm(self, farm):
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue('Я должен быть внутри магазина Фермы...')
            if not can_continue:
                sys.exit()

        self.browser.hold_key_for_time(Keys.RIGHT, 1.7)
        self.browser.hold_key_for_time(Keys.UP, 4)
        self.browser.hold_key_for_time(Keys.RIGHT, 0.5)

        x_cf = DEVICE_LOCATIONS[get_device_name()]['FARMS_RED_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['FARMS_RED_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'LandAndTravel_container')]")
        if err is not None:
            print(err)
            sys.exit()

        # Buy
        farm_input = self.browser.get_element(By.XPATH,
                                              "//input[@type='number' and contains(@class, 'LandAndTravel_numberInput')]")
        farm_input.clear()
        farm_input.send_keys(farm)

        go_button = self.browser.get_element(By.XPATH, "//div[contains(@class, 'LandAndTravel_optionButtons')]//button")
        self.browser.click_element(go_button)

    def bookmarker_bookmark_farm(self, farm):
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue(f"Я должен быть внутри Фермы {farm}...")
            if not can_continue:
                sys.exit()

        x_cf = DEVICE_LOCATIONS[get_device_name()]['FARM_TITLE_X']
        y_cf = DEVICE_LOCATIONS[get_device_name()]['FARM_TITLE_Y']
        x, y = get_coordinates(x_cf, y_cf)
        move_to_coordinates_and_click(x, y)

        err = self.browser.wait_presence_located(By.XPATH, "//div[starts-with(@class, 'FarmDetails_FarmDetailsPanel')]")
        if err is not None:
            print(err)
            sys.exit()

        bookmark_button = self.browser.get_element(By.XPATH,
                                                   "//div[contains(@class, 'FarmDetails_FarmDetailsActions')]//button[contains(text(), 'Bookmark')]")
        self.browser.click_element(bookmark_button)

        close_button = self.browser.get_element(By.XPATH, "//button[contains(@class, 'commons_closeBtn__')]")
        self.browser.click_element(close_button)

    def bookmarker_go_from_farm_to_sauna_1000(self):
        self.browser.hold_key_for_time(Keys.UP, 4.5)
        self.browser.hold_key_for_time(Keys.LEFT, 1.2)
        self.browser.hold_key_for_time(Keys.UP, 2.3)

    def bookmarker_go_from_farm_to_sauna_2123(self):
        self.browser.hold_key_for_time(Keys.UP, 2.9)
        self.browser.hold_key_for_time(Keys.LEFT, 2.6)

    def bookmarker_go_from_farm_to_sauna_4717(self):
        self.browser.hold_key_for_time(Keys.UP, 1.3)
        self.browser.hold_key_for_time(Keys.LEFT, 2.3)

    def bookmarker_go_from_farm_to_sauna(self, farm):
        if farm == 1000:
            self.bookmarker_go_from_farm_to_sauna_1000()
        elif farm == 2123:
            self.bookmarker_go_from_farm_to_sauna_2123()
        elif farm == 4717:
            self.bookmarker_go_from_farm_to_sauna_4717()

        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue(f"Я должен быть внутри Сауны...")
            if not can_continue:
                sys.exit()

    def go_out_from_sauna(self):
        self.browser.hold_key_for_time(Keys.DOWN, 0.5)

    def walk_from_sauna_to_farms(self):
        self.browser.hold_key_for_time(Keys.DOWN, 0.3)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.6)
        self.browser.hold_key_for_time(Keys.UP, 0.7)

    def bookmarker_walk_from_in_sauna_to_farms(self):
        self.go_out_from_sauna()
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue(f"Я должен быть перед Сауной...")
            if not can_continue:
                sys.exit()

        self.walk_from_sauna_to_farms()

    def bookmarker_walk_from_in_sauna_to_buck_galore(self):
        self.go_out_from_sauna()
        try:
            self.wait_location_change()
        except:
            can_continue = can_i_continue(f"Я должен быть перед Сауной...")
            if not can_continue:
                sys.exit()

        self.browser.hold_key_for_time(Keys.DOWN, 0.15)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.6)
        self.walk_from_farm_to_buck_galore()

    def left_right_move(self, direction):
        start_time = time.time()

        if direction == LDir:
            self.browser.hold_key_for_time(Keys.LEFT, 1.92)
            self.browser.hold_key_for_time(Keys.RIGHT, 1.45)
        elif direction == RDir:
            self.browser.hold_key_for_time(Keys.RIGHT, 1.94)
            self.browser.hold_key_for_time(Keys.LEFT, 1.46)
        elif direction == TDir:
            self.browser.hold_key_for_time(Keys.UP, 1.93)
            self.browser.hold_key_for_time(Keys.DOWN, 1.47)
        elif direction == BDir:
            self.browser.hold_key_for_time(Keys.DOWN, 1.99)
            self.browser.hold_key_for_time(Keys.UP, 1.41)
        elif direction == TLDir:
            self.browser.hold_keys_for_time(Keys.UP, Keys.LEFT, 1.93)
            self.browser.hold_keys_for_time(Keys.DOWN, Keys.RIGHT, 1.90)
        elif direction == TRDir:
            self.browser.hold_keys_for_time(Keys.UP, Keys.RIGHT, 1.92)
            self.browser.hold_keys_for_time(Keys.DOWN, Keys.LEFT, 1.95)
        elif direction == BLDir:
            self.browser.hold_keys_for_time(Keys.DOWN, Keys.LEFT, 1.97)
            self.browser.hold_keys_for_time(Keys.UP, Keys.RIGHT, 1.96)
        elif direction == BRDir:
            self.browser.hold_keys_for_time(Keys.DOWN, Keys.RIGHT, 1.91)
            self.browser.hold_keys_for_time(Keys.UP, Keys.LEFT, 1.92)

        end_time = time.time()
        total_secs = int(end_time - start_time)
        return total_secs

    def left_right_one_minute(self, directions):
        seconds = 60
        seconds_before_move = random.randint(5, 40)
        time.sleep(seconds_before_move)

        move_secs = self.left_right_move(random.choice(directions))

        seconds_after_move = seconds - seconds_before_move - move_secs
        time.sleep(seconds_after_move)
