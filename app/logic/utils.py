import random
import time


def sleep_randomly(start=1, end=3):
    time.sleep(random.randint(start, end))


def sleep_exact(second):
    time.sleep(second)

