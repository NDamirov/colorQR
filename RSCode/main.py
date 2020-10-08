from .GField import *

# generator polynom for Reed-Solomon code
# (x - a^0)(x - a^1)...(x - a^(n - 1)) 
# a - primitive element (2 for GF(2^8))
def gen_pol(n):
    # pol = [1], because [1] is identity element
    pol = [1]
    for i in range(n):
        # 0 ^ f_pow(2, i) = f_pow(2, i) = -f_pow(2, i)
        # because of GF(2^8)
        pol = pol_multiply(pol, [1, f_pow(2, i)])
    return pol

# simple encoding algorithm
# TODO: make it faster
# len(msg) + add must be <= 255 because of GF(2^8)
def encode(msg, add):
    res, rem = pol_div(msg + [0] * add, 
                       gen_pol(add))
    msg += rem
    return msg

# counts syndrome polynom
# must be 0 at first <add> values: a^i, a = 2
def syndrome(msg, add):
    synd = [0] * (add + 1)
    for i in range(add):
        synd[i + 1] = pol_get(msg, f_pow(2, i))
    return synd