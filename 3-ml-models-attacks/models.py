from torch import nn


class SoftmaxRegression(nn.Module):
    """Softmax Regression Classifier.

    This classifier is a generalization of logistic regression that
    allows the class variable to take more than two values—in our case,
    there are 40 individuals in the dataset, so the classifier needs to
    distinguish between 40 labels.
    Softmax regression is often used as the final layer in deep neural network
    architectures, so on its own this classifier can be seen as a
    neural network with no hidden layers

    Extracted from: https://dl.acm.org/doi/pdf/10.1145/2810103.2813677
    """

    def __init__(self, in_features: int = 112 * 92, n_classes: int = 40):
        super(SoftmaxRegression, self).__init__()
        self.regression = nn.Linear(in_features, n_classes)

    def forward(self, x):
        x = self.regression(x)
        return nn.LogSoftmax(dim=1)(x)


class MLP(nn.Module):
    """Multilayer Perceptron Network.

    A multilayer perceptron network model with one hidden layer
    of 3000 sigmoid neurons (or units), and a softmax output layer.
    This classifier can be understood as performing
    softmax regression after first applying a non-linear transformation
    to the feature vector.
    The point of this transformation, which corresponds to the hidden layer,
    is to map the feature vector into a lower-dimensional space in which
    the classes are separable by the softmax output layer.

    Adapted from: https://dl.acm.org/doi/pdf/10.1145/2810103.2813677
    """

    def __init__(self, in_features: int = 112 * 92, n_classes: int = 40):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(in_features, 3000)
        self.prediction = nn.Linear(3000, n_classes)

    def forward(self, x):
        x = self.hidden(x)
        x = nn.Sigmoid()(x)
        x = self.prediction(x)
        return nn.LogSoftmax(dim=1)(x)
