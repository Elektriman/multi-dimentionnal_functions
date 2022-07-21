import numpy as np

class CunCercle :
    def __init__(self, r:float):
        self.r = r

    def aire(self)->float:
        return float(np.pi*self.r**2)
