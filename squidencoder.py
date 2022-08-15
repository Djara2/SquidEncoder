import pyclip
import sys
import os
VERNO = "1.2"

def print_header(version):
    os.system("cls")
    print(f"Squid Language Interpreter v{version}\n")

reserved_words_dictionary = {
        "him": "kaar",
        "Him": "Kaar",
        "his": "kaar-noder",
        "His": "Kaar-noder",
        "her": "kaal",
        "hers": "kaal-noder",
        "her's": "kaal-noder",
        "Hers": "Kaal-noder",
        "Her's": "Kaal-noder",
        "at": "ref",
        "At": "Ref",
        "know": "kiman",
        "Know": "Kiman",
        "no": "bu",
        "No": "Bu",
        "not": "buun",
        "Not": "Buun",
        "unable": "unfähig-ji",
        "Unable": "Unfähig-ji",
        "but": "ab'an",
        "But": "Ab'an",
        "think": "i-arum",
        "Think": "I-arum",
        "they": "selma",
        "They": "Selma",
        "able": "fähig-ji",
        "Able": "Fähig-ji",
        "how": "shimiko",
        "have": "tez",
        "Have": "Tez",
        "has": "tez",
        "Has": "Tez",
        "Dave": "Dake",
        "dave": "dake",
        "david": "dake",
        "David": "Dake",
        "sam": "kewlaid",
        "Sam": "Kewlaid",
        "roger": "kuma",
        "Roger": "Kuma",
        "alex": "skremus",
        "Alex": "Skremus",
        "this": "malaan",
        "This": "Malaan",
        "also": "akez",
        "has": "maz",
        "Has": "Maz",
        "Also": "Akez",
        "was": "irupost",
        "Was": "Irupost",
        "were": "irupost",
        "Were": "Irupost",
        "How": "Shimiko",
        "can": "fähig-ki",
        "Can": "Fähig-ki",
        "can't": "unfähig-ki",
        "Can't": "Unfähig-ki",
        "cant": "unfähig-ki",
        "Cant": "Unfähig-ki",
        "yes": "haida",
        "Yes": "Haida",
        "yeah": "haida",
        "Yeah": "Haida",
        "right": "migire",
        "Right": "Migire",
        "now": "iman",
        "Now": "Iman",
        "i": "ikii",
        "I": "ikii",
        "you": "kiimu",
        "You": "Kiimu",
        "are": "iru", 
        "Are": "iru",
        "am": "iru",
        "Am": "Iru",
        "I'm": "ikii iru",
        "i'm": "ikii iru",
        "you're": "kiimu iru",
        "You're": "kiimu iru",
        "ur": "kiimu iru",
        "to": "dai",
        "when": "nanzeit",
        "To": "Dai",
        "When": "Nanzeit",
        "Ur": "Kiimu iru",
        "we": "ikii-ikii",
        "We": "Ikii-ikii",
        "of": "noder",
        "Of": "Noder",
        "my": "ikii-noder",
        "My": "Ikii-noder",
        "your": "kiimu-noder",
        "Your": "Kiimu-noder",
        "what": "nan",
        "What": "Nan",
        "left": "hidariz",
        "Left": "Hidariz",
        "from": "ralia",
        "From": "Ralia",
        "in": "ezu",
        "In": "Ezu",
        "into": "ezudai",
        "Into": "Ezudai",
        "around": "um-um",
        "Around": "Um-um",
        "about": "um",
        "About": "Um",
        "use": "ussen",
        "Use": "Ussen",
        "then": "zaalaan",
        "Then": "Zaalaan",
        "the": "zaal",
        "Then": "Zaal",
        "again": "nohec",
        "Again": "Nohec",
        "it": "kotosa",
        "It": "Kotosa",
        "only": "suur",
        "Only": "Suur",
        "be": "iru",
        "Be": "Iru",
        "is": "iru",
        "Is": "Iru",
        "one": "onin",
        "One": "Onin",
        "on": "dau",
        "On": "Dau",
        "our": "ikii-ikii-noder",
        "Our": "Ikii-ikii-noder",
        "that": "dassko",
        "That": "Dassko",
        "all": "uchuu",
        "All": "Uchuu",
        "me": "ikii-san",
        "Me": "Ikii-san",
        "and": "daiduund",
        "And": "Daiduund",
        "onto": "ondai",
        "Onto": "Ondai",
        "why": "foroz",
        "Why": "Foroz"
    }

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

