# 导入io和data模块
from skimage import io,data
# 调用dataset中的哈勃望远镜
img = data.hubble_deep_field()
# 打印图像信息
imgData = {
    'ImageType':type(img),
    'ImageShape':img.shape,
    'ImageWidth':img.shape[0],
    'ImageHeight':img.shape[1],
    'ColorChannels':img.shape[2],
    'ImagePixels':img.size,
    'ImagePixelMax':img.max(),
    'ImagePixelMin':img.min(),
    'ImagePixelMean':img.mean()
}
print(imgData)