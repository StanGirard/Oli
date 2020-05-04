import importlib
from . import command

switcher = {
        1: "Homebrew",
        2: "Oh-my-zsh"
    }

def run():
    """Main Function"""
    
    print("You are running MacOS")
    command.print_choice(switcher)
    value = command.check_input()
    exit = command.run_input(switcher, value)
    if exit == 0:
        run()
    else: 
        quit()
        
    
    
        


if __name__ == "__main__":
    run()