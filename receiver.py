import socket
import keyboard  # Simulates key presses/releases

# Configuration
PORT = 9050
BUFFER_SIZE = 1024

# Normalize incoming key names to match keyboard module expectations
def normalize_key(key):
    key = key.strip().lower()
    key_map = {
        "space": "space",
        "enter": "enter",
        "escape": "esc",
        "shift": "shift",
        "ctrl": "ctrl",
        "alt": "alt",
        "leftarrow": "left",
        "rightarrow": "right",
        "uparrow": "up",
        "downarrow": "down"
        # Add more mappings if needed
    }
    return key_map.get(key, key)  # fallback to lowercase key

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

print(f"Listening for UDP messages on port {PORT}...")

# Main loop
while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = data.decode('utf-8').strip()
        print(f"Received from {addr[0]}: {message}")

        if message.startswith("KeyDown:"):
            raw_key = message.split(":")[1]
            key = normalize_key(raw_key)
            keyboard.press(key)
            #print(f"Pressed key: {key}")

        elif message.startswith("KeyUp:"):
            raw_key = message.split(":")[1]
            key = normalize_key(raw_key)
            keyboard.release(key)
            #print(f"Released key: {key}")

    except Exception as e:
        print(f"Error: {e}")
