import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE
    #target = sqrt(3)/2 |0> - (i/2) |1>

    qml.RX(np.pi/3, wires = 0)

    return qml.state()
