# DS4LED

[![Crafted by Human](https://madebyhuman.iamjarl.com/badges/crafted-white.svg)](https://madebyhuman.iamjarl.com)

A little cli/gui app for **linux** to control LED color on Dualshock 4.

# Installation

```bash
> git clone https://github.com/ra1nlox/ds4led.git

> cd ds4led

> python -m venv ./

> source ./bin/activate # or whatever you use

> pyenv install # or, if you already have it, it should work automatically

> pip install -r requirements.txt
```

# Setup

To use this app without `sudo`, you need to:
1. Create a group "ds4led": `sudo groupadd ds4led`
2. Add your user to the group: `sudo usermod -aG ds4led "$USER"`
3. Copy `ds4led-permissions.sh` in some directory (e.g. `/usr/local/bin`)
4. Create a udev rule to execute this script for this device.
   (E.g. `SUBSYSTEM=="leds", KERNEL=="input*:*", ATTR{brightness}=="*", KERNELS=="0005:054C:09CC.*", RUN+="/usr/local/bin/ds4led-permissions.sh"` works for me)

The script is pretty selfexplanatory.

# Usage

```bash
> python main.py 0 0 64 # R G B values 0-255

> python main.py -h 000040 # Any valid hex value, without hashtag

> python main.py # Will prompt a color picker dialogue window

> python main.py -p [key] # Will pick a selected preset

> python main.py -l # Will list every preset available
```

# Config and presets

`ds4led` supports config and presets. On first launch a config file will be created in `~/.config/ds4led/ds4led.json`, containing the default blue dualshock 4 led color.

Every preset is a `key:value` pair, where `key` is the name and `value` is a hex code of a color.