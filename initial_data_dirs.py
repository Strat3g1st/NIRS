import os
from config import *


def initial_dirs():
    os.mkdir(abs_path)

    os.mkdir(abs_path_masks)
    os.mkdir(abs_path_images)
    os.mkdir(abs_path_fragmented)
    os.mkdir(abs_path_result)

    os.mkdir(abs_path_masks + dataset)
    os.mkdir(abs_path_images + dataset)
    os.mkdir(abs_path_fragmented + dataset)
    os.mkdir(abs_path_result + dataset)

    path_masks = [path_mask_frame, path_mask_noise, path_mask_rectangle, path_mask_grid, path_mask_half]
    path_fragmented = [path_image_frame, path_image_noise, path_image_rectangle, path_image_grid, path_image_half]
    path_results = [path_recovery_frame, path_recovery_noise, path_recovery_rectangle, path_recovery_grid, path_recovery_half]

    for p in path_masks:
        os.mkdir(abs_path_masks + dataset + p)

    for p in path_fragmented:
        os.mkdir(abs_path_fragmented + dataset + p)

    for i in range(len(methods_inpaint)):
        os.mkdir(abs_path_result + dataset + methods_inpaint[i] + "\\")

    for p in path_results:
        for i in range(len(methods_inpaint)):
            os.mkdir(abs_path_result + dataset + methods_inpaint[i] + "\\" + p)

    for p in [path_recovery_noise, path_recovery_rectangle, path_recovery_half]:
        for i in range(len(methods_inpaint)):
            for v in params_img:
                os.mkdir(abs_path_result + dataset + methods_inpaint[i] + "\\" + p + v)

    for p in [path_recovery_frame, path_recovery_grid]:
        for i in range(len(methods_inpaint)):
            for v in params_small_img:
                os.mkdir(abs_path_result + dataset + methods_inpaint[i] + "\\" + p + v)


if __name__ == '__main__':
    initial_dirs()
