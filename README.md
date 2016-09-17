
# MicroPython e-Ink library for Waveshare 4.3inch display.

This is a simple library for display on a Waveshare 4.3 e-ink device from a system which runs Micropython. These could be the pyboard, wipy, or those based around the ESP8266 device such as the Adafruit Feather Huzzah. It takes as its base a pure conversion from the Waveshare code. I used a few things to start the conversion from C code into Python:
- a utility called cpp2python from https://github.com/hlamer/cpp2python
- a demo script h2py.py in the Python demo/scripts directory to convert the header file
- seasnake from the excellent BeeWare project at http://pybee.org/
- ctopy from http://www.catb.org/~esr/ctopy/

As an alternative see https://github.com/yy502/ePaperDisplay if you are running this on a CPython implementation. Whilst this is NOT a fork of that code, I did read that for some ideas.