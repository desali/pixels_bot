import sys

import pyautogui as pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from core import settings as S
from core.constants import BARNEY_SEED_X, BARNEY_SEED_Y, SLOT_FIRST_Y, SLOT_FIRST_X, BARNEY_LOCATION_X, \
    BARNEY_LOCATION_Y, SLOT_SECOND_X, SLOT_SECOND_Y, SLOT_THIRD_X, SLOT_THIRD_Y, BARNEY_MY_LOCATION_X, \
    BARNEY_MY_LOCATION_Y, DANGER_DALE_LOCATION_X, DANGER_DALE_LOCATION_Y, HAZEL_LOCATION_X, HAZEL_LOCATION_Y, \
    LUMBER_JILL_LOCATION_Y, LUMBER_JILL_LOCATION_X, LUMBER_JILL_WOOD_1_Y, LUMBER_JILL_WOOD_1_X, LUMBER_JILL_WOOD_2_Y, \
    LUMBER_JILL_WOOD_2_X, SLOT_FOURTH_Y, SLOT_FOURTH_X, STICKS_PLANKS_SAW_Y, STICKS_PLANKS_SAW_X, \
    STICKS_PLANKS_STICK_RECIPE_Y, STICKS_PLANKS_STICK_RECIPE_X, STICKS_PLANKS_ACTION_X, STICKS_PLANKS_ACTION_Y, \
    STICKS_PLANKS_CLOSE_X, STICKS_PLANKS_CLOSE_Y, STICKS_PLANKS_STAN_Y, STICKS_PLANKS_STAN_X, \
    STICKS_PLANKS_WOODEN_STOOL_RECIPE_X, STICKS_PLANKS_WOODEN_STOOL_RECIPE_Y, STICKS_PLANKS_OLD_MAN_X, \
    STICKS_PLANKS_OLD_MAN_Y, SLOT_FIFTH_X, SLOT_FIFTH_Y, KAREN_COOKING_COOKER_X, KAREN_COOKING_COOKER_Y, \
    KAREN_COOKING_COOKER_POPBERRY_RECIPE_X, KAREN_COOKING_COOKER_POPBERRY_RECIPE_Y, KAREN_COOKING_ACTION_Y, \
    KAREN_COOKING_ACTION_X, KAREN_COOKING_CLOSE_X, KAREN_COOKING_CLOSE_Y, KAREN_COOKING_KAREN_X, KAREN_COOKING_KAREN_Y
from core.utils import get_coordinates
from logic.pyautogui import move_to_coordinates_and_click, hold_mouse_for_time, press_key, window_is_active
from logic.tkinter import can_i_continue
from logic.utils import sleep_randomly, sleep_exact


