# 导入io和data模块
from skimage import io,data
# 导入data_dir用于指定skimage图像数据的路径
from skimage import data_dir

# 加载哈勃望远镜图像
img = data.hubble_deep_field()
# 显示图像
io.imshow(img)
# 显示所有内容
io.show()
print(data_dir)