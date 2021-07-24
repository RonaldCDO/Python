import numpy as np

weights = np.array([1, 2])
input_data = np.array([3, 4])
target = 6
learning_rate = 0.01
preds = (weights * input_data).sum()
error = preds - target

# my version
it_count = 0
while error > 0.0001:
    weights = np.array([weights[0] - 2 * error * learning_rate * input_data[0],
                        weights[1] - 2 * error * learning_rate * input_data[1]])
    preds = (weights * input_data).sum()
    error = preds - target
    print(f'Target: {target}',
          f'Prediction number: {preds}',
          f'Respective Error: {error}')

    it_count += 1
print(f'number of iterations: {it_count}')

print('\n', '<-- SEPARATOR -->', '\n')

weights = np.array([1, 2])
input_data = np.array([3, 4])
target = 6
learning_rate = 0.01
preds = (weights * input_data).sum()
error = preds - target

# course version
gradient = 2 * input_data * error
print(f'Gradient:{gradient}')
weights_updated = weights - learning_rate * gradient
preds_updated = (weights_updated * input_data).sum()
error_updated = preds_updated - target
print(f'Updated error: {error_updated}')

