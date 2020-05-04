import importlib

switcher = {
        1: "Homebrew"
    }

def installation_finished():
        input_user = str(input("Would you like to install something else ? Default yes (y/n) ") or "y")
        if input_user.lower().startswith('y'):
            run()
        else:
            quit()


def run_input(value):
    string_value = switcher.get(value, "Invalid Value")
    if string_value != 'Invalid Value':
        mymodule = importlib.import_module("." + string_value,  package=__package__)
        return_code = mymodule.run()
        if return_code is 0:
            print("Installation Successfull")
            
        else:
            print("An error occured during the installation")
            print("Please check the logs to see what was the cause and run the command again")
        installation_finished()
            




def check_input():
    """Checks the type of the input and keeps asking if not an int """
    
    value = input("What would you like to install ? ")
    while not value.isdigit():
        value = input("What would you like to install ? (A number please) ")
    return int(value)

    

def print_choice():
    """Prints all the available choices"""
    print("----------------------")
    
    for key in switcher:
        print(str(key) + " - " + str(switcher[key]))

    print("----------------------")


def run():
    """Main Function"""

    print("You are running MacOS")
    print_choice()
    value = check_input()
    run_input(value)
        
    
    
        


if __name__ == "__main__":
    run()