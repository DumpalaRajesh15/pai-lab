# Prior probabilities
P_R = {True: 0.2, False: 0.8}

# Conditional probability P(S | R)
P_S_given_R = {
    True: {True: 0.01, False: 0.99},
    False: {True: 0.4, False: 0.6}
}

# Conditional probability P(G | S, R)
P_G_given_SR = {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.9, False: 0.1},
    (False, True): {True: 0.8, False: 0.2},
    (False, False): {True: 0.0, False: 1.0}
}

# Compute P(R ∧ G)
def joint_R_G(r):
    total = 0
    for s in [True, False]:
        total += (
            P_G_given_SR[(s, r)][True] *
            P_S_given_R[r][s] *
            P_R[r]
        )
    return total

# Compute P(G)
def prob_G():
    total = 0
    for r in [True, False]:
        for s in [True, False]:
            total += (
                P_G_given_SR[(s, r)][True] *
                P_S_given_R[r][s] *
                P_R[r]
            )
    return total

# Final probability P(R | G)
P_RG = joint_R_G(True)
P_G = prob_G()

P_R_given_G = P_RG / P_G

print("P(R=True | G=True) =", round(P_R_given_G, 4))
print("P(R=True | G=True) =", round(P_R_given_G * 100, 2), "%")
