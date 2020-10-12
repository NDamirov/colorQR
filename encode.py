import sys
import RSCode
import Picture
tp = int(input('Print type\n'))
msg = input('Print message\n')
if len(msg) > 54:
    print('Too long')
    sys.exit(0)

enc = [len(msg), tp]
msg = [ord(c) for c in msg] + [0] * (54 - len(msg))
enc += RSCode.encode(msg, 10)
Picture.generate(enc)