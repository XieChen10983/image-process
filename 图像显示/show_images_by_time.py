# coding=gbk
import os
import matplotlib.pyplot as plt
import cv2 as cv


def show_dir_images(root, time=0.3):
    image_names = os.listdir(root)
    choose = []
    for image_name in image_names:
        if (image_name.split('.')[-1] == 'jpg') or (image_name.split('.')[-1] == 'png'):
            choose.append(image_name)
    image_ab_path = []
    for image in choose:
        image_ab_path.append(root + '/' + image)
    print(image_ab_path)
    plt.figure()
    plt.ion()
    plt.cla()
    for image in image_ab_path:
        print(image)
        image = cv.imdecode(np.fromfile(image, dtype=np.uint8), -1)
        print(image)
        plt.imshow(image)
        plt.pause(time)
    plt.ioff()
