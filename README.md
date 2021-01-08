# py-keyboard-mouse
Keyboard mouse emulation implemented in pure python

# Quick Start Guide

## Installation
- ```git clone https://github.com/lucca-ruhland/py-keyboard-mouse```
- ```cd py-keyboard-mouse```
- ```pip install .```

## How to run mouse emulation 
- ```keyboard-mouse```

### default hotkeys
- use ```CTRL + M``` to toggle between mouse and normal mode
- use ```h``` to go left
- use ```l``` to go right
- use ```h``` to go up
- use ```k``` to go down
-use ```right CTRL``` for left click

### Known Issues
- keyboard-mouse needs root permissions
- It may be necessary to run ```xhost +``` before starting keyboard-mouse

# Usage in code
```python
from keyboard_mouse import create_emulator


# for default keybindings
default_emulator = create_emulator()
default_emulator.start_emulation()

# =============================================
# for custom keybindings

custom_config = {'TOGGLE_MODE': 'ctrl+alt+m',
                'LEFT': 'a',
                'RIGHT': 'd',
                'UP':'w',
                'DOWN':'k',
                'CLICK': 'left ctrl'}     

custom_emulator = create_emulator(custom_config)
custom_emulator.start_emulation()
```
