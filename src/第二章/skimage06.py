# 导入模块
from skimage import io,data
# 读取小猫图片
img = data.chelsea()
# 输出图片的R（红色通道）的第20行，30列的像素值
pixel = img[20,30,1]
print(pixel)
# 显示猫图片的红色通道的图片
R = img[:,:,0]
# 显示图像
io.imshow(R)
# 显示内容
io.show()