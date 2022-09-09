import pyclip

def encode(start, reserved_words_dictionary):
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
                            encode += "б"
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
                            if char != "\'":
                                encode += char
                    else:
                        if char != "\'":
                            encode += word[x]
                x += 1
            encode += " "

    print(f"\nEncode result: {encode}")
    try:
        pyclip.copy(encode)
        print("\nThe encoded result has been copied to your clipboard")
    except:
        print("\nThe encoded result could not be copied to your clipboard because the pyclip module does not work with your platform.")
