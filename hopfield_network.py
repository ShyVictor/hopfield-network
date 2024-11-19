import numpy as np

class HopfieldNetwork:
  def __init__(self: HopfieldNetwork, size: int):
    self.size: int = size
    self.weights: np.darray = np.zeros((size, size))

  def train(self, patterns):
    for pattern in patterns:
      pattern = np.array(pattern)
      self.weights += np.outer(pattern, pattern)

    np.fill_diagonal(self.weights, 0)
    self.weights /= self.size
    
  def predict(self, pattern, iterations=10):
        pattern = np.array(pattern)
        for _ in range(iterations):
            for i in range(self.size):
                activation = np.dot(self.weights[i], pattern)
                if activation > 0:
                    pattern[i] = 1
                elif activation < 0:
                    pattern[i] = -1
        return pattern


patterns = [
    [1, 1, -1, -1],
    [1, -1, 1, -1]
]

network = HopfieldNetwork(4)
network.train(patterns)

test_pattern = [1, 1, -1, -1]
predicted_pattern = network.predict(test_pattern)
test_pattern_noisy = [1, -1, -1, -1]
predicted_pattern_noisy = network.predict(test_pattern_noisy)
