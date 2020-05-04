from . import run_process

def run():
    return run_process.run_process(['/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'])