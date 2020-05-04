def check_input():
    value = input("What would you like to install ? ")
    while not value.isdigit():
        value = input("What would you like to install ? (A number please) ")
    return int(value)

def print_choice():
    print("----------------------")
    print("1 - Homebrew ")
    print("----------------------")


def run():
    print("You are running MacOS")
    print_choice()
    value = check_input()
        
    
    
        


if __name__ == "__main__":
    run()