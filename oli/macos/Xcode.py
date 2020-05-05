from .run_process import run_process

def run():
    return run_process(['xcode-select --install'])