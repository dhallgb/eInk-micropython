
# MicroPython e-Ink library for Waveshare 4.3inch display.

This is a simple library for displaying information on a Waveshare 4.3 e-ink display from a device running Micropython. These are boards like the Pyboard, WiPy, or those based around the ESP8266 chip such as the Adafruit Feather Huzzah. As an alternative if you are running this on a full CPython implementation see https://github.com/yy502/ePaperDisplay, as that library has many more functions.

[![Donate with Open Source Citizen](http://www.opensourcecitizen.org/badge?url=github.com/dhallgb/eInk-micropython)](http://www.opensourcecitizen.org/project?url=github.com/dhallgb/eInk-micropython)

If you found this library useful, donate some CPU cycles to its
development efforts by clicking above. Thank you! 😇

### Conversion
It takes as its base a pure conversion from the Waveshare code. I used a few things to start the conversion from C code into Python:

- a utility called cpp2python from https://github.com/hlamer/cpp2python
- a demo script h2py.py in the Python demo/scripts directory to convert the header file
- seasnake from the excellent BeeWare project at http://pybee.org/, but now abandoned - BeeWare itself is still very alive!
- ctopy from http://www.catb.org/~esr/ctopy/

...but mostly just hand-cranked the Python code whilst browsing the C routines.

### Adaption to MicroPython and embedded devices
The original (and derivations) tended to use excessive string concatenation which consumes memory space. In the constrained memory environment of the embedded systems on which MicroPython runs, memory is at a premium so I adapted the library for the following:

- no extraneous operations, just the raw commands
- constant binary strings for complete commands (eg. clear, update) where possible so not to use string concatenation
- precalculated parity bytes
