reserved_words_dictionary = {
        "wtf": "nansa fuck",
        "a": "aan",
        "an": "aa'n",
        "A": "Aan",
        "An": "Aa'n",
        "him": "kaar-san",
        "Him": "Kaar-san",
        "his": "kaar-noder",
        "His": "Kaar-noder",
        "he": "kaar",
        "He": "Kaar",
        "she": "kaal",
        "She": "Kaal",
        "her": "kaal-san",
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
        "dylan": "hayabusa",
        "Dylan": "Hayabusa",
        "this": "malaan",
        "This": "Malaan",
        "also": "akez",
        "has": "maz",
        "Has": "Maz",
        "Also": "Akez",
        "was": "irupost",
        "Was": "Irupost",
        "were": "irupostem",
        "Were": "Irupostem",
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
        "Are": "Iru",
        "am": "irum",
        "Am": "Irum",
        "I'm": "ikii irum",
        "i'm": "ikii irum",
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
        "be": "iruz",
        "Be": "Iruz",
        "is": "irul",
        "Is": "Irul",
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

def get_reversed_dictionary(d):
    reversed_dict = dict()
    d_items = d.items()
    for key, value in d_items:
        reversed_dict[value] = key
    return reversed_dict