import pyfiglet
import socket
import sys
from datetime import datetime

try:
    # Create an informative ASCII banner
    ascii_banner = pyfiglet.figlet_format("Port Scanner", font="slant")
    print(ascii_banner)

except ModuleNotFoundError:
    print("Error: 'pyfiglet' module not found. Please install it using 'pip install pyfiglet'.")
    sys.exit(1)

target = input("Enter Target IP: ")

# Banner with clear information and spacing
print("=" * 50)
print("Scanning Target:", target)
print("Scanning Started at:", datetime.now())
print("=" * 50)

try:
    for port in range(1, 65536):  # Include port 65535
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Set a timeout for faster scanning
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open.")

except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(1)

except socket.error as err:
    print(f"\nError: {err}")
    print("   * Host not responding, or permission denied.")
    sys.exit(1)

print("\nScan completed.")
