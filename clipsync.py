import pyperclip
import time
import pyautogui
import pygetwindow as gw

last_clipboard = ""

# Replace with the exact title of your target window
TARGET_WINDOW_TITLE = "Claude"

def focus_window(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(0.5)  # wait for window to come into focus
        return True
    return False

print("Monitoring clipboard... Press Ctrl+C to stop.")

while True:
    try:
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard:
            last_clipboard = current_clipboard
            print(f"New clipboard content: {current_clipboard}")

            if focus_window(TARGET_WINDOW_TITLE):
                pyautogui.hotkey('ctrl', 'v')  # paste
                time.sleep(0.2)
                pyautogui.press('enter')       # press Enter
            else:
                print(f"Window '{TARGET_WINDOW_TITLE}' not found.")

        time.sleep(1.5)  # wait before checking clipboard again

    except KeyboardInterrupt:
        print("\nScript stopped by user.")
        break
