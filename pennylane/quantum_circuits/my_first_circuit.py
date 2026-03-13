import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

device = qml.device('default.qubit', wires = 2)

def my_first_circuit(theta):

    qml.Hadamard(wires = 0)
    qml.CNOT(wires = [0,1])
    qml.RZ(theta, wires = 0)

    return qml.probs(wires = [0,1])

my_qnode = qml.QNode(my_first_circuit, device) #can define it like this or with a decorator
# @qml.qnode(dev) and place it above my_first_circuit definition

probabilities = my_qnode(np.pi/2)
states = ["|00>", "|01>", "|10>", "|11>"]
for state, probability in zip(states, probabilities):
    print(f"{state}: {probability}")

print(qml.draw(my_qnode)(np.pi/2))
qml.drawer.use_style("black_white")
fig, ax = qml.draw_mpl(my_qnode)(np.pi/2)
plt.show()
# CNOT: control is the solid black dot, target is the "crosshair"