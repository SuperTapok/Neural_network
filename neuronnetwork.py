import numpy as np


class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.txt = text


class Neuron:

    def __init__(self, weights=None):  # , previous_values, weights=None
        self._previous_values = None
        self._weights = weights
        self.__output = None

    @staticmethod
    def __func_of_act(value):
        return 1.0 / (1.0 + np.exp((-1.0) * value))

    def __summa(self):
        summ = 0.0
        try:
            if self._previous_values.shape[0] != self._weights.shape[0]:
                raise NeuralNetworkError("Number of weights and input values are different!")
            else:
                for i in range(len(self._previous_values)):
                    summ = summ + self._previous_values[i] * self._weights[i]
                return summ

        except NeuralNetworkError as nne:
            print(nne)

    def __set_weights(self):  # in this method you can set necessary weights
        self._weights = np.random.random(self._previous_values.shape[0])

    def recalc(self):
        self.__output = self.__func_of_act(self.__summa())
        return self.__output

    def get_result_neuron(self, input_values):
        self._previous_values = input_values
        if self._weights is None:
            self.__set_weights()
        if self.__output is None:
            if self.__summa() is not None:
                self.__output = self.__func_of_act(self.__summa())
        return self.__output


# class InputNeuron(Neuron):
#     def __init__(self, input_value):
#         self.input_value = input_value
#
#     def get_res(self):
#         return self.input_value
#
#
# class OutputNeuron(Neuron):
#     def __init__(self, previous_values, weights=None):  # value=None
#         self._previous_values = previous_values
#         self._weights = weights
#         if self._weights is None:
#             self._weights = np.random.random(previous_values.shape[0])
#         self.__output = None
#
#     @staticmethod
#     def __func_of_act(value):
#         return 1.0 / (1.0 + np.exp((-1.0) * value))
#
#     def __summa(self):
#         sum = 0.0
#         try:
#             if self._previous_values.shape[0] != self._weights.shape[0]:
#                 raise NeuralNetworkError("Number of weights and input values are different!")
#             else:
#                 for i in range(len(self._previous_values)):
#                     sum = sum + self._previous_values[i] * self._weights[i]
#                 return sum
#
#         except NeuralNetworkError as nne:
#             print(nne)
#
#     def recalc(self):
#         self.__output = self.__func_of_act(self.__summa())
#         return self.__output
#
#     def get_res(self):
#         if self.__output is None:
#             if self.__summa() is not None:
#                 self.__output = self.__func_of_act(self.__summa())
#         return self.__output


class NeuronLayer:
    def __init__(self, neurons):
        self._neurons = neurons
        self.__input_values = None
        self.__neurons_list = []
        for i in range(self._neurons):  # initialisation neurons in layer
            new_neuron = Neuron()
            self.__neurons_list.append(new_neuron)
        self.__result_list = []

    def __calc_layer(self):
        for i in self.__neurons_list:
            self.__result_list.append(i.get_result_neuron(self.__input_values))
        return np.array(self.__neurons_list)

    # def recalc_layer(self):
    #

    def get_result_layer(self, input_values):
        self.__input_values = input_values
        self.__calc_layer()
        return self.__result_list


class NeuronNetwork:
    def __init__(self, layer_numbers, neuron_numbers):
        self.__layer_numbers = layer_numbers
        self.__neurons = neuron_numbers
        self.__input_values = None
        self.__layers_list = []
        for i in range(self.__layer_numbers):  # initialisation layers in network
            new_layer = NeuronLayer(self.__neurons)
            self.__layers_list.append(new_layer)
        self.__result = []

    def __calc_net(self):
        for i in self.__layers_list:
            self.__result = i.get_result_layer(self.__input_values)
        return self.__layers_list

    def get_result_net(self, input_values):
        self.__input_values = input_values
        if len(self.__result) == 0:
            self.__calc_net()
            return self.__result
        else:
            return self.__result


class NeuronNetworkFactory:
    def __init__(self):
        self.net_list = []

    def create_net(self, layer_num, neurons_num):
        new_net = NeuronNetwork(layer_num, neurons_num)
        self.net_list.append(new_net)
        print("New network was created")


INPUT_VALUES = [0, 1, 0, 1]
LAYER_NUM = 5
NEURONS_NUM = 4
new_factory = NeuronNetworkFactory()
new_factory.create_net(LAYER_NUM, NEURONS_NUM)
print(new_factory.net_list[0].get_result_net(np.array(INPUT_VALUES)))
