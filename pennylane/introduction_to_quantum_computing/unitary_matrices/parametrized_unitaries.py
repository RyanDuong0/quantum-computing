import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1) #wires = 1 means 1 qubit
#qubits are 0-based indexing so qubit1 is on index = 0 = wire


@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY A ROT GATE USING THE PROVIDED INPUT PARAMETERS
    qml.Rot(phi, theta, omega, wires = 0)

    # RETURN THE QUANTUM STATE VECTOR

    return qml.state()
