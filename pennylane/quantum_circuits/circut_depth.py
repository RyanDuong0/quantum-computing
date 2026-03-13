import pennylane as qml
import matplotlib.pyplot as plt

# What is the depth of the circuit?

dev = qml.device("default.qubit", wires=3)


@qml.qnode(dev)
def my_circuit(theta, phi, omega):
    qml.RX(theta, wires=0)
    qml.RY(phi, wires=1)
    qml.RZ(omega, wires=2)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])
    return qml.probs(wires=[0, 1, 2])


##################
# YOUR CODE HERE #
##################

# FILL IN THE CORRECT CIRCUIT DEPTH
depth = 4

#circuit depth of 4. The "measurement dial" blocks don't count towards the depth

circuit = qml.QNode(my_circuit, dev)
qml.drawer.use_style("black_white")
fig, ax = qml.draw_mpl(circuit)(0,0,0)
plt.show()