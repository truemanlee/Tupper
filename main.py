import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 转灰度图
img = Image.open('input.png')
img = img.convert('L')
threshold = 162
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
img = img.point(table, '1')
nd_img = np.asarray(img)

x_len = nd_img.shape[1]
y_len = nd_img.shape[0]
N = 0
for x in range(x_len):
    for y in range(y_len):
        if nd_img[y][x] == True:
            N += 2 ** (y_len * x + y)
def get_img(x_len, y_len, N):
    res = []
    for x in range(x_len):
        for y in range(y_len):
            # 等价于Tupper公式，所以为嘛我不直接用？因为Wolframe有字数限制啊蠢！！！
            res.append((N // (2 ** (17 * x + y))) % 2)
    return np.reshape(np.asarray(res), [x_len, y_len])
img = get_img(x_len, y_len, N)
img = (1 - img) * 255
plt.imshow(img.T)
plt.savefig('reconstruct.png', dpi=100)
