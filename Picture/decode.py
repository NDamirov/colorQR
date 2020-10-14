from PIL import Image

def decode(name='temp.png'):
    img = Image.open(name)
    (w, h) = img.size

    # gives average color of (i, j) square
    def get_pixel(i, j):
        nonlocal img, w, h
        amount = 0
        r = g = b = 0
        for x in range(w * i // 23, w * (i + 1) // 23):
            for y in range(h * j // 23, h * (j + 1) // 23):
                amount += 1
                curr_col = img.getpixel((x, y))
                r += curr_col[0]
                g += curr_col[1]
                b += curr_col[2]
        return (r // amount, g // amount, b // amount)

    # searches for closest color
    def find(col):
        nonlocal t
        mn = 255 * 3
        res = 0
        for i in range(4):
            tmp = 0
            for j in range(3):
                tmp += abs(t[i][j] - col[j])
            if tmp < mn:
                res = i
                mn = tmp

        return res
    
    # searches for closest color of square
    def find_square(i, j):
        nonlocal img, w, h
        t = [0] * 4
        for x in range(w * i // 23, w * (i + 1) // 23):
            for y in range(h * j // 23, h * (j + 1) // 23):
                t[find(img.getpixel((x, y)))] += 1
        res = 0
        for i in range(1, 4):
            if t[i] > t[res]:
                res = i

        return res
    
    def frequent(a):
        return sorted(a)[len(a) // 2]

    # setting angle colors
    t = [(0, 0, 0) for i in range(4)]
    usd = [[False] * 23 for i in range(23)]
    arr = [[0] * 23 for i in range(23)]
    for i in range(8):
        for j in range(8):
            tmp = [get_pixel(i, j), 
                   get_pixel(i, -j - 1),
                   get_pixel(-i - 1, j),
                   get_pixel(-i - 1, -j - 1)]
            usd[i][j] = usd[i][-j - 1] = usd[-i - 1][j] = usd[-i - 1][-j - 1] = True
            for k in range(4):
                t[k] = (t[k][0] + tmp[k][0],
                        t[k][1] + tmp[k][1],
                        t[k][2] + tmp[k][2])
    for i in range(4):
        t[i] = (t[i][0] // 64, t[i][1] // 64, t[i][2] // 64)
    
    for i in range(23):
        for j in range(23):
            arr[i][j] = find_square(i, j)

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