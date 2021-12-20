from mask_func import *
import os
from os import path


def get_list_images(path):
    lst = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            lst.append(filename)
    return lst


def apply_mask(img, mask):
    new_img = img.copy()
    new_img[mask == masked_color] = 255
    return new_img


def img_open(path):
    img = Image.open(path)
    img = img.convert('RGB')
    img = np.asarray(img)
    return img


def img_save(img, path):
    result = Image.fromarray(img.astype(np.uint8))
    result.save(path)


def apply_mask_to_list_images(func_mask, dir_read, dir_save_image, dir_save_mask, params, params_name):
    lst = get_list_images(dir_read)
    for img_name in lst:
        print('\n' + img_name + ' func: ' + func_mask.__name__)
        img = img_open(dir_read + img_name)

        for i in range(len(params)):
            print(params[i], end=' ')
            mask = func_mask(img.shape, params[i])
            dir = dir_save_mask + params_name[i] + "\\"
            if not path.exists(dir):
                os.mkdir(dir)
            img_save(mask, dir + img_name)

            result = apply_mask(img, mask)
            dir = dir_save_image + params_name[i] + "\\"
            if not path.exists(dir):
                os.mkdir(dir)
            img_save(result, dir + img_name)


def image_gen_main():
    path_masks = [path_mask_half, path_mask_rectangle, path_mask_noise]
    path_masks_small_param = [path_mask_frame, path_mask_grid]

    path_images = [path_image_half, path_image_rectangle, path_image_noise]
    path_images_small_param = [path_image_frame, path_image_grid]

    func_masks = [mask_half, mask_rectangle, mask_noise]
    func_masks_small_param = [mask_frame, mask_grid]

    dir_read = abs_path_images + dataset
    dir_save_mask = abs_path_masks + dataset
    dir_save_image = abs_path_fragmented + dataset

    for i in range(len(func_masks)):
        apply_mask_to_list_images(func_masks[i], dir_read,
                                  dir_save_image + path_images[i],
                                  dir_save_mask + path_masks[i],
                                  params, params_img)

    for i in range(len(func_masks_small_param)):
        apply_mask_to_list_images(func_masks_small_param[i], dir_read,
                                  dir_save_image + path_images_small_param[i],
                                  dir_save_mask + path_masks_small_param[i],
                                  params_small, params_small_img)


if __name__ == '__main__':
    image_gen_main()
