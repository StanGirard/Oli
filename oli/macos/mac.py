import importlib
from oli.macos.command import print_choice, check_input, run_input

switcher = {
        1: "Homebrew"
    }

def run():
    """Main Function"""
    
    print("You are running MacOS")
    print_choice(switcher)
    value = check_input()
    exit = run_input(switcher, value)
    if exit == 0:
        run()
    else: 
        quit()
        
    
    
        


if __name__ == "__main__":
    run()