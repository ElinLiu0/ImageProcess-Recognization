# 导入io,data和color模块
from skimage import io,data,color
# 读取小猫图片
img = data.chelsea()
# 使用color.rgb2gray()将图片转换为灰度图片
img_gray = color.rgb2gray(img)
# 获取长和宽
rows,cols = img_gray.shape
# 对长，宽进行循环
for x in range(rows):
    for y in range(cols):
        # 如果当灰度图像的[X,Y]灰度值大于0.5时，则将其覆盖为1
        if img_gray[x,y] > 0.5:
            img_gray[x,y] = 1
        else:
            img_gray[x,y] = 0
io.imshow(img_gray)
io.show()