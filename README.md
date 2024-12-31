# Gemini Test Project

This project demonstrates how to use the GEMINI API to process text from the clipboard and place the result back into the clipboard.

## Setup

1. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

2. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project directory with the following content:
        ```properties
        GEMINI_API_KEY=your_api_key_here
        ```

## Usage

1. **Run the script:**
    ```sh
    python clipboard.py
    ```

2. **How to use:**
    - Select the text you want to process.
    - Press `Ctrl+Shift+L` to send the selected text to the GEMINI API.
    - The processed text will be copied back to your clipboard.
    - Press `Ctrl+Q` to quit the program.

## Notes

- Ensure you have your GEMINI API key set in the `.env` file.
- The script will print the response from GEMINI to the console and copy it to the clipboard.
