from PIL import Image
from .detect import Detection

def decode(name='temp.png'):
    img = Detection(name)
    img.detect()

    def frequent(a):
        return sorted(a)[len(a) // 2]

    # setting angle colors
    t = [(0, 0, 0) for i in range(4)]
    usd = [[False] * 23 for i in range(23)]
    arr = [[0] * 23 for i in range(23)]
    for i in range(8):
        for j in range(8):
            usd[i][j] = usd[i][-j - 1] = usd[-i - 1][j] = usd[-i - 1][-j - 1] = True
            
    for i in range(2, 5):
        for j in range(2, 5):
            tmp = [img.get_block(i, j), 
                   img.get_block(i, 23 - j - 1),
                   img.get_block(23 -i - 1, j),
                   img.get_block(23 -i - 1, 23 - j - 1)]
            for k in range(4):
                t[k] = (t[k][0] + tmp[k][0],
                        t[k][1] + tmp[k][1],
                        t[k][2] + tmp[k][2])
    for i in range(4):
        t[i] = (t[i][0] // 9, t[i][1] // 9, t[i][2] // 9)
    
    for i in range(23):
        for j in range(23):
            arr[i][j] = img.find_square(i, j, t)

    length = 0
    length ^= frequent([arr[7][-8 - 1], arr[-8 - 1][-8 - 1], arr[-8 - 1][7]])
    length <<= 2
    length ^= frequent([arr[7][8], arr[-7 - 1][-8 - 1], arr[8][-7 - 1]])
    length <<= 2
    length ^= frequent([arr[8][8], arr[-8 - 1][8], arr[8][-8 - 1]])
    length <<= 2
    length ^= frequent([arr[8][7], arr[-7 - 1][8], arr[-8 - 1][-7 - 1]])
    
    usd[8][7] = usd[-7 - 1][8] = usd[-8 - 1][-7 - 1] = True
    usd[8][8] = usd[-8 - 1][8] = usd[8][-8 - 1] = True
    usd[7][8] = usd[-7 - 1][-8 - 1] = usd[8][-7 - 1] = True
    usd[7][-8 - 1] = usd[-8 - 1][-8 - 1] = usd[-8 - 1][7] = True
    
    bits = 0
    tmp = 0
    for i in range(23):
        for j in range(23):
            if usd[i][j]:
                continue
            bits ^= (arr[i][j] << tmp)
            tmp += 2
    
    msg = []
    for i in range(64):
        msg += [bits & 255]
        bits >>= 8
    msg = msg[::-1]
    return length, msg