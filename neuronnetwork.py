import numpy as np


class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.txt = text


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


class OutputNeuron(Neuron):
    def __init__(self, previous_neurons, weights):
        super().__init__(weights)
        self._previous_neurons = previous_neurons
        self._weights = weights
        self.__output = None

    @staticmethod
    def __func_of_act(value):
        return 1.0 / (1.0 + np.exp((-1.0) * value))

    def __summa(self):
        summ = 0.0
        try:
            if self._previous_neurons.shape[0] != self._weights.shape[0]:
                raise NeuralNetworkError("Number of weights and input values are different!")
            else:
                for i in range(len(self._previous_neurons)):
                    summ = summ + self._previous_neurons[i] * self._weights[i]
                return summ

        except NeuralNetworkError as nne:
            print(nne)

    # def __set_weights(self):  # in this method you can set necessary weights
    #     self._weights = np.random.random(self._previous_values.shape[0])

    def recalc(self):
        self.__output = self.__func_of_act(self.__summa())
        return self.__output

    def get_result_neuron(self):
        # if self._weights is None:
        #     self.__set_weights()
        if self.__output is None:
            if self.__summa() is not None:
                self.__output = self.__func_of_act(self.__summa())
        return self.__output


class NeuronLayer:
    def __init__(self, neurons):
        self._neurons = neurons
        self.__result_list = []

    def __calc_layer(self):
        for i in self._neurons:
            self.__result_list.append(i.get_result_neuron())
        return np.array(self._neurons)

    def set_input_value(self, input_values):
        for i in range(len(input_values)):
            self._neurons[i].set_input_value(input_values[i])
        
    def get_result_layer(self):
        self.__calc_layer()
        return self.__result_list


class NeuronNetwork:
    def __init__(self, layers):
        self.__layers = layers
        self.__result = []

    def __calc(self, input_values):
        self.__layers[0].set_input_value(input_values)
        for i in range(1, self.__layers):
            self.__result = self.__layers[i].get_result_layer()
        return self.__layers

    def get_result_net(self, input_values):
        if len(self.__result) == 0:
            self.__calc(input_values)
            return self.__result
        else:
            return self.__result


class NeuronNetworkFactory:
    def create_net(self, layer_num, neurons_num):
        new_network = NeuronNetwork(self._create_layers(layer_num, neurons_num))
        print("New network was created")
        return new_network

    def _create_layers(self, layer_num, neurons_num):
        layers_list = [self._create_input_layer(neurons_num)]
        for i in range(layer_num):
            layers_list.append(self._create_layer(neurons_num))
        return layers_list

    def _create_input_layer(self, neurons_num):
        new__input_layer = NeuronLayer(self._create_input_neurons(neurons_num))
        return new__input_layer

    def _create_layer(self, neurons_num):
        new_layer = NeuronLayer(self._create_neurons(neurons_num))
        return new_layer

    def _create_input_neurons(self, neurons_num):
        neurons_list = []
        for i in range(neurons_num):
            neurons_list.append(self._create_input_neuron())
        return neurons_list

    def _create_neurons(self, neurons_num):
        neurons_list = []
        for i in range(neurons_num):
            neurons_list.append(self._create_output_neuron())
        return neurons_list

    def _create_input_neuron(self):
        new_input_neuron = InputNeuron()
        return new_input_neuron

    def _create_output_neuron(self):
        new_output_neuron = OutputNeuron( , self._set_weights())  # ???
        return new_output_neuron

    def _set_weights(self):
        new_weights = [1, 0, 1, 0, 0]
        return new_weights


INPUT_VALUES = [0, 1, 0, 1]
LAYER_NUM = 5
NEURONS_NUM = 4
new_factory = NeuronNetworkFactory()
new_net = new_factory.create_net(LAYER_NUM, NEURONS_NUM)
print(new_net.get_result_net(np.array(INPUT_VALUES)))
