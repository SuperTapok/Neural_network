import numpy as np
from Neuron import Neuron


class NeuronLayer:
    def __init__(self, neurons):
        self._neurons = neurons

    def __calc(self, input_values, neurons):
        list = []
        for i in range(self._neurons):
            new_neuron = Neuron(self.previous_values)
            list.append(new_neuron)
        return np.array(list)

    def get_result(self):
        return NeuronLayer.__calc(self, self.__previous_layer, self._neurons)
