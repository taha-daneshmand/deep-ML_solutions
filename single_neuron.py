import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    def sigmoid(z):
        return 1 / (1 + math.exp(-z))

    probabilities = []
    squared_errors = []

    for feature_vector in features:
        z = sum(w * x for w, x in zip(weights, feature_vector)) + bias
        
        probability = sigmoid(z)
        probabilities.append(round(probability, 4))

    mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels)
    mse = round(mse, 4)

    return probabilities, mse
