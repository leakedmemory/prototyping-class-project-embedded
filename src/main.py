import network
import urequests
import time
from machine import Pin, reset
import secrets

red_led = Pin(0, Pin.OUT)
green_led = Pin(28, Pin.OUT)

PING_INTERVAL_IN_MS = 900


def connect_wifi_led_action() -> None:
    green_led.on()
    red_led.off()
    time.sleep(0.2)
    green_led.off()
    red_led.on()
    time.sleep(0.2)
    green_led.on()
    red_led.off()
    time.sleep(0.2)
    green_led.off()
    red_led.on()
    time.sleep(0.2)
    green_led.on()
    time.sleep(0.4)
    green_led.off()
    red_led.off()
    time.sleep(0.3)


def connect_wifi() -> network.WLAN:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

    attempt = 0
    while not wlan.isconnected():
        print(f"Connecting to Wi-Fi... Attempt {attempt + 1}")
        connect_wifi_led_action()
        attempt += 1

        if attempt >= 10:
            print("Failed to connect to Wi-Fi")
            red_led.on()
            time.sleep(3)
            red_led.off()
            attempt = 0

    print("Connected to Wi-Fi")
    green_led.on()
    time.sleep(2)
    green_led.off()

    return wlan


def make_post_request(url: str) -> bool:
    try:
        print(f"Making request...")
        response = urequests.post(url)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error making request: {e}")
        return False


def ensure_wifi_connected(wlan: network.WLAN) -> network.WLAN:
    if wlan is None or not wlan.isconnected():
        return connect_wifi()
    return wlan


def main() -> None:
    wlan = None
    last_request_time = 0

    while True:
        current_time = time.ticks_ms()

        wlan = ensure_wifi_connected(wlan)

        if time.ticks_diff(current_time, last_request_time) >= PING_INTERVAL_IN_MS:
            url = f"https://prototyping-class-webapp.fly.dev/pet/ping?leash_id={secrets.LEASH_ID}"

            if make_post_request(url):
                green_led.on()
                red_led.off()
            else:
                green_led.off()
                red_led.on()

            last_request_time = current_time

        # delay to prevent busy-waiting
        time.sleep(0.2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"A critical error has occured: {e}")
        print("Resetting device...")
        reset()
