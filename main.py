import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 转灰度图
img = Image.open('test.png')
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
