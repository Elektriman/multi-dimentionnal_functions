
def classement(entry1, entry2):
    #cas où on donne deux chaines de caractères
    if type(entry1)==type(entry2)==str :
        if len(entry1)>len(entry2) :
            return entry1
        elif len(entry1)<len(entry2) :
            return entry2
        else :
            return "les deux chaînes de caractères sont de la même longueur"
    
    #cas où l'on donne deux nombres
    elif type(entry1) in [float, int] and type(entry2) in [float, int]:
        if entry1 < entry2 :
            return entry1
        else :
            return entry2
    
    else :
        raise TypeError(f"les entrées doivent êtres de types (int ou float, int ou float) ou (str, str) et pas ({type(entry1).__name__}, {type(entry2).__name__})")
