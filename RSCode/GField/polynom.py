from .field import *

# everything in GF(2^8)
# each polynom is array of coefficients:
# [a1, a2, a3,.., an] = an + a(n - 1)x + ... + a1 * (x^(n - 1))

# sum of two polynoms
def pol_add(p, q):
    val = [0] * max(len(p), len(q))

    # len(val) - len(p) - is shift, because of polynom array order
    for i in range(len(p)):
        val[i + len(val) - len(p)] = p[i]
    # addition mod 2 because of GF(2^8)
    for i in range(len(q)):
        val[i + len(val) - len(q)] ^= q[i]

    return val

# polynom * scale
def pol_scale(p, x):
    val = list(p)
    # each coefficient is multiplied
    for i in range(len(p)):
        val[i] = multiply(p[i], x)
    return val

# polynom * polynom
def pol_multiply(p, q):
    # deg(p) = len(p) - 1
    # deg(q) = len(q) - 1
    # deg(pq) = len(p) + len(q) - 2 -> 
    # max val length = len(p) + len(q) - 1
    val = [0] * (len(p) + len(q) - 1)

    for i in range(len(p)):
        for j in range(len(q)):
            # xor for sum in GF(2^8)
            val[i + j] ^= multiply(p[i], q[j])
    
    return val

# polynom / polynom
# p / q
# returns quotient and remainder
# synthetic division technique 
def pol_div(p, q):
    result = list(p)
    for i in range(len(p) - len(q) + 1):
        temp = result[i]
        if temp != 0:
            for j in range(1, len(q)):
                if q[j] != 0:
                    result[i + j] ^= multiply(q[j], temp)
    sep = -len(q) + 1
    return result[:sep], result[sep:]

# get p(x)
def pol_get(p, x):
    res = p[0]
    # p(x) = (((p[0] * x) + p[1]) * x).... + p[len(p) - 1]
    # called Horner's method
    for i in range(1, len(p)):
        res = multiply(res, x) ^ p[i]

    return res