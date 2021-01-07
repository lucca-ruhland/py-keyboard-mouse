from dataclasses import dataclass
from typing import List

import keyboard
import pyautogui


@dataclass
class Hotkey:
    keyname: str
    function: object
    enabled: bool

    def on_triggered(self):
        if enabled:
            self.function()

    def toggle(self):
        self.enabled = not self.enabled


class Mouse:
    def move_up(self):
        raise NotImplementedError

    def move_down(self):
        raise NotImplementedError

    def move_left(self):
        raise NotImplementedError

    def move_right(self):
        raise NotImplementedError

    def click(self):
        raise NotImplementedError


class BasicMouse:
    def __init__(self, increment=35):
        self.increment = increment

    def move_up(self):
        pyautogui.move(0, -self.increment)

    def move_down(self):
        pyautogui.move(0, self.increment)

    def move_left(self):
        pyautogui.move(-self.increment, 0)

    def move_right(self):
        pyautogui.move(self.increment, 0)

    def click(self):
        pyautogui.click(duration=0.3)


class MouseHandler:
    def register_hotkey(self, keyname: str, function: object) -> None:
        raise NotImplementedError

    def toggle_hotkeys(self) -> None:
        raise NotImplementedError

    def start_emulation(self) -> None:
        raise NotImplementedError


class BasicMouseHandler(MouseHandler):
    def __init__(self, mouse: Mouse, toggle_hotkey: Hotkey, hotkeys: List[Hotkey]):
        self.mouse = mouse
        self.hotkeys = hotkeys
        self.toggle_hotkey = toggle_hotkey
        self.register_hotkeys()

    def register_hotkeys(self) -> None:
        for hotkey in self.hotkeys:
            self.register_hotkey(hotkey.keyname, hotkey.on_triggered)

    def register_hotkey(self, keyname: str, function: object) -> None:
        keyboard.add_hotkey(keyname, lambda: function())

    @classmethod()
    def from_config(cls, config: dict) -> BasicMouseEmulator:
        pass

    def toggle_hotkeys():
        for hotkey in self.hotkeys:
            hotkey.toggle()

    def start_emulation() -> None:
        keyboard.wait()




