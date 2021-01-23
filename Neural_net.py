from Neural_layer import NeuronLayer


class NeuralNet:
    def __init__(self, layer_numbers, neuron_numbers):
        self.layer_numbers = layer_numbers
        self.neurons = neuron_numbers

    def __calc(self, input_values):
        result = []
        for i in range(self.layer_numbers):
            new_layer = NeuronLayer(input_values, self.neurons)
            input_values = new_layer.get_result()
        result = new_layer.get_result()
        for i in result:
            i = i.get_result()
        return result

    def get_results(self, input_values):
        return NeuralNet.__calc(self, input_values)

input_values = [0, 1, 0, 1]
num_of_layers = 100
num_of_neurons = 4
new_net = NeuralNet(input_values, num_of_layers, num_of_neurons)
print(new_net.get_results())
