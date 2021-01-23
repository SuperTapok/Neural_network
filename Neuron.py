import numpy as np

class NeuralNetworkError(Exception):
    def __init__(self, text):
        self.txt = text
        
        
class Neuron:

    def __init__(self, _previous_values, weights = None, value=None):
        self._previous_values = _previous_values
        self._weights = weights
        if self._weights == None:
            self._weights = np.random.random(_previous_values.shape[0])
        self.__output = value

    def __summa(self):
        sum = 0.0
        try:
            if self._previous_values.shape[0] != self._weights.shape[0]:
                raise NeuralNetworkError("Number of weights and input values are different!")
            else:
                for i in range(len(self._previous_values)):
                    sum = sum + self._previous_values[i]*self._weights[i]
                return sum
       except NeuralNetworkError as nne:
            print(nne)

    def __func_of_act(self, value):
        return 1.0/(1.0+np.exp((-1.0) * value))

    def get_result(self):
        if self.__output is None:
            if self.__summa() != None:
                self.__output = self.__func_of_act(self.__summa())
        return self.output

    def recalc(self):
        self.output = self.__func_of_act(self.__summa())
        return self.output
