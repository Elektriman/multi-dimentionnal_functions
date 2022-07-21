import numpy as np

class CunJeuDeCartes :
    couleurs = ["pique", "trèfle", "coeur", "carreau"]
    valeurs = ["as", "roi", "dame", "valet", "dix", "neuf", "huit", "sept", "six", "cinq", "quatre", "trois", "deux"]

    def __init__(self):
        P = []
        for c in self.couleurs :
            for v in self.valeurs :
                P.append(f'{v} de {c}')
        self.paquet = P

    def nom_carte(self, n:int)->str :
        return self.paquet[n]

    def afficher(self):
        print(str(self))

    def __str__(self)->str:
        return "Le paquet de cartes est :\n"+"\n".join(self.paquet)

    def battre(self):
        #pour mélanger les cartes on échange deux cartes aléatoiresment jusqu'à ce que le paquet soit mélangé.
        #un paquet de n cartes est en général bien mélangé après 2n échanges
        for i in range(2*len(self.paquet)):
            a,b = np.random.randint(0, len(self.paquet)),np.random.randint(0, len(self.paquet))
            self.paquet[a], self.paquet[b] = self.paquet[b], self.paquet[a]

    def tirer(self):
        a = np.random.randint(0, len(self.paquet))
        return self.paquet[a]
