from pynput.mouse import Listener
from datetime import datetime


def on_click(x, y, button, pressed):
    if pressed:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(f'Click detected at ({x}, {y}) - {button} - {current_time}')


def start_bot_detection():
    with Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == '__main__':
    start_bot_detection()
