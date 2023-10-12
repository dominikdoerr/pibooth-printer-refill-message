# pibooth-printer-refill-message

`pibooth-printer-refill-message` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application. It shows a message screen when the number of maximum allowed prints has been reached, prompting the refill of print material.

After confirmation on the refill page the counter of printed pages is reset.

## Install

This plugin is not (yet) available on PyPI.

You can install it manually by downloading this repository and then install it from the local path with `pip3 install /path/to/the/downloaded/pibooth-printer-refill-message`.

## Configuration

The following configuration options will be added to the pibooth configuration file after the first pibooth restart. The values can be changed by editing the configuration file directly or open it with the command `pibooth --config`.

```
[PRINTER REFILL MESSAGE]
# Text to display when max_pages is reached
text_refill = Please refill printer paper and/or cartridge(s).

# Confirmation button for the refill
text_done = Done?

# Path to the image with the refill instructions
image_path = assets/refill_instructions.png
```

To display the refill message screen at the right times, the configuration value for `max_pages` should be set to the paper amount contained in the printer's tray.

If you do not use pibooth with a connected printer, you can deactivate the plugin through pibooth's menu.

## License

This plugin is licensed under the [GPL-3.0 license](LICENSE).

## Credits

Many thanks to [Ulmerju](https://github.com/Ulmerju), who kindly [provided the code base](https://github.com/pibooth/pibooth/issues/414).