import random

import numpy as np


class Perceptron(object):

    def __init__(self, no_of_inputs, iterations=1000, learning_rate=0.5):
        self.no_of_inputs = no_of_inputs
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.weights = np.random.rand(self.no_of_inputs + 1) - 0.5

    def train(self, training_data, labels):
        for _ in range(self.iterations):
            t = 0
            _t = t
            _w = self.weights
            for input, label in random.choices(zip(training_data, labels), k=len(training_data)):
                prediction = self.output(input)
                if label == prediction:
                    t += 1
                else:
                    if t > _t:
                        _t = t
                        _w = self.weights
                    t = 0
                    self.weights[1:] += self.learning_rate * (label - prediction) * input
                    self.weights[0] += self.learning_rate * (label - prediction)

    def output(self, x):
        summation = np.dot(self.weights[1:], x) + self.weights[0]
        if summation > 0:
            return 1
        else:
            return 0

    def error(self):  # Zad. 5. Napisac funkcj Error
        pass