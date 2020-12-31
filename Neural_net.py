from Neural_layer import NeuronLayer


class NeuralNet:
    def __init__(self, input_values, numbers_of_layers, num_of_neurons_on_every_layer):
        self.input_values = input_values
        self.numbers_of_layers = numbers_of_layers
        self.neurons = num_of_neurons_on_every_layer

    def __calc(self, input_values, quantity_of_neurons, number_of_layers):
        result = []
        previous_values = input_values
        for i in range(number_of_layers):
            new_layer = NeuronLayer(previous_values, quantity_of_neurons)
            previous_values = new_layer.get_result()
        result = new_layer.get_result()
        return result

    def get_results(self):
        return NeuralNet.__calc(self, self.input_values, self.neurons,  self.numbers_of_layers)


input_values = [0, 1, 0, 1]
num_of_layers = 100
num_of_neurons = 4
new_net = NeuralNet(input_values, num_of_layers, num_of_neurons)
print(new_net.get_results())
