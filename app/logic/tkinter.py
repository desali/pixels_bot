import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

import pyperclip

from app.core.settings import set_screen_size, devices


def request_and_set_coordinates():
    def on_device_selected(event):
        device_name = combo_box.get()
        set_screen_size(device_name, *devices[device_name])
        root.destroy()

    root = tk.Tk()
    root.geometry("600x600")

    label = tk.Label(root, text="Выберите устройство:")
    label.pack(pady=10)

    combo_box = ttk.Combobox(root, values=list(devices.keys()))
    combo_box.current(0)
    combo_box.bind("<<ComboboxSelected>>", on_device_selected)
    combo_box.pack(pady=10)

    root.mainloop()


def can_i_continue(text):
    def on_continue():
        nonlocal choice
        choice = True
        window.destroy()

    window = tk.Tk()
    window.geometry("600x600")
    window.title(text)

    yes_button = tk.Button(window, text="Продолжай...", command=on_continue)
    yes_button.pack(pady=30)

    choice = False
    window.mainloop()
    return choice


def get_chrome_version_and_selenium_port():
    def on_submit():
        root.destroy()

    root = tk.Tk()
    root.geometry("600x600")
    root.title("Selenium порт и версия хрома (цифры)")

    port_value = tk.StringVar()
    version_value = tk.StringVar()

    port_version = pyperclip.paste()
    port = port_version.split(':')[0]
    version = port_version.split(':')[1]

    port_value.set(port)
    version_value.set(version)

    tk.Label(root, text="Порт Selenium:").pack(pady=5)
    port_entry = tk.Entry(root, textvariable=port_value)
    port_entry.pack(pady=5)

    tk.Label(root, text="Версия Chrome:").pack(pady=5)
    version_entry = tk.Entry(root, textvariable=version_value)
    version_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Продолжить", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()
    return port_value.get(), version_value.get()


def get_ads_profile_id():
    def on_submit():
        nonlocal profile_id
        profile_id = profile_id_entry.get()
        root.destroy()

    root = tk.Tk()
    root.geometry("600x600")
    root.title("Укажи ads profile_id")

    tk.Label(root, text="Id profile:").pack(pady=5)
    profile_id_entry = tk.Entry(root)
    profile_id_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Продолжить", command=on_submit)
    submit_button.pack(pady=10)

    profile_id = ""
    root.mainloop()
    return profile_id
