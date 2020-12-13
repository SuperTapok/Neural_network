import numpy as np


class Neuron:

    def __init__(self, _previous_values):
        self._previous_values = _previous_values
        self._weights = np.random.random(_previous_values.shape[0])
        self.output = None

    def __summa(self):
        sum = 0.0
        for i in range(len(self._previous_values)):
                sum = sum + self._previous_values[i]*self._weights[i]
        return sum

    def __func_of_act(self, value):
        return 1/(1+np.exp((-1) * value))

    def get_result(self):
        if self.output is None:
            self.output = self.__func_of_act(self.__summa())
        return self.output

    def recalc(self):
        self.output = self.__func_of_act(self.__summa())
        return self.output


previous_values = np.random.random(3)
new_Neuron = Neuron(previous_values)
print("Output value: {}".format(new_Neuron.get_result()))
print("Recalculated value: {}".format(new_Neuron.recalc()))
