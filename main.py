import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def encode(image):
    img = Image.open(image)
    img = img.convert('L')
    threshold = 162
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img = img.point(table, '1')
    nd_img = 1 - np.asarray(img)

    x_len = nd_img.shape[1]
    y_len = nd_img.shape[0]
    N = 0
    for x in range(x_len):
        for y in range(y_len):
            if nd_img[y][x] == True:
                N += 2 ** (y_len * x + y)
    return x_len, y_len, N


def decode(x_len, y_len, N):
    res = []
    for x in range(x_len):
        for y in range(y_len):
            # 等价于Tupper公式，所以为嘛我不直接用？因为Wolframe有字数限制啊蠢！！！
            res.append((N // (2 ** (17 * x + y))) % 2)
    return np.reshape(np.asarray(res), [x_len, y_len])


x_len, y_len, N = encode('input.png')
img = decode(x_len, y_len, N)
plt.imshow(img.T)
plt.savefig('reconstruct.png', dpi=100)
# N = 363883192643747563551837003640319734361344919275045642456821576727758849680568610655472869095310579713145739970424055134873763100371507195057705167542045163719218909595628492414168137184906417342910102653140415989331655334015224850096808876512724614412125304789667705755361037858442357839702447250599397533469781429518525840998580535065707655630489235686305490104581844257613151364624778494791996409551327634379918465194360631479718516738136853559041943410590970590857067105094419349504
