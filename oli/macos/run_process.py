import subprocess
from .command import bcolors

def run_process(command_execute):
    process = subprocess.Popen(command_execute, 
                           stdout=subprocess.PIPE,
                           shell=True,
                           universal_newlines=True)
    return_code_script = None
    
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            return_code_script = return_code
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(bcolors.WARNING + output.strip() + bcolors.ENDC)
            break
    return return_code_script

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