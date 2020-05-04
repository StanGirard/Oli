import platform
from oli.macos import macos
import signal
import sys

def signal_handler(signal, frame):
    print("\nGracefully exiting")
    sys.exit(0)

def main():
    platform_name = platform.system()
    if platform_name == "Darwin":
        macos.run()
        

signal.signal(signal.SIGINT, signal_handler)



if __name__ == "__main__":
    
    main()