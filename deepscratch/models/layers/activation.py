import numpy as np

from deepscratch.models.layers.layer import Layer

from deepscratch.models.layers.activations.activation import Activation as Linear
from deepscratch.models.layers.activations.relu import Relu, Selu, Elu, LeakyRelu
from deepscratch.models.layers.activations.sigmoid import Sigmoid
from deepscratch.models.layers.activations.tanh import Tanh
from deepscratch.models.layers.activations.softmax import Softmax


class Activation(Layer):
    _activations = {
        'relu': Relu,
        'selu': Selu,
        'elu': Elu,
        'leaky-relu': LeakyRelu,
        'sigmoid': Sigmoid,
        'tanh': Tanh,
        'linear': Linear,
        'softmax': Softmax
    }
    
    def __init__(self, name):
        if name not in self._activations:
            raise ValueError('Activation unknown %s' % name)
        self._activation = self._activations[name]()
        
    def __call__(self, data):
        return self.forward(data)
    
    def forward(self, data):
        self._current_input_data = data
        return self._activation(data)

    def backward(self, grads, **kwargs):
        return grads * self._activation.grads(self._current_input_data)
    
    def initialize(self, initializer, otimizer, input_shape, **kwargs):
        self.input_shape = input_shape
    
    def output_shape(self):
        return self.input_shape
    