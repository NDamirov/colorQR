from PIL import Image

def detect(name="temp.png"):
    img = Image.open(name)
    (w, h) = img.size

    # constants
    col_similar = 20
    delta = 0.1

    def get(i, j):
        nonlocal img
        return img.getpixel((i, j))

    def similar(col1, col2):
        for i in range(3):
            if abs(col1[i] - col2[i]) > col_similar:
                return False
        return True
    
    def find(ratio):
        for col in range(w):
            temp_groups = []
            last = (-100, -100, -100)
            for row in range(h):
                curr = get(col, row)
                if similar(last, curr):
                    temp_groups[-1] = (temp_groups[-1][0], temp_groups[-1][1] + 1)
                else:
                    temp_groups.append((curr, 1))
                last = curr
            
            groups = []
            for g in temp_groups:
                if g[1] > 3:
                    groups.append(g)

            for i in range(len(groups) - 5):
                if not (similar(groups[i][0], groups[i + 2][0]) and
                        similar(groups[i][0], groups[i + 4][0]) and 
                        similar(groups[i + 1][0], groups[i + 3][0]) and
                        similar(groups[i + 1][0], groups[i + 5][0])):
                    continue
                
                if not (abs(groups[i][1] / groups[i + 1][1] - ratio[0] / ratio[1]) < delta or 
                        abs(groups[i + 1][1] / groups[i + 2][1] - ratio[1] / ratio[2]) < delta or
                        abs(groups[i + 2][1] / groups[i + 3][1] - ratio[2] / ratio[3]) < delta or
                        abs(groups[i + 3][1] / groups[i + 4][1] - ratio[3] / ratio[4]) < delta):
                    continue
                for t in range(i, i + 5):
                    print(groups[t])
                return
    find([1, 1, 3, 1, 1, 1])