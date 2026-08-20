# Neuron.py 

from Connection import connection
import random

class neuron:

    def __init__(self):
        self.value: float = 0.0
        self.bias: float = random.random()
        self.connections = []

    def connect(self, c: connection):
        self.connections.append(c)

    def update(self, value: int):
        self.value = value

    def __str__(self):
        return f"({self.value})"
     