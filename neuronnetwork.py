import numpy as np


class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.txt = text


class Neuron:

    def __init__(self, _previous_values, weights=None, value=None):
        self._previous_values = _previous_values
        self._weights = weights
        if self._weights is None:
            self._weights = np.random.random(_previous_values.shape[0])
        self.__output = value

    def __summa(self):
        sum = 0.0
        try:
            if self._previous_values.shape[0] != self._weights.shape[0]:
                raise NeuralNetworkError("Number of weights and input values are different!")
            else:
                for i in range(len(self._previous_values)):
                    sum = sum + self._previous_values[i] * self._weights[i]
                return sum

        except NeuralNetworkError as nne:
            print(nne)

    @staticmethod
    def __func_of_act(value):
        return 1.0 / (1.0 + np.exp((-1.0) * value))

    def get_result(self):
        if self.__output is None:
            if self.__summa() is not None:
                self.__output = self.__func_of_act(self.__summa())
        return self.__output

    def recalc(self):
        self.__output = self.__func_of_act(self.__summa())
        return self.__output


class NeuronLayer:
    def __init__(self, neurons):
        self._neurons = neurons

    def __calc(self):
        list = []
        for i in range(self._neurons):
            new_neuron = Neuron(self.previous_values)
            list.append(new_neuron)
        return np.array(list)

    def get_result(self):
        return self.__calc()


class NeuralNet:
    def __init__(self, layer_numbers, neuron_numbers):
        self.layer_numbers = layer_numbers
        self.neurons = neuron_numbers

    def __calc(self):
        for i in range(self.layer_numbers):
            new_layer = NeuronLayer(self.neurons)
        result = new_layer.get_result()
        for i in result:
            i = i.get_result()
        return result

    def get_results(self):
        return self.__calc()


INPUT_VALUES = [0, 1, 0, 1]
LAYER_NUM = 100
NEURONS_NUM = 4
new_net = NeuralNet(layer_num, neurons_num)
print(new_net.get_results())
