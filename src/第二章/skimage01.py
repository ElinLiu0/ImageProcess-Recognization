# 导入skimage下data和io模块
from skimage import data,io
# 创建io操作图像流
img = io.imread('../../imgs/111.jpg')
# 调用io.imshow()显示图像
io.imshow(img)
# io.show()显示所用内容
io.show()