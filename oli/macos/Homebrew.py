import subprocess

def run():

    process = subprocess.Popen(['/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'], 
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
                print(output.strip())
            break
    return return_code_script