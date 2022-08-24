import os
import platform
import file_tools as ft

has_git = input("Is git installed on your system? [y/n]: ")

if has_git == "y":
    print("READ ME: please run the update.bat file to update on Windows and the update.sh file to update on Linux/Unix platforms")
else:
    print("You do not have git installed, which you need to update the SquidEncoder application. Please install git.\n")
    if platform.system() == "Windows":
        has_winget = input("Do you have winget installed? [y/n]: ")
        if has_winget == "y":
            os.system("winget install git.git")
        else:
            print("\nPlease install winget from the link here → https://www.microsoft.com/p/app-installer/9nblggh4nns1#activetab=pivot:overviewtab ーthen re-run this update application.")
            exit()
    else:
        if platform.system() == "Linux":
            termux = input("Are you on Termux? [y/n]: ")
            if termux == "y":
                os.system("pkg install git")
            else:
                apt = input("Are you on a Debian/Ubuntu based distribution? [y/n]: ")
                if apt == "y":
                    os.system("sudo apt install git")

path = ft.get_path()
path_basename = ft.get_path_basename(path)
stop = len(path) - len(path_basename)
one_dir_down = path[:stop]
if platform.system() == "Windows":
    os.system(f"move file_tools.py {one_dir_down}")
    os.system(f"move squid_encoder_updater.py {one_dir_down}")
else:
    os.system(f"mv file_tools.py {one_dir_down}")
    os.system(f"mv squid_encoder_updater.py {one_dir_down}")

