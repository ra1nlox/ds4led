import subprocess

import click
from vcolorpicker import getColor, hex2rgb

red_path = "/sys/class/leds/%DEVICE%:red/brightness"
green_path = "/sys/class/leds/%DEVICE%:green/brightness"
blue_path = "/sys/class/leds/%DEVICE%:blue/brightness"

path_templates = (red_path, green_path, blue_path)


def get_device_name() -> str:
    device_info = subprocess.run(
        "udevadm info -a -p $(udevadm info -q path -n /dev/input/js0) | grep -oE 'input[0-9]+' | head -n1",
        check=True,
        capture_output=True,
        text=True,
        shell=True,
    )
    device = device_info.stdout.strip()

    return device


def write_colors_in(paths: tuple[str], colors: tuple[int, int, int]) -> None:
    for i, path in enumerate(paths):
        with open(path, "w") as f:
            # using `i` here because len(paths) = len(colors), and they both are in the same order
            f.write(f"{colors[i]}")


@click.command()
@click.option("-h", "--hex", "hex", required=False, help="Specify HEX RGB value")
@click.argument("red_green_blue", required=False, nargs=3)
def main(hex: str, red_green_blue: tuple[str, str, str]):
    device = get_device_name()

    if not device:
        print("The gamepad is not connected.")
        return 1

    led_paths = tuple(path.replace("%DEVICE%", device) for path in path_templates)

    if hex:
        expected_length = 6
        if "#" in hex:
            expected_length = 7

        if len(hex) < expected_length:
            print("Invalid format (#FFFFFF or FFFFFF)")
            return 1

        colors = hex2rgb(hex)
        write_colors_in(led_paths, colors)

    elif red_green_blue:
        red_green_blue = [int(c) for c in red_green_blue]
        for c in red_green_blue:
            if c < 0 or c > 255:
                print("Invalid value (0 < c < 255)")
        write_colors_in(led_paths, red_green_blue)

    else:
        rgb_colors = getColor()
        colors = [int(c) for c in rgb_colors]
        write_colors_in(led_paths, colors)

    return 0


if __name__ == "__main__":
    main()
