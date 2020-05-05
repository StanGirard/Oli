import importlib

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def installation_finished():
        input_user = str(input(bcolors.OKBLUE +"\nWould you like to install something else ?" +  bcolors.ENDC + " Default yes (y/n) " ) or "y")
        if input_user.lower().startswith('y'):
            return 0
        else:
            return 1
            


def run_input(package, switch, value):
    string_value = switch.get(value, "Invalid Value")
    if string_value != 'Invalid Value':
        mymodule = importlib.import_module("oli." + package + "." + string_value)
        return_code = mymodule.run()
        if return_code == 0:
            print(bcolors.OKGREEN + "Command Successfull" + bcolors.ENDC )
            
        else:
            print(bcolors.FAIL + "An error occured during the execution" + bcolors.ENDC)
            print("Please check the logs to see what was the cause and run the command again")
        return installation_finished()
    print("Invalid Value")
    return 0


def check_input():
    """Checks the type of the input and keeps asking if not an int """
    
    value = input(bcolors.OKBLUE + "What would you like to install ? " + bcolors.ENDC)
    while not value.isdigit():
        value = input(bcolors.OKBLUE +"What would you like to install ? (A number please) "+ bcolors.ENDC)
    return int(value)

    

def print_choice(switcher_value):
    """Prints all the available choices"""
    print("----------------------")
    for key in switcher_value:
        print(str(key) + " - " + str(switcher_value[key]))

    print("----------------------")

