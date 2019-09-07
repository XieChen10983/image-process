# coding=gbk
import os
import numpy as np
import cv2 as cv
from PIL import Image


def cut_image(Batch: np.ndarray, Sub_image_size=64, Save=True, Save_path='./cut_image'):
    """
    此函数将Batch中的图像按列按行剪切成想要的大小，并决定是否保存到相应的路径中。若不保存，则返回相应的ndarray。
    :param Batch:需要剪切的图像集，其类型为ndarray类型，其大小类型为[batch, width, height, channel]
    :param Sub_image_size:需剪切成的形状大小。
    :param Save:决定是否要保存成图像。
    :param Save_path:图像保存的位置
    :return:若不保存成图像，则返回剪切之后的数据集，包括图像本身的集合和图像所在位置的信息集合。
    """
    Image_set = []  # 用来存放子图像的列表
    Image_information_set = []  # 用来存放子图像的位置信息的列表，图像信息包括该子图像所在哪张父图像，在父图像的哪行和哪列。
    for image_num, image in enumerate(Batch):
        row, col, channel = image.shape
        for row_num in range(0, row, Sub_image_size):
            for col_num in range(0, col, Sub_image_size):
                Sub_image = image[row_num:row_num+Sub_image_size, col_num:col_num+Sub_image_size, :]
                Image_set.append(Sub_image)
                Image_information_set.append(np.array([image_num, row_num, col_num]))
    Image_set = np.array(Image_set)
    Image_information_set = np.array(Image_information_set)
    if Save:
        if not os.path.exists(Save_path):
            os.mkdir(save_path)
        print('正在保存图像...')
        for num, information in enumerate(Image_information_set):
            cv.imwrite(Save_path + '/image%d_row%d_col%d.png' %
                       (information[0], information[1], information[2]), img=Image_set[num])
        print('保存完毕。')
    else:
        return Image_set, Image_information_set


Data = Image.open('C:/Users/Administrator/Desktop/1.png').resize((1024, 1024))
batch = np.array(Data)[:, :, :3].reshape((1, 1024, 1024, 3))
save_path = 'B:/cut_image'
sub_image, _ = cut_image(batch, 64, False)
print(sub_image.shape)
