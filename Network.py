# Network.py

from Layer import layer 
from Neuron import neuron 
from Connection import connection
import math 
from itertools import zip_longest

class network: 

    def __init__(self, architecture: list[int]):
        self.layers = [] 

        for length in architecture:
            self.add(length)

    # sigmoid activation function
    def activate(self, sum: float) -> float:
        return 1.0 / (1.0 + math.exp(-1*sum))

    # add a layer to the network 
    def add(self, length: int):
        current: layer = layer(length)
        self.layers.append(current)

        # initialize connections of each neuron

        previous: layer = None

        if len(self.layers) > 1:
            previous = self.layers[len(self.layers) - 2]
        else:
            return 

        for neuron in previous.neurons:

                for n in current.neurons:

                    c: connection = connection(neuron, n)
                    n.connect(c)

    def forward(self, input: list[float]):

        if len(self.layers) < 1:
            return

        input_layer = self.layers[0]

        if len(input_layer.neurons) != len(input):
            raise ValueError("Input layer and Input Lengths don't match!")

        for i, neuron in enumerate(input_layer.neurons):
            neuron.value = input[i]

        for layer in self.layers[1:]:

            for neuron in layer:

                sum = 0.0
                for connection in neuron.connections:
                    sum += connection.weight * connection.n1.value

                sum += neuron.bias

                z = self.activate(sum)

                neuron.value = z 

    def __str__(self):
        columns = [str(layer).splitlines() for layer in self.layers]
        widths = [max((len(line) for line in col), default=0) for col in columns]
        padded = [
            [line.ljust(width) for line in col]
            for col, width in zip(columns, widths)
        ]
        fills = [" " * w for w in widths]
        rows = zip_longest(*padded, fillvalue=None)
        lines = []
        for row in rows:
            cells = [
                fills[i] if cell is None else cell
                for i, cell in enumerate(row)
            ]
            lines.append("   ".join(cells))
        return "\n".join(lines)


    




                





                

                




        

