# Probabilities from the tables

# Priors
P_E = {True: 0.4, False: 0.6}   # +e, -e
P_M = {True: 0.1, False: 0.9}   # +m, -m

# P(S | E, M)
P_S = {
    (True, True): {True: 1.0, False: 0.0},   # +e, +m
    (True, False): {True: 0.8, False: 0.2},  # +e, -m
    (False, True): {True: 0.3, False: 0.7},  # -e, +m
    (False, False): {True: 0.1, False: 0.9}, # -e, -m
}

# P(B | M)
P_B = {
    True: {True: 1.0, False: 0.0},   # +m
    False: {True: 0.1, False: 0.9},  # -m
}

# (a) P(-e, -s, -m, -b)
a = P_E[False] * P_M[False] * P_S[(False, False)][False] * P_B[False][False]
print("(a):", a)

# (b) P(b) = sum over M
b = P_B[True][True] * P_M[True] + P_B[False][True] * P_M[False]
print("(b):", b)

# (c) P(m | b) = P(b|m)P(m) / P(b)
c = (P_B[True][True] * P_M[True]) / b
print("(c):", c)

# (d) P(m | s, b, e)
# proportional to: P(m) * P(s|e,m) * P(b|m)
num_true = P_M[True] * P_S[(True, True)][True] * P_B[True][True]
num_false = P_M[False] * P_S[(True, False)][True] * P_B[False][True]
d = num_true / (num_true + num_false)
print("(d):", d)

# (e) P(e | m) = P(e) since E ⟂ M
e = P_E[True]
print("(e):", e)
