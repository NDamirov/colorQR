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
    # synd = [0] * (add + 1)
    # for i in range(add):
    #     synd[i + 1] = pol_get(msg, f_pow(2, i))
    synd = [0] * add
    for i in range(add):
        synd[i] = pol_get(msg, f_pow(2, i))
    return synd

# checks if message is corrupted
def check(msg, add):
    # values of syndrome polynome can't be < 0
    # because of GF(2^8)
    return (max(syndrome(msg, add)) == 0)

# counts error locator polynom
# Berlekamp-Messey algorithm
# roots of locator polynom are errors
def error_locator(synd):
    err = [1] # locator polynom
    prev = [1] # previous state for algorithm
    add = len(synd) # number of added symbols

    for i in range(add): 
        delta = synd[i]        
        for j in range(1, len(err)):
            delta ^= multiply(err[-j - 1], synd[i - j])
        prev += [0]
        
        if delta == 0:
            continue

        if len(prev) > len(err):
            err, prev = pol_scale(prev, delta), \
                        pol_scale(err, inverse(delta))
        
        err = pol_add(err, pol_scale(prev, delta))
    
    while len(err) > 0 and err[0] == 0: 
        del err[0]
    amount = len(err) - 1
    if amount * 2 > add:
        raise Exception()

    return err

# find errors using locator polynom
# simple brutforce
def _find(loc, msl): # msl = len(msg_in) = len(msg) - add
    amount = len(loc) - 1
    positions = []
    for i in range(msl):
        if pol_get(loc, f_pow(2, i)) == 0:
            positions += [msl - i - 1]
    
    if len(positions) != amount:
        raise Exception()

    return positions


# get positions
def find(msg, add):
    synd = syndrome(msg, add)
    loc = error_locator(synd)
    return _find(loc[::-1], len(msg))

# brutforce fix
def simple_fix(msg, add):
    last = find(msg, add)
    for i in last:
        msg[i] = 0
    last = find(msg, add)
    for i in last:
        msg[i] = 1
    while not check(msg, add):
        last = find(msg, add)
        for i in last:
            msg[i] = multiply(msg[i], 2)
    return msg

