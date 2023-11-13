import pyautogui

x, y = pyautogui.position()
print(x, y)



tl_x, tl_y, br_x, br_y = -2560, 0, -960, 1000

screen_width = br_x - tl_x
screen_height = br_y - tl_y

max_x = screen_width - 1
max_y = screen_height - 1

print(f"Максимальная X координата: {max_x}")
print(f"Максимальная Y координата: {max_y}")

print((x-tl_x)/max_x, (y-tl_y)/max_y)
