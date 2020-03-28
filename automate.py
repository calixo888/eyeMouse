import pyautogui
import sys

pyautogui.FAILSAFE = False

# PARAMETERS FOR MOVE_MOUSE
# coords - coordinates of where the mouse should be relative to eyes -> tuple
# left_click - if the mouse should left click -> boolean -> wink left eye
# right_click - if the mouse should right click -> boolean -> wink right eye
# dbl_click - if the mouse should double click -> boolean -> blink both eyes twice
# shut_down - if the program should be shut down -> boolean -> shut eyes for prolonged time
def move_mouse(coords, left_click, right_click, dbl_click, shut_down):
    if shut_down:
        sys.exit()

    pyautogui.moveTo(coords)

    # Executing clicks
    if left_click:
        pyautogui.click(button="left")

    elif right_click:
        pyautogui.click(button="right")

    elif dbl_click:
        pyautogui.doubleClick()
