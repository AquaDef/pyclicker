import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from random import seed
from random import randint
from random import uniform
seed(3)

delay = 0.02
button = Button.left
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='[')
with open("clicks-demo.ta") as f:
    content = f.readlines()

content = [x.strip() for x in content]
for thing in content:
    if thing.startswith("-"):
        content.remove(thing)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        print("Welcome to autoclicker!")
        print("Press {} to toggle autoclicking.".format(start_stop_key))
        print("Press {} to exit the program or Ctrl + C in the terminal.".format(exit_key))
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:

                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.01)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
