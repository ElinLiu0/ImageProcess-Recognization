# 导入io和data模块
from skimage import io,data
# 读取小猫图片
img = data.chelsea()
# 对图像进行裁剪
cutted = img[150:250,200:300,:]
# 显示图像
io.imshow(cutted)
io.show()