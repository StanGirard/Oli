from oli.lib.linux_process import run_process

def run():
    #sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /home/stan/fahclient_7.4.4_amd64.deb
    
    
    if run_process("sudo mkdir -p /run/folding") == 0:
        print("YEAH")
        if run_process("sudo wget -N https://download.foldingathome.org/releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4_amd64.deb -P /run/folding/") == 0:
            return 0
    return 1
    # FAHClient
