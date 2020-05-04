from run_process import run_process

def run():
    return_code_rm_dist = run_process(["rm -rf - i dist/"])
    if (return_code_rm_dist != 0):
        