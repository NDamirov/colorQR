from RSCode import *
from random import randint
msg_in = [ randint(0, 255) for i in range(54) ]
msg = encode(msg_in, 10)
print(msg)
# Errors
for i in range(5):
    msg[i] = 0
print(simple_fix(msg, 10))