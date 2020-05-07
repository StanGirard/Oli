from oli.lib.linux_process import run_process

def generateConfig():
    config = "<config> <user value='Anonymous'><team value='263124'><passkey value=''><smp value='true'><gpu value='false'><power value='full'></config>"
    return config

def run():
    #sudo DEBIAN_FRONTEND=noninteractive apt-get install -y /home/stan/fahclient_7.4.4_amd64.deb
    
    
    if run_process("sudo mkdir -p /run/folding") == 0:
        print("YEAH")
        if run_process("sudo wget -N https://download.foldingathome.org/releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4_amd64.deb -P /run/folding/") == 0:
            print("HAHAHAHAHAH")
            if run_process("sudo mkdir -p /etc/fahclient && sudo chown $USER:$USER /etc/fahclient/") == 0:
                print("HEHEHEHEHEHEH")
                
                if run_process("touch /etc/fahclient/config.xml") == 0:
                    print("CHMOD")
                    if run_process("chmod u+w /etc/fahclient/config.xml") == 0:
                        print("WRITE")
                        with open("/etc/fahclient/config.xml", 'w') as configFile:
                            configFile.write(generateConfig())
    return 1
    # FAHClient
