import subprocess
from oli.lib.command import bcolors
import sys

def run_process(command_execute):
    process = subprocess.Popen(command_execute, 
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True,
                           universal_newlines=True)
    
    while True:
        out = process.stdout.read(1)
        if out == '' and process.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
    return process.poll()


def run_process_no_log(command_execute):
    process = subprocess.Popen(command_execute, 
                           stdout=subprocess.PIPE,
                           shell=True,
                           universal_newlines=True)
    return_code_script = None
    while True:
        return_code = process.poll()
        if return_code is not None:
            return_code_script = return_code
            break
    return return_code_script
