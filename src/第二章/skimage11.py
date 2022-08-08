# 导入io,data,color模块
from skimage import io,data,color
# 加载小猫图片
image = data.chelsea()
# 使用color.rgb2gray()将RGB图像转换为灰度图像
image_gray = color.rgb2gray(image)
# 显示图像
io.imshow(image_gray)
io.show()