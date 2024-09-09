import pyautogui
import keyboard
import requests
from PIL import Image
import pytesseract
import openai
import config
from config import console_enable, OPEN_API_KEY


class Chatbot:
    def __init__(self):
        self.context = [{"role": "system",
                         "content": "Please answer the questions shortly, no need to explain. Ignore the rest of the text that seems meaningless."}]

    def ask_question(self, question):
        answer, self.context = chat_with_gpt(question, self.context)
        return answer


def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    text = extract_text_from_image("screenshot.png")
    answer = bot.ask_question(text)
    if not console_enable:
        send_message(answer)
    else:
        print(answer)


def send_message(answer):
    url = "http://10.1.1.99:11129/api/answers"
    payload = {
        "answer": f"{answer}"
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


def chat_with_gpt(prompt, context=[]):
    context.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=context
    )
    answer = response.choices[0].message.content
    context.append({"role": "assistant", "content": answer})
    return answer, context


# OpenAI API key
openai.api_key = config.OPEN_API_KEY

# Initialize chatbot
bot = Chatbot()

# Set up the keyboard shortcut (e.g., Ctrl+Shift+S)
# Set the hotkey as backtick (`)
keyboard.add_hotkey("`", take_screenshot)

# Keep the script running
print("Press '`' to take a screenshot and get answers.")
keyboard.wait("esc")  # Press "esc" to exit the script
