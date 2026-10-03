# DS4LED

[![Crafted by Human](https://madebyhuman.iamjarl.com/badges/crafted-white.svg)](https://madebyhuman.iamjarl.com)

A little cli/gui app for **linux** to control LED color on Dualshock 4.

# Installation

# Setup

To use this app without `sudo`, you need to:
1. Create a udev rule like this:
   `KERNEL=="js*", SUBSYSTEM=="input", ATTRS{idVendor}=="YOUR_VENDOR_ID", ATTRS{idProduct}=="YOUR_PRODUCT_ID", GROUP="ds4led", MODE="0660", TAG+="uaccess"`
   and add your user to "ds4led" group,
2. Add your user to "input" group.

# Usage