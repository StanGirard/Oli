from .run_process import run_process

def run():
    return run_process(['sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'])