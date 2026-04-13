import pennylane as qml
import pennylane.numpy as np

n_qubits = 9
dev = qml.device("default.qubit", wires=n_qubits)
error_dict = {0: 'PauliX', 1: 'PauliY', 2: 'PauliZ'}

def error(error_key, qubit):
    """Defines the error that is induced in the circuit.

    Args:
        error_key (int): An integer associated to the type of error (Pauli X, Y, or Z)
        qubit (int): The qubit that the error occurs on.
    """
    getattr(qml, error_dict[error_key])(qubit)


@qml.qnode(dev)
def shor(state, error_key, qubit):
    """A circuit defining Shor's code for error correction.

    Args:
        state (list(float)): The quantum state of the first qubit in the circuit.
        error_key (int): An integer associated to the type of error (Pauli X, Y, or Z)
        qubit (int): The qubit that the error occurs on.

    Returns:
        (list(float)): The expectation value of the Pauli Z operator on every qubit.
    """
    qml.StatePrep(np.array(state), wires=0)

    # Student implementation starts here #
    qml.CNOT(wires=[0, 3])
    qml.CNOT(wires=[0, 6])

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[3, 4])
    qml.CNOT(wires=[6, 7])

    qml.CNOT(wires=[0, 2])
    qml.CNOT(wires=[3, 5])
    qml.CNOT(wires=[6, 8])

    # apply the error
    error(error_key, qubit)

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[3, 4])
    qml.CNOT(wires=[6, 7])

    qml.CNOT(wires=[0, 2])
    qml.CNOT(wires=[3, 5])
    qml.CNOT(wires=[6, 8])

    qml.Toffoli(wires=[1, 2, 0])
    qml.Toffoli(wires=[4, 5, 3])
    qml.Toffoli(wires=[7, 8, 6])

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0, 3])
    qml.CNOT(wires=[0, 6])
    qml.Toffoli(wires=[3, 6, 0])

    # return expectation value of the Pauli-Z operator on each qubit
    return [qml.expval(qml.PauliZ(i)) for i in range(9)]  # from qubit0 - qubit8

