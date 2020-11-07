import Picture
import RSCode
length, msg = Picture.decode()
msg = RSCode.simple_fix(msg, 64 - length)
msg = msg[:length]
msg = bytes(msg)
print(msg.decode())