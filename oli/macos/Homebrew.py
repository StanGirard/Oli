from .run_process import run_process

def run():
    return run_process(['/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'])