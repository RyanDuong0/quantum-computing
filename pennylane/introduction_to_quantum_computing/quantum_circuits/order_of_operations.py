import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

dev = qml.device('default.qubit', wires = 3)

def my_circuit(theta, phi):
    ##################
    # YOUR CODE HERE #
    ##################

    # REORDER THESE 5 GATES TO MATCH THE CIRCUIT IN THE PICTURE

    # qml.CNOT(wires=[0, 1])
    # qml.CNOT(wires=[2, 0])
    # qml.Hadamard(wires=0)
    # qml.RX(theta, wires=2)
    # qml.RY(phi, wires=1)

    #correct order
    qml.CNOT(wires=[0, 1])
    qml.RX(theta, wires=2)
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[2, 0])
    qml.RY(phi, wires=1)

    # This is the measurement; we return the probabilities of all possible output states
    # You'll learn more about what types of measurements are available in a later node
    return qml.probs(wires=[0, 1, 2])

def PREV_my_circuit(theta, phi):
    ##################
    # YOUR CODE HERE #
    ##################

    # REORDER THESE 5 GATES TO MATCH THE CIRCUIT IN THE PICTURE

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[2, 0])
    qml.Hadamard(wires=0)
    qml.RX(theta, wires=2)
    qml.RY(phi, wires=1)

    # This is the measurement; we return the probabilities of all possible output states
    # You'll learn more about what types of measurements are available in a later node
    return qml.probs(wires=[0, 1, 2])

theta, phi = 0.1, 0.2

my_qnode = qml.QNode(my_circuit, dev)
PREV_qnode = qml.QNode(PREV_my_circuit, dev)

qml.drawer.use_style("black_white")
fig, ax = qml.draw_mpl(my_qnode)(theta, phi)
plt.show()

fig, ax = qml.draw_mpl(PREV_qnode)(theta, phi)
plt.show()