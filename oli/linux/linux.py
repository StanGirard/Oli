from ..lib import command

switcher = {
        1: "Netdata"
    }

def run_linux():
    """Main Function"""
    
    print("You are running a Linux Based Distribution")
    command.print_choice(switcher)
    value = command.check_input()
    exit_value = command.run_input("linux", switcher, value)
    if exit_value == 0:
        run_linux()
    else: 
        quit()