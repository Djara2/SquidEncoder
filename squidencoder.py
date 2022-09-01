import pyclip
import sys
import os
import platform
from encoder import encode
from decoder import decode
from lexicon import reserved_words_dictionary, get_reversed_dictionary
VERNO = "22.09.01"

def print_header(version):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(f"Squid Language Interpreter v{version}\n")


reversed_dict = get_reversed_dictionary(reserved_words_dictionary)
mode = None
command_line = False

# get arguments from command line
print_header(VERNO)
if len(sys.argv) >= 3:
    if mode != "exit":
        mode = sys.argv[1]
    else:
        exit()
    start = sys.argv[2]
    if "termux" in sys.argv:
        termux = True
    else:
        termux = False
else:
    if len(sys.argv) == 2:
        if mode != "exit":
            mode = sys.argv[1]
        else:
            exit()
    else:
        print("Please select a mode")
        print("\n1. Encode")
        print("2. Decode")
        print("3. Lookup")
        mode = input("\n> ")
        if mode == "1":
            mode = "encode"
        elif mode == "2":
            mode = "decode"
        elif mode == "3":
            mode = "lookup"
        else:
            mode = "unrecognized"
        if mode == "exit":
            exit()
    
    if mode in ["encode", "Encode", "ENCODE", "1", "en", "EN," "En"]:
        print_header(VERNO)
        print(f"In {mode} mode")
        start = input("\nEncode: ")
    elif mode in ["decode", "Denode", "DECODE", "2", "de", "DE," "De"]:
        print_header(VERNO)
        print(f"In {mode} mode")
        start = input("\nDecode: ")
    elif mode in ["lookup", "Lookup", "LOOKUP", "lk", "Lk", "LK", "3", "l", "L"]:
        print_header(VERNO)
        print(f"In {mode} mode")
        start = input("\nLookup: ")
    else:
        print("Mode input was unrecognized.")



exit_keywords = set(["exit", "quit", "stop", "Exit", "Quit", "Stop", "EXIT", "QUIT", "STOP"])

while True:
    print_header(VERNO)
    
    if mode == "exit":
        exit()
    
    # encode
    elif mode in ["encode", "Encode", "ENCODE", "1", "en", "EN," "En"]:
        # if argument not already predefined from CLI
        if start == "":
            start = input("Encode: ")
        encode(start, reserved_words_dictionary)
        mode = ""
        start = ""
        halt = input("\nPress ENTER to terminate ")
    
    # decode
    elif mode in ["decode", "Decode", "DECODE", "2", "de", "DE," "De"]:
        # if argument not already predefined from CLI
        if start == "":
            start = input("Decode: ")
        decode(start, reversed_dict)
        mode = ""
        start = ""
        halt = input("\nPress ENTER to terminate ")

    # lookup
    elif mode in ["lookup", "Lookup", "LOOKUP", "lk", "Lk", "LK", "3", "l", "L"]:
        # if argument not already predefined from CLI
        if start == "":
            start = input("Lookup: ")
        lookup(start, reserved_words_dictionary)
        mode = ""
        start = ""
        halt = input("\nPress ENTER to terminate ")
    elif mode in exit_keywords:
        exit()
    
    else:
        print("Please select a mode")
        print("\n1. Encode")
        print("2. Decode")
        print("3. Lookup")
        mode = input("\n> ")
        print_header(VERNO)
        if mode == "1":
            mode = "encode"
        elif mode == "2":
            mode = "decode"
        elif mode == "3":
            mode == "lookup"
        else:
            mode == "unrecognized" 
        print(f"In {mode} mode\n")
        start = input("> ")
