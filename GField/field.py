# double sized exp to get rid of % operation
exp = [0] * 512
log = [0] * 256

# GF(2^8) multiplication is the same xor operation
def add(x, y):
    return x ^ y

# simple multiplication operation
def simple_multiply(x, y):
    value = 0
    # table multiplication with xor instead of +
    # because of GF(2^8)
    for i in range(8):
        if x & (1 << i):
            value ^= (y << i)

    # modular reduction
    # 100011101 prime in GF(2^8)
    prime = 0b100011101
    for i in range(16, 7, -1):
        if value & (1 << i):
            value ^= (prime << (i - 8))

    return value

# fill of constant arrays exp, log
# to make fast multiply operation
def initial_fill():
    global exp, log
    current = 1
    # 2 is primitive in GF(2^8)
    for ind in range(255):
        exp[ind] = current
        log[current] = ind
        current = simple_multiply(current, 2)

    # second half of exp is the same as first
    for ind in range(255, 512):
        exp[ind] = exp[ind - 255]

# each number = 2^t -> a * b = 2^x * 2^y = 2^(x + y)
def multiply(x, y):
    # 0 has no log
    if x == 0 or y == 0:
        return 0

    global exp, log
    # using double sized exp array
    return exp[log[x] + log[y]]

# division similar to multiplication
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    # 0 has no log
    if x == 0:
        return 0

    return exp[255 + log[x] - log[y]]

# x^y, y >= 0
def pow(x, y):
    return exp[(log[x] * y) % 255]

# x^(-1)
def inverse(x):
    return exp[255 - log[x]]
