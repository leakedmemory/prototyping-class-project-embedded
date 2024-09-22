# Electronic Leash (Embedded)

This is the embedded system component of the Electronic Leash project, designed
to run on a microcontroller with a Wi-Fi module (e.g., Raspberry Pi Pico W) with
MicroPython. It periodically sends ping requests to the server to update the
pet's status.

Obs.: you can find the web part
[here](https://github.com/leakedmemory/prototyping-class-project).

## Getting Started

### Prerequisites

- Running on a Linux machine
- MicroPython-compatible board with a Wi-Fi module (e.g., Raspberry Pi Pico W)
- Python 3.10 or higher
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [MicroPython](https://duckduckgo.com/?q=micropython&ia=web)

You can download MicroPython using `make download` and, if you're using a
Raspberry Pi, install it with `make install`. Keep in mind that you must connect
the board to the computer while holding the BOOTSEL button and then run the
install command.

### Developing

- Create a `src/secrets.py` file and set up your environment variables based on
  the [src/secrets.py.example](src/secrets.py.example) file
- Install the dependencies

```bash
pipenv install
```

- Enter `pipenv shell`
- Running the project

```bash
make run
```

- Deploying to the board

```bash
make push
```

## Main Script Functionality

The `src/main.py` script does the following:

1. Connects to Wi-Fi
2. Periodically sends ping requests to the server
3. Updates LED status based on successful/failed pings
4. Handles Wi-Fi disconnections and reconnections
5. Resets the device in case of critical errors

## Hardware

- The script uses two LEDs:
  - Green LED on Pin 28
  - Red LED on Pin 0

Adjust these pin numbers in the script if your hardware setup is different.

## Built With

- [MicroPython](https://micropython.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.

## Disclaimers

- This was a project built for my prototyping class at university
- It's my first project with this stack, so keep in mind that a lot of things
  are most likely made in an unusual way or details.
