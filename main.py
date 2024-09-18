import requests
from PIL import ImageGrab
import keyboard
from config import CONSOLE_ENABLE
from bot import Bot
import subprocess
from pynput import keyboard


def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    text = extract_text_from_image("screenshot.png")
    answer = bot.ask_question(text) if text else 'No answer detected'

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
    try:
        result = subprocess.run(['tesseract', image_path, 'stdout'], capture_output=True, text=True, check=True)
        extracted_text = result.stdout  # The extracted text is stored in the stdout
        return extracted_text

        # You can now use the extracted_text for further processing
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Tesseract: {e}")
    # text = pytesseract.image_to_string(image)
    # text = unidecode(text)
    return None


# Initialize chatbot
bot = Bot()

print('Listening keyboard events...')


def on_press(key):
    try:
        if key == keyboard.Key.alt_r:
            take_screenshot()
    except AttributeError:
        pass


keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()
