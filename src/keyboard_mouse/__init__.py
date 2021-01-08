from keyboard_mouse.mouse_emulation import MouseHandler, BasicMouseHandler


def create_emulator(config: dict = None) -> MouseHandler:
    if config is None:
        return BasicMouseHandler.default()
    else:
        return BasicMouseHandler.from_config(config)
