from PIL import Image

class Detection:
    def __init__(self, name="temp.png"):
        self.img = Image.open(name)
        (self.w, self.h) = self.img.size

    def detect(self):
        # constants
        col_similar = 60
        col_similar_big = 100
        delta = 0.8

        def get(i, j):
            return self.img.getpixel((i, j))

        def similar(col1, col2, similarity):
            sm = 0
            for i in range(3):
                sm += abs(col1[i] - col2[i])
                if abs(col1[i] - col2[i]) > similarity / 2:
                    return False
            return (sm < similarity)

        def sum_colors(col1, col2):
            return (col1[0] + col2[0], col1[1] + col2[1], col1[2] + col2[2])

        def div_color(col, div):
            return (col[0] / div, col[1] / div, col[2] / div)

        def near(a, b):
            return ((abs(a[0] - b[0]) < 10) and (abs(a[1] - b[1]) < 10))

        # serches for ratio in given row, starting with certain point
        def get_row(cx, cy, ratio):
            left_groups = []
            left_start = []
            right_groups = []
            right_start = []

            last = (-100, -100, -100)
            cur_sum = (0, 0, 0)
            cur_sz = 0
            for col in range(cx, -1, -1):
                curr = get(col, cy)
                if similar(last, curr, col_similar):
                    cur_sum = sum_colors(cur_sum, curr)
                    cur_sz += 1
                else:
                    if cur_sz > 3:
                        left_groups.append((div_color(cur_sum, cur_sz), cur_sz))
                        left_start.append(col + 1)
                    cur_sz = 1
                    cur_sum = (0, 0, 0)

                last = curr
                if len(left_groups) > 3:
                    break
            if cur_sz > 3:
                left_groups.append((div_color(cur_sum, cur_sz), cur_sz))
                left_start.append(col + 1)
            last = (-100, -100, -100)
            cur_sum = (0, 0, 0)
            cur_sz = 0
            for col in range(cx, self.w):
                curr = get(col, cy)
                if similar(last, curr, col_similar):
                    cur_sum = sum_colors(cur_sum, curr)
                    cur_sz += 1
                else:
                    if cur_sz > 3:
                        right_groups.append((div_color(cur_sum, cur_sz), cur_sz))
                        right_start.append(col - cur_sz)
                    cur_sz = 1
                    cur_sum = (0, 0, 0)

                last = curr
                if len(right_start) > 3:
                    break

            if cur_sz > 3:
                right_groups.append((div_color(cur_sum, cur_sz), cur_sz))
                right_start.append(col - cur_sz)

            if len(left_groups) == 0 or len(right_groups) == 0:
                return False

            # print(left_groups)
            # print(right_groups)

            left_start = left_start[::-1]
            left_groups = left_groups[::-1]

            if similar(left_groups[-1][0], right_groups[0][0], col_similar_big):
                right_groups[0] = (right_groups[0][0], right_groups[0][1] + left_groups.pop()[1])
            
            result_groups = []
            result_start = []
            isLeft = True
            right_index = 0
            for i in ratio:
                if i == 3:
                    isLeft = False
                if isLeft:
                    if len(left_groups) == 0:
                        return False
                    result_groups = [left_groups.pop()] + result_groups
                    result_start = [left_start.pop()] + result_start
                else:
                    if right_index >= len(right_groups):
                        return False
                    result_groups += [right_groups[right_index]]
                    result_start += [right_start[right_index]]
                    right_index += 1

            # haha, classic
            groups = result_groups
            start = result_start

            if not (similar(groups[0][0], groups[2][0], col_similar_big) and
                    similar(groups[0][0], groups[4][0], col_similar_big) and 
                    similar(groups[1][0], groups[3][0], col_similar_big)):
                return False
            
            if not (abs(groups[0][1] / groups[1][1] - ratio[0] / ratio[1]) < delta and 
                    abs(groups[1][1] / groups[2][1] - ratio[1] / ratio[2]) < delta and
                    abs(groups[2][1] / groups[3][1] - ratio[2] / ratio[3]) < delta and
                    abs(groups[3][1] / groups[4][1] - ratio[3] / ratio[4]) < delta):
                return False

            ind = 0
            while ratio[ind] != 3:
                ind += 1
            
            # print(start)
            # return start[ind] + groups[ind][1] // 2
            return (start[0], start[-1] + groups[-1][1] - 1)


        # searces for ratio in each column
        def find(ratio, row_ratio):
            res = []
            for col in range(0, self.w):
                temp_groups = []
                last = (-100, -100, -100)
                for row in range(self.h):
                    curr = get(col, row)
                    if similar(last, curr, col_similar):
                        temp_groups[-1] = (sum_colors(temp_groups[-1][0], curr), temp_groups[-1][1] + 1)
                    else:
                        temp_groups.append((curr, 1))
                    last = curr
                
                groups = []
                gr_start = []
                curr = 0
                for g in temp_groups:
                    if g[1] > 3:
                        groups.append((div_color(g[0], g[1]), g[1]))
                        gr_start.append(curr)
                    curr += g[1]
                # print(groups)
                # print(gr_start)

                for i in range(len(groups) - 4):
                    if not (similar(groups[i][0], groups[i + 2][0], col_similar_big) and
                            similar(groups[i][0], groups[i + 4][0], col_similar_big) and 
                            similar(groups[i + 1][0], groups[i + 3][0], col_similar_big)):
                        continue
                    
                    if not (abs(groups[i][1] / groups[i + 1][1] - ratio[0] / ratio[1]) < delta and 
                            abs(groups[i + 1][1] / groups[i + 2][1] - ratio[1] / ratio[2]) < delta and
                            abs(groups[i + 2][1] / groups[i + 3][1] - ratio[2] / ratio[3]) < delta and
                            abs(groups[i + 3][1] / groups[i + 4][1] - ratio[3] / ratio[4]) < delta):
                        continue
                    
                    if ratio[2] == 3:
                        cen_row = gr_start[i + 2] + groups[i + 2][1] // 2
                    else:
                        cen_row = gr_start[i + 3] + groups[i + 3][1] // 2
                    cen_col = get_row(col, cen_row, row_ratio)
                    # print(col, cen_row)
                    # print(cen_col, cen_row)
                    if cen_col:
                        # [left, up, right, bottom]
                        # self.img.putpixel((cen_col[0], cen_row), (0, 0, 0))
                        res += [(cen_col, (gr_start[i], gr_start[i + 4] + groups[i + 4][1] - 1))]
                    # return
            return res
        angles = find([1, 1, 3, 1, 1], [1, 1, 3, 1, 1])
        # print(angles)

        self.lu = (1e5, 1e5)
        self.ld = (1e5, -1)
        self.ru = (-1, 1e5)
        self.rd = (-1, -1)
        for an in angles:
            for i in range(2):
                for j in range(2):
                    t = (an[0][i], an[1][j])
                    if near(self.lu, t) or near(self.ld, t) or \
                       near(self.ru, t) or near(self.rd, t):
                        continue
                    if t[0] <= self.lu[0] and t[1] <= self.lu[1]:
                        self.lu = t
                    elif t[0] <= self.ld[0] and t[1] >= self.ld[1]:
                        self.ld = t
                    elif t[0] >= self.ru[0] and t[1] <= self.ru[1]:
                        self.ru = t
                    elif t[0] >= self.rd[0] and t[1] >= self.rd[1]:
                        self.rd = t
        self.wth = (self.ru[0] - self.lu[0], self.ru[1] - self.lu[1])
        self.hht = (self.ld[0] - self.lu[0], self.ld[1] - self.lu[1])
        self.w = (self.wth[0] ** 2 + self.wth[1] ** 2) ** 0.5
        self.h = (self.hht[0] ** 2 + self.hht[1] ** 2) ** 0.5
        # self.img.save("decoded.png")

    def get_block(self, i, j):
        def p_add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        def p_mult(a, x):
            return (a[0] * x, a[1] * x)     

        def get_pixel(a):
            return self.img.getpixel((int(a[0]), int(a[1])))
        
        r = g = b = 0
        cur = 0
        for x in range(int(self.w / 23 * i), int(self.w / 23 * (i + 1))):
            for y in range(int(self.h / 23 * j), int(self.h / 23 * (j + 1))):
                p = p_add(self.lu, p_add(p_mult(self.wth, x / self.w), p_mult(self.hht, y / self.h)))
                col = get_pixel(p)
                r += col[0]
                g += col[1]
                b += col[2]
                cur += 1

        return (r // cur, g // cur, b // cur)
        