from ..lib import command

switcher = {
        1: {"name":"Homebrew", "file": "Homebrew", "description":"Home Brew Installer"},
        2: {"name":"Oh-my-zsh", "file": "Oh-my-zsh", "description":"Oh-my-zsh"},
        3: {"name":"Xcode", "file": "XCode", "description":"Xcode"},
        4: {"name":"Development-setup", "file": "Development-setup", "description":"Dev App"},
        5: {"name":"Netdata", "file": "Netdata", "description":"Netdata"},
    }

def run_macos():
    """Main Function"""
    
    print("You are running MacOS")
    command.print_choice(switcher)
    value = command.check_input()
    exit_value = command.run_input("macos", switcher, value)
    if exit_value == 0:
        run_macos()
    else: 
        quit()