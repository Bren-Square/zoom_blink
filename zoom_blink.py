"""zoom_blink.py - Checks for zoom meetings and
lights up a blink(1) LED if you are in a meeting.
"""
import time
import psutil
from blink1.blink1 import blink1


def proc_check(process_name):
    """proc_check: Checks for running process on system
    Args: process_name (string): the name of the process you are looking for.
    Returns: boolean: bool tells you if process is running or not.
    """
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False


if __name__ == "__main__":
    while True:
        with blink1() as b1:
            b1.fade_to_color(100, 'red')
            while proc_check("CptHost"):
                time.sleep(5)
        time.sleep(10)
