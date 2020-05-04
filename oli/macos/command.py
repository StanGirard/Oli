import importlib
def installation_finished():
        input_user = str(input("Would you like to install something else ? Default yes (y/n) ") or "y")
        if input_user.lower().startswith('y'):
            return 0
        else:
            return 1
            


def run_input(switch, value):
    string_value = switch.get(value, "Invalid Value")
    if string_value != 'Invalid Value':
        mymodule = importlib.import_module("." + string_value,  package=__package__)
        print(mymodule)
        return_code = mymodule.run()
        if return_code is 0:
            print("Command Successfull")
            
        else:
            print("An error occured during the execution")
            print("Please check the logs to see what was the cause and run the command again")
        return installation_finished()
    print("Invalid Value")
    return 0


def check_input():
    """Checks the type of the input and keeps asking if not an int """
    
    value = input("What would you like to install ? ")
    while not value.isdigit():
        value = input("What would you like to install ? (A number please) ")
    return int(value)

    

def print_choice(switcher_value):
    """Prints all the available choices"""
    print("----------------------")
    
    for key in switcher_value:
        print(str(key) + " - " + str(switcher_value[key]))

    print("----------------------")
