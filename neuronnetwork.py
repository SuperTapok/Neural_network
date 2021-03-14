import numpy as np
import random


class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.__txt = text


class LoadingException(Exception):
    def __init(self, text):
        self.__txt = text


class Neuron:

    def __init__(self, weights=None):
        self._previous_values = None
        self._weights = weights
        self.__output = None

    def get_result_neuron(self):
        return self.__output


class InputNeuron(Neuron):
    def __init__(self):
        super().__init__()

    def set_input_value(self, value):
        self.__output = value

    def get_result_input_neuron(self):
        return self.__output


class OutputNeuron(Neuron):
    def __init__(self, weights, previous_neurons):
        super().__init__(weights)
        self.__previous_neurons = previous_neurons
        self._weights = weights
        self.__output = None

    @staticmethod
    def __func_of_act(value):
        return 1.0 / (1.0 + np.exp((-1.0) * value))

    def __str__(self):
        f = ""
        for i in self._weights:
            f = f + str(i)+" "
        return f

    def __sum(self, k):
        sum = 0.0
        try:
            if k.shape[0] != self._weights.shape[0]:
                raise NeuralNetworkError("Number of weights and input values are different!")
            else:
                for i in range(k.shape[0]):
                    sum = sum + k[i] * self._weights[i]
                return sum

        except NeuralNetworkError as nne:
            print(nne)

    def re_calc(self, k):
        self.__output = self.__func_of_act(self.__sum(k))
        return self.__output

    def get_result_neuron(self):
        k = np.array(self.__previous_neurons.get_result_layer())
        if self.__output is None:
            if self.__sum(k) is not None:
                self.__output = self.__func_of_act(self.__sum(k))
        return self.__output

    def save_weights(self):
        with open('weights.txt', 'a') as file:
            file.writelines("{0}\n".format(str(self)))


class NeuronLayer:
    def __init__(self, neurons):
        self.__neurons = neurons
        self.__result_list = []

    def __calc_layer(self):
        for i in self.__neurons:
            self.__result_list.append(i.get_result_neuron())
        return np.array(self.__neurons)

    def set_input_value(self, input_values):
        try:
            if len(input_values) != len(self.__neurons):
                raise NeuralNetworkError("Number of neurons and input values are different!")
            else:
                for i in range(len(input_values)):
                    self.__neurons[i].set_input_value(input_values[i])
                    self.__result_list.append(self.__neurons[i].get_result_input_neuron())
        except NeuralNetworkError as e:
            print(e)

    def get_result_layer(self):
        if len(self.__result_list) == 0:
            self.__calc_layer()
            return self.__result_list
        else:
            return self.__result_list

    def save_weights(self):
        for i in self.__neurons:
            i.save_weights()
        with open('weights.txt', 'a') as file:
            file.writelines("\n")


class NeuronNetwork:
    def __init__(self, layers):
        self.__layers = layers
        self.__result = []

    def __calc(self, input_values):
        self.__layers[0].set_input_value(input_values)
        self.__result = self.__layers[0].get_result_layer()
        for i in range(1, len(self.__layers)):
            self.__result = self.__layers[i].get_result_layer()
        return self.__layers

    def get_result_net(self, input_values):
        if len(self.__result) == 0:
            self.__calc(input_values)
            return self.__result
        else:
            return self.__result

    def save_weights(self):
        for i in range(1, len(self.__layers)):
            self.__layers[i].save_weights()


class NeuronNetworkFactory:
    def create_net(self, layer_num, neurons_num, load_weights=False):
        if load_weights is True:
            new_network = NeuronNetwork(self.__create_layers(layer_num, neurons_num, True))
        else:
            new_network = NeuronNetwork(self.__create_layers(layer_num, neurons_num))
        print("New network was created")
        return new_network

    def __create_layers(self, layer_num, neurons_num, load_weights=False):
        layers_list = [self.__create_input_layer(neurons_num)]
        if load_weights is True:
            for i in range(1, layer_num):
                new_neurons = self.__create_neurons(neurons_num, layers_list[i - 1], True)
        else:
            for i in range(1, layer_num):
                new_neurons = self.__create_neurons(neurons_num, layers_list[i - 1])
        new_layer = NeuronLayer(new_neurons)
        layers_list.append(new_layer)
        return layers_list

    def __create_input_layer(self, neurons_num):
        new__input_layer = NeuronLayer(self.__create_input_neurons(neurons_num))
        return new__input_layer

    def __create_input_neurons(self, neurons_num):
        neurons_list = []
        for i in range(neurons_num):
            neurons_list.append(self.__create_input_neuron())
        return neurons_list

    def __create_neurons(self, neurons_num, old_neurons, load_weights=False):
        neurons_list = []
        if load_weights is True:
            for i in range(neurons_num):
                neurons_list.append(self.__create_output_neuron(old_neurons, True))
        else:
            for i in range(neurons_num):
                neurons_list.append(self.__create_output_neuron(old_neurons))
        return neurons_list

    @staticmethod
    def __create_input_neuron():
        new_input_neuron = InputNeuron()
        return new_input_neuron

    def __create_output_neuron(self, old_neurons, load_weights=True):
        if load_weights is True:
            new_output_neuron = OutputNeuron(self.__load_weights(), old_neurons)
        else:
            new_output_neuron = OutputNeuron(self.__set_weights(), old_neurons)
        return new_output_neuron

    @staticmethod
    def __load_weights():
        with open('weights.txt') as f:
            try:
                float(f.read(1))
            except ValueError:
                raise LoadingException("Weights.txt is empty!")
            else:
                pass

    @staticmethod
    def __set_weights():
        new_weights = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
        return np.array(new_weights)


INPUT_VALUES = [0, 0, 0, 0]
LAYER_NUM = 5
NEURONS_NUM = 4
if NEURONS_NUM != len(INPUT_VALUES):
    print("Neural Network error! Check numbers of neurons and input values")
else:
    new_factory = NeuronNetworkFactory()
    new_net = new_factory.create_net(LAYER_NUM, NEURONS_NUM)
    print(new_net.get_result_net(np.array(INPUT_VALUES)))
    new_net.save_weights()
