from oli.lib.linux_process import run_process
import os

def generateConfig(name, team, gpu):
    config = '<config> <user value="' + str(name) + '"/><team value="' + str(team) + '"/><passkey value=""/><smp value="true"/><gpu value="'+ str(gpu) + '"/><power value="full"/></config>'
    return config

def run():
    #sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /home/stan/fahclient_7.4.4_amd64.deb
    name = str(input("\nWhat would you like your name to be ? Default Anonymous " ) or "Anonymous")
    team = int(input("\nWhat team would you like to join (int) ? Default 263124 ") or "263124")
    gpu = "false"
    if str(input("Would you like to use your gpu ? Default No (y/n)" ) or "No").lower().startswith("y"):
        gpu = "true"
    if run_process("sudo mkdir -p ~/folding") == 0:
        if run_process("sudo wget -N https://download.foldingathome.org/releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4-64bit-release.tar.bz2 -P ~/folding/") == 0:
            if run_process("sudo chown $USER:$USER ~/folding/") == 0:
                if run_process("tar jxf ~/folding/fahclient_7.4.4-64bit-release.tar.bz2 --strip-components=1 -C ~/folding/ ") == 0:
                    with open(os.path.expanduser("~/folding/config.xml"), 'w') as configFile:
                        configFile.write(generateConfig(name, team, gpu))
                        return 0
                            
    return 1
    # FAHClient
