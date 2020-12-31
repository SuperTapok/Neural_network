import numpy as np
from Neuron import Neuron


class NeuronLayer:
    def __init__(self, previous_values, neurons):
        self.__previous_layer = previous_values
        self._neurons = neurons

    def __calc(self, input_values, neurons):
        list = []
        prev_values = np.array(input_values)
        for i in range(neurons):
            new_neuron = Neuron(prev_values)
            list.append(new_neuron.get_result())
        return np.array(list)

    def get_result(self):
        return NeuronLayer.__calc(self, self.__previous_layer, self._neurons)
