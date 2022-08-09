# 导入transform,io模块
from skimage import transform,io
# 导入matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置字体和坐标系
mpl.rcParams['font.sans-serif'] = "MicroSoft YaHei"
mpl.rcParams['axes.unicode_minus'] = False
# 读取图片
img = io.imread("../../imgs/111.jpg")
# 打印原始图片大小
print(img.shape)
# 使用transform.rotate()函数对图像进行旋转处理
img1 = transform.rotate(img,60)
print(img1.shape)
# 使用transform.rotate()函数，并同时同时传入resize函数自适应重新匹配大小
img2 = transform.rotate(img,30,resize=True)
print(img2.shape)
# 创建figure()
plt.figure('缩放')
plt.subplot(121)
plt.title('旋转60度')
plt.imshow(img1,plt.cm.gray)

plt.subplot(122)
plt.title('旋转30度')
plt.imshow(img2,plt.cm.gray)

plt.show()