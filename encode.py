import sys
import RSCode
import Picture
tp = int(input('Print type\n'))
msg_t = input('Print message\n')
msg_t = msg_t.encode()
msg = []
for i in range(len(msg_t)):
    msg.append(msg_t[i])

if len(msg) > 54:
    print('Too long')
    sys.exit(0)

enc = [len(msg), tp]
enc += RSCode.encode(msg, 64 - len(msg))
Picture.generate(enc)