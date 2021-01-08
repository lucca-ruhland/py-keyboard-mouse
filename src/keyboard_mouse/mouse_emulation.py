from dataclasses import dataclass
from typing import List
from collections.abc import Callable

import keyboard
import pyautogui


class CannotBuildFromConfig(Exception):
    pass


@dataclass
class Hotkey:
    key_name: str
    function: Callable
    enabled: bool

    def on_triggered(self):
        if self.enabled:
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
    def register_hotkey(self, key_name: str, function: object) -> None:
        raise NotImplementedError

    def toggle_hotkeys(self) -> None:
        raise NotImplementedError

    def start_emulation(self) -> None:
        raise NotImplementedError


class BasicMouseHandler(MouseHandler):
    def __init__(self, toggle_hotkey: str, hotkeys: List[Hotkey]):
        self.hotkeys = hotkeys
        self.toggle_hotkey = Hotkey(key_name=toggle_hotkey, function=self.toggle_hotkeys, enabled=True)
        self.register_hotkeys()

    def register_hotkeys(self) -> None:
        for hotkey in self.hotkeys:
            self.register_hotkey(hotkey.key_name, hotkey.on_triggered)

    def register_hotkey(self, key_name: str, function: Callable) -> None:
        keyboard.add_hotkey(key_name, lambda: function())

    @classmethod
    def default(cls):
        import keyboard_mouse.default_config as config

        mouse = BasicMouse(config.INCREMENT)

        toggle = config.TOGGLE_MODE

        left_hotkey = Hotkey(config.LEFT, mouse.move_left, False)
        right_hotkey = Hotkey(config.RIGHT, mouse.move_right, False)
        up_hotkey = Hotkey(config.UP, mouse.move_up, False)
        down_hotkey = Hotkey(config.DOWN, mouse.move_down, False)

        hotkey_list = [left_hotkey, right_hotkey, up_hotkey, down_hotkey]

        return cls(toggle, hotkey_list)

    @classmethod
    def from_config(cls, config: dict):
        try:
            increment = config['INCREMENT']
            mouse = BasicMouse(increment)

            toggle = config['TOGGLE_MODE']

            left = config['LEFT']
            left_hotkey = Hotkey(left, mouse.move_left, False)

            right = config['RIGHT']
            right_hotkey = Hotkey(right, mouse.move_right, False)

            up = config['UP']
            up_hotkey = Hotkey(up, mouse.move_up, False)

            down = config['DOWN']
            down_hotkey = Hotkey(down, mouse.move_down, False)

            click = config['CLICK']
            click_hotkey = Hotkey(click, mouse.click, False)

            hotkey_list = [left_hotkey, right_hotkey, up_hotkey, down_hotkey, click_hotkey]

            return cls(toggle, hotkey_list)
        except KeyError:
            raise CannotBuildFromConfig

    def toggle_hotkeys(self):
        for hotkey in self.hotkeys:
            hotkey.toggle()

    def start_emulation(self) -> None:
        keyboard.wait()
