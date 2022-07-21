
import math

def Aire_Cercle (rayon) :
    return (math.pi * rayon * rayon )
def Perimetre_Cercle (rayon) :
    return (2 * math.pi * rayon)
if __name__ == "__main__" :
    r = int (input ("Votre rayon : "))
    print ("Aire : %f" % (Aire_Cercle (r)))
    print ("Perimetre : %f" % (Perimetre_Cercle (r)))
