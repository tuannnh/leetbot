import pyautogui
import requests
from PIL import Image
import pytesseract

from config import CONSOLE_ENABLE
from pynput import keyboard
from bot import Bot


def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    text = extract_text_from_image("screenshot.png")
    answer = bot.ask_question(text)
    if not CONSOLE_ENABLE:
        send_message(answer)
    else:
        print(answer)


def send_message(answer):
    # url = "http://localhost:8333/api/answers"
    url = "http://10.1.1.99:11129/api/answers"
    payload = {
        "answer": answer
    }
    # Sending a POST request with json payload
    response = requests.post(url, json=payload)
    # Checking the response status code
    if response.status_code == 200:
        print('POST request successful')
        print('Response:', response.json())
    else:
        print('POST request failed with status code:', response.status_code)


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


# Initialize chatbot
bot = Bot()

print('Listening keyboard events...')


# Set up the keyboard listener for the backtick (`) key
def on_press(key):
    try:
        # print('Key pressed: {0}'.format(key))
        if key == keyboard.Key.alt_l:
            # if key.char == '`':
            take_screenshot()
    except AttributeError:
        pass


# Start the mouse and keyboard listeners
keyboard_listener = keyboard.Listener(on_press=on_press)

keyboard_listener.start()

# Keep the script running
keyboard_listener.join()
