# 导入skimage data和io模块
from skimage import data,io
# 使用io.imread()读取图像文件，另外使用as_gray指定图像加载是否以灰度模式读取
img = io.imread('../../imgs/123.jpg',as_gray=True)
# 使用io.imshow()展示图像
io.imshow(img)
# 使用io.show()显示窗口
io.show()