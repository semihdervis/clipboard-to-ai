import google.generativeai as genai
from dotenv import load_dotenv
import os
import pyperclip
import keyboard
import pyperclip

# Load the GEMINI API key from the environment
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def process_selected_text():
    """
    Fetches text from the clipboard, sends it to the GEMINI API, 
    and places the result back into the clipboard.
    """
    try:
        # Get selected text from the clipboard
        selected_text = pyperclip.paste()
        if not selected_text.strip():
            print("No text selected or clipboard is empty.")
            return

        # Send text to GEMINI for processing
        response = model.generate_content(selected_text)

        # Place the generated content back in the clipboard
        pyperclip.copy(response.text)
        print("Response from GEMINI copied to clipboard:", response.text)

    except Exception as e:
        print("An error occurred:", e)

# Bind the key combination to trigger the function
keyboard.add_hotkey("ctrl+shift+l", process_selected_text)

print("Program is running. Select text and press Ctrl+Alt+G.")

# Keep the program running
keyboard.wait("ctrl+q")
