# 导入io和data模块
from skimage import io,data
# 加载图像
img = data.hubble_deep_field()
# 显示图像
io.imshow(img)
# 显示所有内容
io.show()
# 调用imsave()保存图像文件
io.imsave('hubble_deep_field.jpg',img)