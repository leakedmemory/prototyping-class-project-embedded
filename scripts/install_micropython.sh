#!/usr/bin/env bash

FILE="micropython.uf2"

if [ -f "$FILE" ]; then
    cp $FILE "/media/$USER/RPI-RP2"
else
    read -p "MicroPython file not found. Do you want to download it? [Y/n] " choice
    choice=${choice:-Y}
    case "$choice" in
    [Yy]*)
        ./scripts/download_micropython.sh
        ;;
    *)
        echo "You chose to not download MicroPython. Exiting..."
        ;;
    esac
fi
