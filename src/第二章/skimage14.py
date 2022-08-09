# 导入data,io,color
from skimage import data,io,color
# 导入matplotlib和mpl
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置字体以及坐标轴
mpl.rcParams['font.sans-serif'] = "Microsoft YaHei"
mpl.rcParams['axes.unicode_minus'] = False
# 读取图像
img = io.imread("../../imgs/111.jpg")
# 使用rgb2hsv()将其转换为HSV色彩空间
img_hsv = color.rgb2hsv(img)
# 使用plt.subplots()创建一个多子图窗口
fig,axes = plt.subplots(2,2,figsize=(8,8))

# 使用ravel()函数将axes进行拆分
ax0,ax1,ax2,ax3 = axes.ravel()

# 使用axes.imshow()显示图像，并使用axes.title()为子图添加标题
ax0.imshow(img)
ax0.set_title('原始图像')

ax1.imshow(img_hsv[:,:,0])
ax1.set_title('H通道')

ax2.imshow(img_hsv[:,:,1])
ax2.set_title('S通道')

ax3.imshow(img_hsv[:,:,2])
ax2.set_title('V通道')

# 使用fig.tight_layout()函数将布局设置为紧凑结构
fig.tight_layout()

plt.show()