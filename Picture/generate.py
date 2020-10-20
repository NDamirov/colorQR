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
    
    def set_angles():
        nonlocal arr
        for i in range(0, 23):
            for j in range (0, 23):
                if i == 0 and j == 0:
                    arr[i][j] = 0
                if i == 0 and j == 1:
                    arr[i][j] = 0
                if i == 0 and j == 2:
                    arr[i][j] = 0
                if i == 0 and j == 3:
                    arr[i][j] = 0
                if i == 0 and j == 4:
                    arr[i][j] = 0
                if i == 0 and j == 5:
                    arr[i][j] = 0
                if i == 0 and j == 6:
                    arr[i][j] = 0
                if i == 0 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 1 and j == 0:
                    arr[i][j] = 0
                if i == 1 and j == 1:
                    arr[i][j] = 1
                if i == 1 and j == 2:
                    arr[i][j] = 1
                if i == 1 and j == 3:
                    arr[i][j] = 1
                if i == 1 and j == 4:
                    arr[i][j] = 1
                if i == 1 and j == 5:
                    arr[i][j] = 1
                if i == 1 and j == 6:
                    arr[i][j] = 0
                if i == 1 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 2 and j == 0:
                    arr[i][j] = 0
                if i == 2 and j == 1:
                    arr[i][j] = 1
                if i == 2 and j == 2:
                    arr[i][j] = 0
                if i == 2 and j == 3:
                    arr[i][j] = 0
                if i == 2 and j == 4:
                    arr[i][j] = 0
                if i == 2 and j == 5:
                    arr[i][j] = 1
                if i == 2 and j == 6:
                    arr[i][j] = 0
                if i == 2 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 3 and j == 0:
                    arr[i][j] = 0
                if i == 3 and j == 1:
                    arr[i][j] = 1
                if i == 3 and j == 2:
                    arr[i][j] = 0
                if i == 3  and j == 3:
                    arr[i][j] = 0
                if i == 3 and j == 4:
                    arr[i][j] = 0
                if i == 3 and j == 5:
                    arr[i][j] = 1
                if i == 3 and j == 6:
                    arr[i][j] = 0
                if i == 3 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 4 and j == 0:
                    arr[i][j] = 0
                if i == 4 and j == 1:
                    arr[i][j] = 1
                if i == 4 and j == 2:
                    arr[i][j] = 0
                if i == 4 and j == 3:
                    arr[i][j] = 0
                if i == 4 and j == 4:
                    arr[i][j] = 0
                if i == 4 and j == 5:
                    arr[i][j] = 1
                if i == 4 and j == 6:
                    arr[i][j] = 0
                if i == 4 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 5 and j == 0:
                    arr[i][j] = 0
                if i == 5 and j == 1:
                    arr[i][j] = 1
                if i == 5 and j == 2:
                    arr[i][j] = 1
                if i == 5 and j == 3:
                    arr[i][j] = 1
                if i == 5 and j == 4:
                    arr[i][j] = 1
                if i == 5 and j == 5:
                    arr[i][j] = 1
                if i == 5 and j == 6:
                    arr[i][j] = 0
                if i == 5 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 6 and j == 0:
                    arr[i][j] = 0
                if i == 6 and j == 1:
                    arr[i][j] = 0
                if i == 6 and j == 2:
                    arr[i][j] = 0
                if i == 6 and j == 3:
                    arr[i][j] = 0
                if i == 6 and j == 4:
                    arr[i][j] = 0
                if i == 6 and j == 5:
                    arr[i][j] = 0
                if i == 6 and j == 6:
                    arr[i][j] = 0
                if i == 6 and j == 7:
                    arr[i][j] = 1
                    ###############
                if i == 7 and j == 0:
                    arr[i][j] = 1
                if i == 7 and j == 1:
                    arr[i][j] = 1
                if i == 7 and j == 2:
                    arr[i][j] = 1
                if i == 7 and j == 3:
                    arr[i][j] = 1
                if i == 7 and j == 4:
                    arr[i][j] = 1
                if i == 7 and j == 5:
                    arr[i][j] = 1
                if i == 7 and j == 6:
                    arr[i][j] = 1
                if i == 7 and j == 7:
                    arr[i][j] = 1
                    ###############
                    ###############
                    ###############
                if i == 0 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 0 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 2 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 3 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 4 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 5 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 6 + 15:
                    arr[i][j] = 1
                if i == 0 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 1 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 1 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 1 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 2 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 2 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 2 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 2 and j == 3 + 15:
                    arr[i][j] = 1
                if i == 2 and j == 4 + 15:
                    arr[i][j] = 1
                if i == 2 and j == 5 + 15:
                    arr[i][j] = 1
                if i == 2 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 2 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 3 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 3 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 3 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 3  and j == 3 + 15:
                    arr[i][j] = 1
                if i == 3 and j == 4 + 15:
                    arr[i][j] = 1
                if i == 3 and j == 5 + 15:
                    arr[i][j] = 1
                if i == 3 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 3 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 4 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 4 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 4 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 4 and j == 3 + 15:
                    arr[i][j] = 1
                if i == 4 and j == 4 + 15:
                    arr[i][j] = 1
                if i == 4 and j == 5 + 15:
                    arr[i][j] = 1
                if i == 4 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 4 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 5 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 5 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 5 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 6 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 6 and j == 1 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 2 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 3 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 4 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 5 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 6 + 15:
                    arr[i][j] = 1
                if i == 6 and j == 7 + 15:
                    arr[i][j] = 1
                    ###############
                if i == 7 and j == 0 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 7 and j == 7 + 15:
                    arr[i][j] = 3
                        ###############
                        ###############
                        ###############
                if i == 0 + 15 and j == 0:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 2:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 3:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 4:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 6:
                    arr[i][j] = 0
                if i == 0 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 1 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 1:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 2:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 3:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 4:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 5:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 2 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 2 + 15 and j == 2:
                    arr[i][j] = 0
                if i == 2 + 15 and j == 3:
                    arr[i][j] = 0
                if i == 2 + 15 and j == 4:
                    arr[i][j] = 0
                if i == 2 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 2 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 3 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 3 + 15 and j == 2:
                    arr[i][j] = 2
                if i == 3 + 15  and j == 3:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 4:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 3 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 4 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 4 + 15 and j == 2:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 3:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 4:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 4 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 5 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 5 + 15 and j == 2:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 3:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 4:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 5 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 6 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 1:
                    arr[i][j] = 0
                if i == 6 + 15 and j == 2:
                    arr[i][j] = 0
                if i == 6 + 15 and j == 3:
                    arr[i][j] = 0
                if i == 6 + 15 and j == 4:
                    arr[i][j] = 0
                if i == 6 + 15 and j == 5:
                    arr[i][j] = 0
                if i == 6 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                if i == 7 + 15 and j == 0:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 1:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 2:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 3:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 4:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 5:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 6:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 7:
                    arr[i][j] = 0
                    ###############
                    ###############
                    ###############
                if i == 0 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 1 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 3 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 4 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 5 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 0 + 15 and j == 7 + 15:
                    arr[i][j] = 2
                    ###############
                if i == 1 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 1 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 1 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 2 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 2 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 3 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 4 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 5 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 2 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 3 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 3 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 3 + 15  and j == 3 + 15:
                    arr[i][j] = 3
                if i == 3 + 15 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 3 + 15 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 3 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 3 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 4 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 4 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 4 + 15 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 4 + 15 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 4 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 4 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 5 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 5 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 5 + 15 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 5 + 15 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 5 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 5 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 6 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 6 + 15 and j == 2 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 3 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 4 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 5 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 6 + 15:
                    arr[i][j] = 2
                if i == 6 + 15 and j == 7 + 15:
                    arr[i][j] = 3
                    ###############
                if i == 7 + 15 and j == 0 + 15:
                    arr[i][j] = 2
                if i == 7 + 15 and j == 1 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 2 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 3 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 4 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 5 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 6 + 15:
                    arr[i][j] = 3
                if i == 7 + 15 and j == 7 + 15:
                    arr[i][j] = 3

    # unite all numbers in one
    bits = 0
    for i in msg[2:]:
        bits <<= 8
        bits += i
    # generate angles
    set_angles()

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