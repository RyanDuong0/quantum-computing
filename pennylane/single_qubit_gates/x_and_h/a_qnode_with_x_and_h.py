import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

##################
# YOUR CODE HERE #
##################

# CREATE A DEVICE
dev = qml.device('default.qubit', wires=1)

# CREATE A QNODE CALLED apply_hxh THAT APPLIES THE CIRCUIT ABOVE
@qml.qnode(dev)
def apply_hxh(state):
    if state == 1:
        qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

# Print your results
print(apply_hxh(0))
print(apply_hxh(1))

circuit = qml.QNode(apply_hxh, dev)
qml.drawer.use_style("black_white")
fig, ax = qml.draw_mpl(apply_hxh)(0)
plt.show()