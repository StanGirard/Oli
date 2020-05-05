from oli.lib.linux_process import run_process, run_process_no_log

def run():
    if run_process(["bash <(curl -Ss https://my-netdata.io/kickstart.sh"]) == 0:
        print("You can now access Netdata at http://localhost:19999")
        return 0
    else:
        return 1