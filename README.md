# py-keyboard-mouse
Keyboard mouse emulation implemented in pure python

# Quick Start Guide

## Installation
- ```git clone https://github.com/lucca-ruhland/py-keyboard-mouse```
- ```cd py-keyboard-mouse```
- ```pip install .```

## How to run mouse emulation 
- ```keyboard-mouse [--flags]```

### flags
| flag | description |
| ---- | ----------- |
| -h, --help | show help message |
| -c, --config | set path to config file with ini or yaml style |
| --left | set key for moving cursor left |
| --right | set key for moving curosor right |
| --up | set key for moving cursor up |
| --down | set key for moving cursor down |
| --toggle | set key to toggle between normal (writing) mode and mouse emulation |
| --increment | set mouse sensitivity (cursor movement in pixel per key stroke) |

### default hotkeys
- use ```CTRL + M``` to toggle between mouse and normal mode
- use ```h``` to go left
- use ```l``` to go right
- use ```h``` to go up
- use ```k``` to go down
- use ```right CTRL``` for left click

# config file
.ini or .yaml style can be used for configuration files.
An example is given under [/example/example.config](/example/example.config).
View https://github.com/bw2/ConfigArgParse for more information on how to create config files.

# Known Issues
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
