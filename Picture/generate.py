from PIL import Image
from random import randint

def get_color(x):
    if (x == 0):
        return (70, 70, 70)
    if (x == 1):
        return (140, 140, 140)
    if (x == 2):
        return (210, 210, 210)
    return (0, 0, 0)



# msg = [length, type, message]
def generate(msg, name='temp.png'):
    # generate field and image
    arr = [[-1] * 23 for i in range(23)]
    sz = 30
    img = Image.new('RGB', (sz * 23, sz * 23), 'white')


    def set_pixel(i, j, col):
        nonlocal img, sz
        for x in range(i * sz, (i + 1) * sz):
            for y in range(j * sz, (j + 1) * sz):
                img.putpixel((x, y), col)

    # unite all numbers in one
    bits = 0
    for i in msg[2:]:
        bits <<= 8
        bits += i
    # generate angles
    # TODO: fix
    for i in range(8):
        for j in range(8):
            arr[i][j] = 0
            arr[i][-j - 1] = 1
            arr[-i - 1][j] = 2
            arr[-i - 1][-j - 1] = 3

    # set length squares
    arr[8][7] = arr[-7 - 1][8] = arr[-8 - 1][-7 - 1] = (msg[0] & 3)
    arr[8][8] = arr[-8 - 1][8] = arr[8][-8 - 1] = ((msg[0] >> 2) & 3)
    arr[7][8] = arr[-7 - 1][-8 - 1] = arr[8][-7 - 1] = ((msg[0] >> 4) & 3)
    arr[7][-8 - 1] = arr[-8 - 1][-8 - 1] = arr[-8 - 1][7] = ((msg[0] >> 6) & 3)

    # TODO: set type squares

    # set everything else
    for i in range(23):
        for j in range(23):
            if arr[i][j] != -1:
                continue
            arr[i][j] = bits & 3
            bits >>= 2

    # create image and save it
    for i in range(23):
        for j in range(23):
            set_pixel(i, j, get_color(arr[i][j]))

    img.save(name)