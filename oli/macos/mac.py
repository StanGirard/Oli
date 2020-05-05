import importlib
from . import command

switcher = {
        1: "Homebrew",
        2: "Oh-my-zsh",
        3: "Xcode",
        4: "Development-setup"
    }

def run_macos():
    """Main Function"""
    
    print("You are running MacOS")
    command.print_choice(switcher)
    value = command.check_input()
    exit_value = command.run_input(switcher, value)
    if exit_value == 0:
        run_macos()
    else: 
        quit()