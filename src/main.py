import keyboard

def main():
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == keyboard.KEY_DOWN:
            print(f"Key '{key_event.name}' pressed")
main()