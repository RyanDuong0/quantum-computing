import numpy as np

def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (np.array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        np.array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES

    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES

    #store first state as "state" is an array with two vectors
    state_1 = state[0]

    #calculate one of the probabilities, if we did the other the logic of appending 0 and 1 would flip
    probability_1 = np.abs(state_1) ** 2
    ans = np.empty(num_meas) #initialise an empty numpy array of size num_meas to store the 0 and 1

    for i in range(num_meas):
        randomNum = np.random.rand() #generate a number between 0 and 1
        if randomNum < probability_1: #for each number generated, compare with the probability
            ans[i] = 0
        else:
            ans[i] = 1

    #e.g. 64% of random numbers fall in the first region -> 0
    #36% fall in the second region -> 1

    # pennylane:
    #     p_alpha = np.abs(state[0]) ** 2
    #     p_beta = np.abs(state[1]) ** 2
    #
    #     # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES
    #     meas_outcome = np.random.choice([0, 1], p=[p_alpha, p_beta], size=num_meas)
    #
    #     return meas_outcome

    return ans
