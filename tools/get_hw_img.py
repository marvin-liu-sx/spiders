# _*_coding:utf-8_*_
# Time : 2018/6/19 10:48
# User : yy-zhangcong2
# Email: zhangcong2@yy.com
# Python: 3.6.4

"""Documentation comments"""

from io import BytesIO
import urllib.request
from PIL import Image


class Size:
    def __init__(self):
        pass

    @staticmethod
    def get_size(img_url):
        response = urllib.request.urlopen(img_url)
        tmp_img = BytesIO(response.read())
        img = Image.open(tmp_img)
        return img.size[0], img.size[1]


if __name__ == '__main__':
    w, h = Size.get_size(
        'http://image1.pearvideo.com/cont/20180507/cont-1339103-11209369.jpg')
    print(w, h)
