# 导入io和data模块
from skimage import data,io
# 导入matplotlib.pyplot
import matplotlib.pyplot as plt
from pylab import mpl
# 修改字体以及坐标系坐标样式
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False
# 读取图片
img = io.imread("../../imgs/111.jpg")

# 使用plt.figure()创建一个窗口，名为cat
plt.figure(num='cat',figsize=(8,8))

# 使用plt.subplot()创建一个2x2的图像子图窗口，并进行绘制第一张图
plt.subplot(2,2,1)
plt.title('原始图像')
plt.imshow(img)

# 绘制第二张图
plt.subplot(2,2,2)
plt.title("R通道")
plt.imshow(img[:,:,0])

# 绘制第三张图
plt.subplot(2,2,3)
plt.title("G通道")
plt.imshow(img[:,:,1])

# 绘制第四张图
plt.subplot(2,2,4)
plt.title("B通道")
plt.imshow(img[:,:,2])

plt.show()