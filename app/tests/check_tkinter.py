import sys

from app.logic.tkinter import can_i_continue

print("start")

print("Waiting tkinter continue")

can_continue = can_i_continue('Могу продолжать?')
if not can_continue:
    sys.exit()

print("end")