class Bot:
    browser = None

    def __init__(self, browser):
        self.browser = browser

    def open_main_menu(self):
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
        x, y = get_coordinates(SLOT_FIRST_X, SLOT_FIRST_Y)
        move_to_coordinates_and_click(x, y)

        # Plant
        x, y = get_coordinates(BARNEY_SEED_X, BARNEY_SEED_Y)
        move_to_coordinates_and_click(x, y)

    def barney_quest_talk(self):
        # Talk
        x, y = get_coordinates(BARNEY_LOCATION_X, BARNEY_LOCATION_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def barney_quest_water_seed(self):
        sleep_randomly(1, 2)
        # Take water
        x, y = get_coordinates(SLOT_FIRST_X, SLOT_FIRST_Y)
        move_to_coordinates_and_click(x, y)

        # Water
        x, y = get_coordinates(BARNEY_SEED_X, BARNEY_SEED_Y)
        move_to_coordinates_and_click(x, y)

        # Take off water
        x, y = get_coordinates(SLOT_FIRST_X, SLOT_FIRST_Y)
        move_to_coordinates_and_click(x, y)

    def barney_quest_fertilize_seed(self):
        sleep_randomly(1, 2)

        # Take fertilizer
        x, y = get_coordinates(SLOT_SECOND_X, SLOT_SECOND_Y)
        move_to_coordinates_and_click(x, y)

        # Fertilize
        x, y = get_coordinates(BARNEY_SEED_X, BARNEY_SEED_Y)
        move_to_coordinates_and_click(x, y)

    def barney_quest_cut_seed(self):
        sleep_randomly(1, 2)

        # Take shears
        x, y = get_coordinates(SLOT_SECOND_X, SLOT_SECOND_Y)
        move_to_coordinates_and_click(x, y)

        # Cut
        x, y = get_coordinates(BARNEY_SEED_X, BARNEY_SEED_Y)
        move_to_coordinates_and_click(x, y)

        # Take off shears
        x, y = get_coordinates(SLOT_SECOND_X, SLOT_SECOND_Y)
        move_to_coordinates_and_click(x, y)

    def barney_quest_eat_seed(self):
        sleep_randomly(1, 2)

        # Take fertilizer
        x, y = get_coordinates(SLOT_THIRD_X, SLOT_THIRD_Y)
        move_to_coordinates_and_click(x, y)

        # Fertilize
        x, y = get_coordinates(BARNEY_MY_LOCATION_X, BARNEY_MY_LOCATION_Y)
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
        x, y = get_coordinates(DANGER_DALE_LOCATION_X, DANGER_DALE_LOCATION_Y)
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
        x, y = get_coordinates(HAZEL_LOCATION_X, HAZEL_LOCATION_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def buck_galore_quest_go_out_from_bg(self):
        self.browser.hold_keys_for_time(Keys.LEFT, Keys.DOWN, 4)

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
        self.buck_galore_quest_go_out_from_bg()

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
        self.browser.hold_key_for_time(Keys.LEFT, 2)
        can_continue = can_i_continue('Убедись что персонаж в яме...')
        if not can_continue:
            sys.exit()

    def lumber_jill_quest_talk(self):
        # Talk
        x, y = get_coordinates(LUMBER_JILL_LOCATION_X, LUMBER_JILL_LOCATION_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def lumber_jill_quest_axe_woods(self):
        sleep_randomly(1, 2)

        # Take axe
        x, y = get_coordinates(SLOT_FOURTH_X, SLOT_FOURTH_Y)
        move_to_coordinates_and_click(x, y)

        for i in range(6):
            x, y = get_coordinates(LUMBER_JILL_WOOD_1_X, LUMBER_JILL_WOOD_1_Y)
            move_to_coordinates_and_click(x, y)

        for i in range(6):
            x, y = get_coordinates(LUMBER_JILL_WOOD_2_X, LUMBER_JILL_WOOD_2_Y)
            move_to_coordinates_and_click(x, y)

        # UnTake axe
        x, y = get_coordinates(SLOT_FOURTH_X, SLOT_FOURTH_Y)
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
        self.browser.hold_key_for_time(Keys.DOWN, 0.5)
        self.browser.hold_key_for_time(Keys.RIGHT, 0.2)
        can_continue = can_i_continue('Убедись что персонаж в яме...')
        if not can_continue:
            sys.exit()

    def lumber_jill_quest(self):
        # try:
        #     self.wait_location_change()
        # except:
        #     can_continue = can_i_continue('Я должен быть перед Buck Galore...')
        #     if not can_continue:
        #         sys.exit()
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
        self.browser.hold_key_for_time(Keys.UP, 2)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.3)
        can_continue = can_i_continue('Убедись что персонаж в цветочке...')
        if not can_continue:
            sys.exit()

    def sticks_planks_quest_talk_stan(self):
        # Talk
        x, y = get_coordinates(STICKS_PLANKS_STAN_X, STICKS_PLANKS_STAN_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def sticks_planks_quest_make_sticks(self):
        # Open saw
        x, y = get_coordinates(STICKS_PLANKS_SAW_X, STICKS_PLANKS_SAW_Y)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        # Sticks
        x, y = get_coordinates(STICKS_PLANKS_STICK_RECIPE_X, STICKS_PLANKS_STICK_RECIPE_Y)
        move_to_coordinates_and_click(x, y)

        for i in range(8):
            # Create
            x, y = get_coordinates(STICKS_PLANKS_ACTION_X, STICKS_PLANKS_ACTION_Y)
            move_to_coordinates_and_click(x, y)
            # Wait craft
            sleep_randomly(12, 13)
            # Collect
            x, y = get_coordinates(STICKS_PLANKS_ACTION_X, STICKS_PLANKS_ACTION_Y)
            move_to_coordinates_and_click(x, y)

        # Close
        x, y = get_coordinates(STICKS_PLANKS_CLOSE_X, STICKS_PLANKS_CLOSE_Y)
        move_to_coordinates_and_click(x, y)

    def sticks_planks_quest_make_wooden_stool(self):
        # Open saw
        x, y = get_coordinates(STICKS_PLANKS_SAW_X, STICKS_PLANKS_SAW_Y)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        # Sticks
        x, y = get_coordinates(STICKS_PLANKS_WOODEN_STOOL_RECIPE_X, STICKS_PLANKS_WOODEN_STOOL_RECIPE_Y)
        move_to_coordinates_and_click(x, y)

        # Create
        x, y = get_coordinates(STICKS_PLANKS_ACTION_X, STICKS_PLANKS_ACTION_Y)
        move_to_coordinates_and_click(x, y)
        # Wait craft
        sleep_exact(32)
        # Collect
        x, y = get_coordinates(STICKS_PLANKS_ACTION_X, STICKS_PLANKS_ACTION_Y)
        move_to_coordinates_and_click(x, y)

        # Close
        x, y = get_coordinates(STICKS_PLANKS_CLOSE_X, STICKS_PLANKS_CLOSE_Y)
        move_to_coordinates_and_click(x, y)

    def sticks_planks_quest_old_man_deliver(self):
        self.browser.hold_key_for_time(Keys.LEFT, 1.2)
        self.browser.hold_key_for_time(Keys.UP, 1.5)
        self.browser.hold_key_for_time(Keys.LEFT, 3.6)
        self.browser.hold_key_for_time(Keys.UP, 0.8)
        self.browser.hold_key_for_time(Keys.LEFT, 14)
        self.browser.hold_key_for_time(Keys.UP, 1)
        can_continue = can_i_continue('Убедись что персонаж в уголке море...')
        if not can_continue:
            sys.exit()

    def sticks_planks_quest_talk_old_man(self):
        # Talk
        x, y = get_coordinates(STICKS_PLANKS_OLD_MAN_X, STICKS_PLANKS_OLD_MAN_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def sticks_planks_quest_from_old_to_stan(self):
        self.browser.hold_key_for_time(Keys.DOWN, 0.8)
        self.browser.hold_key_for_time(Keys.RIGHT, 14)
        self.browser.hold_key_for_time(Keys.DOWN, 0.8)
        self.browser.hold_key_for_time(Keys.RIGHT, 3.6)
        self.browser.hold_key_for_time(Keys.DOWN, 1.5)
        self.browser.hold_key_for_time(Keys.RIGHT, 1.2)

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
        self.browser.hold_key_for_time(Keys.LEFT, 1.15)
        self.browser.hold_key_for_time(Keys.UP, 13)
        self.browser.hold_key_for_time(Keys.LEFT, 8.4)
        self.browser.hold_key_for_time(Keys.UP, 4.5)

    def karen_cooking_quest_talk_karen(self):
        # Talk
        x, y = get_coordinates(KAREN_COOKING_KAREN_X, KAREN_COOKING_KAREN_Y)
        move_to_coordinates_and_click(x, y)
        sleep_randomly(1, 2)

    def karen_cooking_quest_wood_cooker(self):
        # Take Wood
        x, y = get_coordinates(SLOT_FIFTH_X, SLOT_FIFTH_Y)
        move_to_coordinates_and_click(x, y)

        # Fire
        x, y = get_coordinates(KAREN_COOKING_COOKER_X, KAREN_COOKING_COOKER_Y)
        move_to_coordinates_and_click(x, y)

        # Take off Wood
        x, y = get_coordinates(SLOT_FIFTH_X, SLOT_FIFTH_Y)
        move_to_coordinates_and_click(x, y)

    def karen_cooking_quest_cook(self):
        x, y = get_coordinates(KAREN_COOKING_COOKER_X, KAREN_COOKING_COOKER_Y)
        move_to_coordinates_and_click(x, y)

        sleep_exact(2)

        x, y = get_coordinates(KAREN_COOKING_COOKER_POPBERRY_RECIPE_X, KAREN_COOKING_COOKER_POPBERRY_RECIPE_Y)
        move_to_coordinates_and_click(x, y)

        # Create
        x, y = get_coordinates(KAREN_COOKING_ACTION_X, KAREN_COOKING_ACTION_Y)
        move_to_coordinates_and_click(x, y)
        # Wait craft
        sleep_exact(26)
        # Collect
        x, y = get_coordinates(KAREN_COOKING_ACTION_X, KAREN_COOKING_ACTION_Y)
        move_to_coordinates_and_click(x, y)

        # Close
        x, y = get_coordinates(KAREN_COOKING_CLOSE_X, KAREN_COOKING_CLOSE_Y)
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
