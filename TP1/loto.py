import numpy as np

np.random.seed(69) #le tirage sera 12-10-46-29-23-26
def tirage(essais:int):
    V = [i for i in range(1,49)]
    T = [V.pop(np.random.randint(len(V))) for i in range(6)]
    E = []
    if not 0<essais<7 :
        raise ValueError("le nombre d'essais doit être compris entre 1 et 6 inclus")
    for i in range(essais):
        n = int(input(f"entrez votre nombre ({i+1}) : "))
        if not 0<n<50 :
            raise ValueError("Vous devez donner un nombre entier entre 1 et 49 inclus")
        if n in E :
            raise ValueError("Vous ne pouvez pas donner deux fois le même nombre")
        E.append(n)
    G = ["perdu", "gagné"]
    print(f"Vous avez {G[int(E==T[:len(E)])]} au PMU")
    print(f"Vous avez {G[set(E)<=set(T)]} au LOTO")
    print("-".join([str(t) for t in T]))