def encode(start, d):
    start = start.split()
    encode = ""
    for word in start:
        if word in reserved_words_dictionary:
            encode += reserved_words_dictionary[word]
            encode += " "
        else:
            x = 0
            while x < len(word):
                char = word[x]
                
            
                if char == "d":
                    if x + 1 < len(word):
                        if word[x+1] == char:
                            encode += "\'Д"
                            x += 1
                        else:
                            encode += "Д"
                    else:
                        encode += "Д"

                
                # ss
                # st
                elif char == "s":
                    if x + 1 < len(word):
                        if word[x+1] == "s":
                            encode += "ß"
                            x += 1
                        elif word[x+1] == "t":
                            encode += "š"
                            x += 1
                        elif word[x+1] == "e":
                            if x + 2 < len(word):
                                if word[x+2] == "e" or word[x+2] == "a":
                                    encode += char
                                else:
                                    encode += "çand"
                                    x += 1
                            else:
                                encode += "çand"
                                x += 1
                        else:
                            encode += char
                    else:
                        encode += char
                elif char == "c":
                    if x + 1 < len(word):
                        if word[x+1] == "e":
                            encode += "kand" 
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += char
                # ea
                # ee
                # er
                # et
                elif char == "e":
                    if x + 1 < len(word):
                        if word[x+1] == "a":
                            encode += "ë"
                            x += 1
                        elif word[x+1] == "e":
                            encode += "ä"
                            x += 1
                        elif word[x+1] == "r":
                            encode += "-ll"
                            x += 1
                        elif word[x+1] == "t":
                            encode += "-ejd"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += char
                elif char == "u":
                    if x + 1 < len(word):
                        if word[x+1] == "a":
                            encode += "ø"
                            x += 1
                        else: 
                            encode += char
                    else:
                        encode += char
                # or
                # ology
                elif char == "o":
                    if x + 1 < len(word):
                        if word[x+1] == "r":
                            encode += "-il"
                            x += 1
                        elif word[x+1] == "o":
                            encode += "\'o"
                            x += 1
                        elif word[x:len(word)] == "logy":
                            encode += "-kyo"
                            x = len(word)
                        else:
                            encode += char
                    else:
                        encode += char

                # ity
                # ium
                # ion
                # ing
                elif char == "i":
                    if x + 1 < len(word):
                        if word[x+1] == "e":
                            encode += "y"
                            x += 1
                        
                        # ing
                        elif word[x+1] == "n":
                            if x + 2 < len(word):
                                if word[x+2] == "g":
                                    encode += "-dzai"
                                    x += 2
                                else:
                                    encode += char
                            else:
                                encode += char
                        
                        # ity
                        elif word[x+1] == "t":
                            if x + 2 < len(word):
                                if word[x+2] == "y":
                                    encode += "ю"
                                    x += 2
                                else:
                                    encode += char
                            else:
                                encode += char
                        # ium
                        elif word[x+1] == "u":
                            if x + 2 < len(word):
                                if word[x+2] == "m":
                                    encode += "ц"
                                    x += 2
                                else:
                                    encode += char
                            else:
                                encode += char
                        # ion
                        elif word[x+1] == "o":
                            if x + 2 < len(word):
                                if word[x+2] == "n":
                                    encode += "ü"
                                    x += 2
                                else:
                                    encode += char
                            else:
                                encode += char
                        else:
                            encode += char
                    else:
                        encode += char

                elif char == "g":
                    if x + 1 < len(word):
                        if word[x+1] == "e":
                            encode += "δ"
                            x += 1
                        elif word[x+1] == "g":
                            encode += "\'g"
                            x += 1
                        else:
                            encode += "g"
                    else:
                        encode += "g"

                elif char == "r":
                    if x + 1 < len(word):
                        if word[x+1] == "y":
                            encode += "ö"
                            x += 1
                        elif word[x+1] == "e":
                            encode += "μ"
                            x += 1
                        elif word[x+1] == "r":
                            encode += "\'r"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += "r"
                
                elif char == "m":
                    if x + 1 < len(word):
                        if word[x+1] == "e":
                            encode += "λ"
                            x += 1
                        elif word[x+1] == "n":
                            encode += "й"
                            x += 1
                        elif word[x+1] == "m":
                            encode += "\'m"
                            x += 1
                        else:
                            encode += "m"
                    else:
                        encode += char

                elif char == "n":
                    if x + 1 < len(word):
                        if word[x+1] == "t":
                            encode += "lnj"
                            x += 1
                        elif word[x+1] == "n":
                            encode += "\'n"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += char

                elif char == "l":
                    if x + 1 < len(word):
                        if word[x+1] == "y":
                            encode += "-iij"
                            x += 1
                        elif word[x+1] == "l":
                            encode += "\'l"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += char

                else:
                    if x + 1 < len(word):
                        if word[x+1] == char:
                            encode += f"\'{char}"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += word[x]
                x += 1
            encode += " "

    print(f"\nEncode result: {encode}")
    pyclip.copy(encode)
    print("\nThe encoded result has been copied to your clipboard")

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
    elif mode in ["decode", "Denode", "DECODE", "2", "de", "DE," "De"]:
        # if argument not already predefined from CLI
        if start == "":
            start = input("Decode: ")
        decode(start, reserved_words_dictionary)
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
    
    else:
        print("Please select a mode")
        print("\n1. Encode")
        print("2. Decode")
        print("3. Lookup")
        mode = input("\n> ")
        print_header(VERNO) 
        print(f"In {mode} mode\n")
        start = input("> ")

