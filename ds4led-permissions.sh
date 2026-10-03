#!/bin/sh

for led in /sys/class/leds/input*:red \
           /sys/class/leds/input*:green \
           /sys/class/leds/input*:blue
do
    [ -e "$led/brightness" ] || continue

    chgrp ds4led "$led/brightness"
    chmod 0660 "$led/brightness"
done
