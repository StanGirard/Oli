from oli.lib.linux_process import run_process, run_process_no_log

def run():
    if run_process(['sh -c "$(curl -Ss https://my-netdata.io/kickstart.sh)"']) == 0:
        return 0
    else:
        return 1