# 导入transform，data，io
from skimage import transform,data,io
# 读取图片
image = io.imread("../../imgs/111.jpg")
# 打印图像的原始大小
print(image.shape)
# 按照1/10倍等比例进行缩放
print(transform.rescale(image,0.1).shape)
# 将图像的长缩小为原来的一半，宽缩小为原来的四分之一
print(transform.rescale(image,(0.50,0.25)).shape)
# 将图像放大为原始的两倍
print(transform.rescale(image,2).shape)