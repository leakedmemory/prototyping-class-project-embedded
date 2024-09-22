#!/usr/bin/env bash

FILE="micropython.uf2"

if [ ! -f $FILE ]; then
    echo "Downloading MicroPython...\n"
    wget -c --show-progress --output-document=$FILE \
        https://micropython.org/resources/firmware/RPI_PICO_W-20240222-v1.22.2.uf2
    echo "MicroPython Download Complete"
else
    echo "$FILE already exists"
fi
