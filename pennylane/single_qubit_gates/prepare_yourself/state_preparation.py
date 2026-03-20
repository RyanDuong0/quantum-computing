import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE
    #target state is 1/sqrt(2) |0> + 1/sqrt(2) e^((5/4)i pi)) |1>

    qml.Hadamard(wires = 0) #apply hadamard to get the 1/sqrt(2) factor
    qml.RZ(5*np.pi/4, wires=0) #apply RZ with input (5pi/4) which will affect both |0> and |1>
    #results in e^(-i x (5pi/8)) being coefficient of |0> and e^(i x (5pi/8)) being coefficient of |1>
    #factor out global phase of e^(-i x (5pi/8)) which leaves relative phase on |1> of e^(5pi/8)

    return qml.state()
