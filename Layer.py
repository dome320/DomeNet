# Layer.py 

from Neuron import neuron 

class layer: 

    def __init__(self, length: int):
        self.neurons = [] 

        for i in range(length):
            self.neurons.append(neuron())

    def __str__(self):
        return "\n".join(str(n) for n in self.neurons)


