import Picture
import RSCode
length, msg = Picture.decode()
msg = RSCode.simple_fix(msg, 64 - length)
res = ''.join(chr(msg[i]) for i in range(length))
print(res)