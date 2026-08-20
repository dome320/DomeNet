# Connection.py 

import random

class connection:
        
    def __init__(self, n1: "neuron", n2: "neuron"):
        self.weight = random.random() 
        self.n1 = n1
        self.n2 = n2

    def update(self, weight: float):
        self.weight = weight

    
