import numpy as np

# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])


def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        np.array: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """
    # check if probability adds up to 1. P(actual) = |a|^2 + |b|^2 should equal 1
    alpha_squared_magnitude = alpha * alpha.conjugate()
    beta_squared_magnitude = beta * beta.conjugate()

    normalization = (alpha_squared_magnitude + beta_squared_magnitude) ** 0.5

    return np.array([alpha / normalization, beta / normalization])


# Example test
state = normalize_state(3, 4)
print(state)

# Check probabilities sum to 1
print(abs(state[0])**2 + abs(state[1])**2)


#pennylane's solution
# Here are the vector representations, for convenience
# ket_0 = np.array([1, 0])
# ket_1 = np.array([0, 1])
#
#
# def normalize_state(alpha, beta):
#     """Compute a normalized quantum state given arbitrary amplitudes.
#
#     Args:
#         alpha (complex): The amplitude associated with the |0> state.
#         beta (complex): The amplitude associated with the |1> state.
#
#     Returns:
#         np.array[complex]: A vector with 2 elements that represents
#         a normalized quantum state.
#     """
#
#     ##################
#     # YOUR CODE HERE #
#     ##################
#
#     # CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
#     norm = np.abs(alpha) ** 2 + np.abs(beta) ** 2
#     alpha_prime = alpha / np.sqrt(norm)
#     beta_prime = beta / np.sqrt(norm)
#
#     # RETURN A VECTOR
#     return alpha_prime * ket_0 + beta_prime * ket_1
