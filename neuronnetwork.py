import numpy as np


class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.txt = text


class Neuron:

    def __init__(self, previous_values=None, weights=None, value=None):
        self._previous_values = previous_values
        self._weights = weights
        if self._weights is None:
            self._weights = np.random.random(previous_values.shape[0])
        self.__output = value

    @staticmethod
    def __func_of_act(value):
        return 1.0 / (1.0 + np.exp((-1.0) * value))

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

    def recalc(self):
        self.__output = self.__func_of_act(self.__summa())
        return self.__output

    def get_res(self):
        if self.__output is None:
            if self.__summa() is not None:
                self.__output = self.__func_of_act(self.__summa())
        return self.__output


class InputNeuron(Neuron):
    pass


class OutputNeuron(Neuron):
    pass


INPUT_VALUES = [1, 0, 1, 0]
new_neuron = Neuron()
# class NeuronLayer:
#     def __init__(self, neurons):
#         self._neurons = neurons
#         self.neurons_list = []
#         for i in range(self._neurons):
#             new_neuron = Neuron(self, self._previous_values)
#             self.neurons_list.append(new_neuron)
#
#     def __cal(self, input_values):
#         list = []
#         for i in range(self._neurons):
#             new_neuron = Neuron(input_values)
#             list.append(new_neuron)
#         return np.array(list)
#
#     def get_result(self, input_values):
#         return self.__calc(input_values)
#
#
# class NeuralNet:
#     def __init__(self, layer_numbers, neuron_numbers):
#         self.layer_numbers = layer_numbers
#         self.neurons = neuron_numbers
#         self.__layers_list = []
#         for i in range(self.layer_numbers):
#             new_layer = NeuronLayer(self.neurons)
#             self.layers_list.append(new_layer)
#
#     def __calc(self, inpt_values):
#         for i in self.__layers_list:
#             i = i.__cal(inpt_values)
#         return self.__layers_list
#
#     def get_results(self, input_values):
#         self.__calc(input_values)
#
#
# INPUT_VALUES = [0, 1, 0, 1]
# LAYER_NUM = 100
# NEURONS_NUM = 4
# new_net = NeuralNet(LAYER_NUM, NEURONS_NUM)
# print(new_net.get_results())

