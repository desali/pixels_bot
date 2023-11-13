import json

from core.settings import get_screen_size


def read_file_data(filename):
    with open(f"json/{filename}") as json_file:
        return json.load(json_file)


def get_coordinates(x, y):
    tl_x, tl_y, br_x, br_y = get_screen_size()

    screen_width = br_x - tl_x
    screen_height = br_y - tl_y

    new_x = tl_x + (screen_width * x)
    new_y = tl_y + (screen_height * y)
    return new_x, new_y
