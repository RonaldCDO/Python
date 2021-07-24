import numpy as np

# Forward Propagation

input_data = np.array([2, 3])
weigths = {'node_0': np.array([1, 1]),
           'node_1': np.array([-1, 1]),
           'output': np.array([2, -1])}

node_0_value = (input_data * weigths['node_0']).sum()
node_1_value = (input_data * weigths['node_1']).sum()

hidden_layer_values = np.array([node_0_value, node_1_value])
print(hidden_layer_values)
output = (hidden_layer_values * weigths['output']).sum()
print(output)
