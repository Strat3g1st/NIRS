import cv2
from config import *
from image_gen import get_list_images


# отсекает в выводе HII финальное решение (четвертое изображение из склеенных)
def extract_final_images_from_HII(path):
    images = get_list_images(path)
    for name in images:
        img = cv2.imread(path + name)
        h1, h2 = img.shape[0], img.shape[1]
        img = img[:, h2 - int(h2 * 0.25):h2, :]
        cv2.imwrite(path + name, img)


if __name__ == '__main__':
    path_hii_frame = abs_path_result + dataset + 'HII\\' + path_recovery_frame + '0.1_\\'
    path_hii_grid = abs_path_result + dataset + 'HII\\' + path_recovery_grid + '0.1_\\'
    path_hii_noise = abs_path_result + dataset + 'HII\\' + path_recovery_noise + '0.5_\\'
    path_hii_half = abs_path_result + dataset + 'HII\\' + path_recovery_half + '0.5_\\'
    path_hii_rectangle1 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.1_\\'
    path_hii_rectangle2 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.2_\\'
    path_hii_rectangle5 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.5_\\'

    extract_final_images_from_HII(path_hii_frame)
    print('frame formated')
    extract_final_images_from_HII(path_hii_grid)
    print('grid formated')
    extract_final_images_from_HII(path_hii_noise)
    print('noise formated')
    extract_final_images_from_HII(path_hii_half)
    print('half formated')
    extract_final_images_from_HII(path_hii_rectangle1)
    print('rectangle 0.1 formated')
    extract_final_images_from_HII(path_hii_rectangle2)
    print('rectangle 0.2 formated')
    extract_final_images_from_HII(path_hii_rectangle5)
    print('rectangle 0.5 formated')
