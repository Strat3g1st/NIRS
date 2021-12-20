import os
from config import *
from image_gen import get_list_images


def rename_images_to_format():
    path = abs_path_images + dataset
    list_images = get_list_images(path)
    for i in range(0, len(list_images)):
        os.rename(path + list_images[i], path + str(i + 1) + '.jpg')
        print(str(i + 1) + ' renamed')


if __name__ == '__main__':
    rename_images_to_format()
