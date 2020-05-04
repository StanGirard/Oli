import platform
from macos import macos

def main():
    platform_name = platform.system()
    if platform_name == "Darwin":
        macos.run()
        





if __name__ == "__main__":
    main()