import pyclip

def decode(start, d):
    start_og = start
    start = start.split()
    encode = ""

    for word in start:
        if word in d:
            encode += d[word]
            encode += " "
        else:
            x = 0
            while x < len(word):
                char = word[x]
                        
                if char == "Д":
                    encode += "d"
                
                elif char in ["d", "z", "a", "i", "n", "j", "e"]:
                    if (encode[len(encode)-3:] == "ing") or (encode[len(encode)-2:] == "ce") or (encode[len(encode)-2:] == "se") or (encode[len(encode)-2:] == "nt") or (encode[len(encode)-2:] == "ly") or (encode[len(encode)-2:] == "et"):
                        if char != "e":
                            encode += ""
    
                    else:
                        encode += char
                
                # ss
                # st
                elif char == "ß":
                    encode += "ss"
                
                elif char == "š":
                    encode += "st"
                
                elif char == "ç":
                    if x + 1 < len(word):
                        if word[x+1] == "a":
                            if x + 2 < len(word):
                                if word[x+2] == "n":
                                    if x + 3 < len(word):
                                        if word[x+3] == "d":
                                            encode += "se"
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        else:
                            encode += char
                    else:
                        encode += char

                elif char == "k":
                    if x + 1 < len(word):
                        if word[x+1] == "a":
                            if x + 2 < len(word):
                                if word[x+2] == "n":
                                    if x + 3 < len(word):
                                        if word[x+3] == "d":
                                            encode += "ce"
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        else:
                            encode += char
                    else:
                        encode += char
                    
                elif char == "ë":
                    encode += "ea"
                
                elif char == "ä":
                    encode += "ee"
                
                elif char == "δ":
                    encode += "ge"
                
                elif char == "μ":
                    encode += "re"
                
                elif char == "ю":
                    encode += "ity"
                
                elif char == "ц":
                    encode += "ium"
                
                elif char == "ü":
                    encode += "ion"
                
                elif char == "ö":
                    encode += "ry"
                
                elif char == "ø":
                    encode += "ua"
                
                elif char == "λ":
                    encode += "me"
                
                elif char == "ඞ":
                    encode += "sus"
                
                elif char == " й":
                    encode += "mn"
                
                elif char == "б":
                    encode += "ie"
                
                elif char == "-":
                    if x + 1 < len(word):
                        # -ll → er
                        if word[x+1] == "l":
                            if x + 2  < len(word):
                                if word[x+2] == "l":
                                    encode += "er"
                                else:
                                    encode += char
                            else:
                                encode += char
                        
                        # -il  → or and -iij → ly
                        elif word[x+1] == "i":
                            if x + 2 < len(word):
                                #-il  → or
                                if word[x+2] == "l":
                                    encode += "or"
                                #-iij → ly
                                elif word[x+2] == "i":
                                    if x + 3 < len(word):
                                        if word[x+3] == "j":
                                            encode += "ly"
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        
                        # -ejd → et
                        elif word[x+1] == "e":
                            if x + 2 < len(word):
                                if word[x+2] == "j":
                                    if x + 3 < len(word):
                                        if word[x+3] == "d":
                                            encode += "et"
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        
                        #-kyo → ology
                        elif word[x+1] == "k":
                            if x + 2 < len(word):
                                if word[x+2] == "y":
                                    if x + 3 < len(word):
                                        if word[x+3] == "o":
                                            encode += "ology"
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                    
                        #-dzai → ing
                        elif word[x+1] == "d":
                            if x + 2 < len(word):
                                if word[x+2] == "z":
                                    if x + 3 < len(word):
                                        if word[x+3] == "a":
                                            if x + 4 < len(word):
                                                if word[x+4] == "i":
                                                    encode += "ing"
                                                else:
                                                    encode += char
                                            else:
                                                encode += char
                                        else:
                                            encode += char
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        else:
                            encode += char
                    else:
                        encode += char
                
                elif char == "l":
                    if encode[len(encode)-1] != "r" and encode[len(encode)-2] != "e":
                        if x + 1 < len(word):
                            if word[x+1] == "n":
                                if x + 2 < len(word):
                                    if word[x+2] == "j":
                                        encode += "nt"
                                    else:
                                        encode += char
                                else:
                                    encode += char
                            else:
                                encode += char
                        else:
                            encode += char
                
                elif char == "\'":
                    if x + 1 < len(word):
                        encode += f"{word[x+1]}"
                else:
                    """
                    if x + 1 < len(word):
                        if word[x+1] == char:
                            encode += f"\'{char}"
                            x += 1
                        else:
                            encode += char
                    else:
                        encode += word[x]
                    """

                    encode += char
                x += 1
            encode += " "
    print(f"Input: {start_og}")
    print(f"\n\nDecode result: {encode}")
    try:
        pyclip.copy(encode)
        print("\n\nThe decoded result has been copied to your clipboard")
    except:
        print("\nThe encoded result could not be copied to your clipboard because the pyclip module does not work with your platform.")
