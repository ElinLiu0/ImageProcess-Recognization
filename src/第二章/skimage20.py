# 导入transform,data,io模块
from skimage import transform,data,io
# 导入matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置字体和坐标轴
mpl.rcParams['font.sans-serif'] = "Microsoft YaHei"
mpl.rcParams['axes.unicode_minus'] = False
# 读取图片
img = io.imread("../../imgs/111.jpg")
# 使用transform.resize()函数
dst = transform.resize(img,(80,60))

# 创建窗口
plt.figure('resize')
plt.subplot(121)
plt.title("原始图")
plt.imshow(img,plt.cm.gray)
# 绘制resize后的图像
plt.subplot(122)
plt.title('改变后')
plt.imshow(dst,plt.cm.gray)
plt.show()