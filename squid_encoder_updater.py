import os
import platform
import file_tools as ft
path = ft.get_path()
path_basename = ft.get_path_basename(path)

USER_OS = platform.system()

if  USER_OS == "Windows":
    # setup will move this file (update.py) to the directory below the SquidEncoder directory -- therefore, it can just do rmdir SquidEncoder
    os.system("rmdir /S SquidEncoder")
else:
    os.system("rm -d -r SquidEncoder")

os.system("git clone http://www.github.com/Djara2/SquidEncoder")
