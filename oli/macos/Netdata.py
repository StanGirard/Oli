from oli.lib.linux_process import run_process, run_process_no_log
from oli.lib.command import bcolors

def run():

    if run_process(['brew install netdata']) == 0:
       
        if run_process(['brew services start netdata']) == 0:
            print(bcolors.OKGREEN + "You can access Netdata at http://localhost:19999" + bcolors.OKGREEN)
            return 0
        else :
            return 1
    else: 
        return 1