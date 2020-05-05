from .run_process import run_process, run_process_no_log
from oli.lib.command import bcolors
from .Homebrew import run as hbrun

def run_brew(name, command):
    if str(input("\nWould you like to install "+ name +" ? Default yes (y/n) " ) or "y").lower().startswith('y'):
        print(bcolors.OKBLUE + "Installing " + name + bcolors.ENDC)
        exit_code = run_process(["brew " + command])
        if exit_code != 0:
            print(bcolors.FAIL + "Error in the installation of " + name  + ", exit code: " + exit_code + bcolors.ENDC)
            quit()
        else:
            print(bcolors.OKGREEN + "Installation Successfull" + bcolors.ENDC)
    else: 
        print("Ok, not installing " + name)

def run():
    print(bcolors.HEADER + " Checking" + bcolors.ENDC)
    exit_code = run_process_no_log(['which brew'])
    
    if exit_code != 0:
        input_user = str(input(bcolors.OKBLUE +"\nWould you like to install brew ?" +  bcolors.ENDC + " Default yes (y/n) " ) or "y")
        if input_user.lower().startswith('y'):
            print(bcolors.OKBLUE + "Installing Homebrew" + bcolors.ENDC)
            exit_code = hbrun()
            if not exit_code:
                print(bcolors.FAIL + "Error in the installation of Homebrew" + bcolors.ENDC)
                return 1
    else:
        print(bcolors.OKGREEN + "Updating Brew" + bcolors.ENDC)
        exit_code = run_process(["brew update"])
        if exit_code != 0:
            return 1
    run_brew("git", "install git")
    run_brew("Google Chrome", "cask install google-chrome")
    run_brew("Google Chrome Canary", "cask install google-chrome-canary")
    run_brew("Firefox", "cask install firefox")
    run_brew("Firefox Developer Edition", "cask install firefox-developer-edition")
    run_brew("Visual Studio Code", "cask install visual-studio-code")
    run_brew("Visual Studio Code Insiders", "cask install visual-studio-code-insiders")
    run_brew("Intellij", "cask install intellij-idea")
    run_brew("Eclipse Java", "cask install eclipse-java")
    run_brew("Postman", "cask install postman")
    run_brew("Docker", "cask install docker")
    run_brew("Spectacle", "cask install spectacle")
    run_brew("Tree", " install tree")




# brew install git
# brew cask install google-chrome
# brew cask install google-chrome-canary
# brew cask install firefox
# brew cask install firefox-developer-edition
# brew cask install visual-studio-code
# brew cask install visual-studio-code-insiders
# brew cask install intellij-idea
# brew cask install eclipse-java
# brew cask install postman
# brew cask install docker
# brew cask install spectacle
# brew install tree