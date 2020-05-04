import platform
import signal
import sys
from oli.macos import mac

def signal_handler(signal, frame):
    print("\nGracefully exiting")
    sys.exit(0)

def run_as_command():
    platform_name = platform.system()
    if platform_name == "Darwin":
        mac.run_macos()
        

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    run_as_command()

