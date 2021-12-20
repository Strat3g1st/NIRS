import numpy as np
from PIL import Image
import random
from config import *


fill = [masked_color, masked_color, masked_color]
background = [non_masked_color, non_masked_color, non_masked_color]


def mask_frame(shape, param):
    h1, h2 = shape[0], shape[1]
    mask = np.zeros(shape)
    mask.fill(non_masked_color)
    h1_value = int(h1 * param)
    h2_value = int(h2 * param)
    mask[0:h1_value, :, :] = fill
    mask[h1 - h1_value:h1, :, :] = fill
    mask[:, 0:h2_value, :] = fill
    mask[:, h2 - h2_value: h2, :] = fill
    return mask


def mask_rectangle(shape, param):
    h1, h2 = shape[0], shape[1]
    mask = np.zeros(shape)
    mask.fill(non_masked_color)
    h1_value = int(h1 * param)
    h2_value = int(h2 * param)
    coord1 = random.randint(0, h1 - h1_value)
    coord2 = random.randint(0, h2 - h2_value)
    mask[coord1:coord1 + h1_value, coord2:coord2 + h2_value, :] = fill
    return mask


def mask_half(shape, param):
    h1, h2 = shape[0], shape[1]
    mask = np.zeros(shape)
    mask.fill(non_masked_color)
    mask[:, h2 - int(h2 * param):h2, :] = fill
    return mask


def mask_grid(shape, param): #, regime=2):
    h1, h2 = shape[0], shape[1]
    h1_value = int(h1 * param)
    # h2_value = int(h2 * value)
    mask = np.zeros(shape)
    mask.fill(non_masked_color)
    # if regime == 1:
    h_value = int(h1 * param)
    start = 0
    end = h_value
    while end <= h1:
        mask[start:end, :, :] = fill
        start += int(2 * h1_value)
        end += int(2 * h1_value)
    # else:
    #     h_value = int(h2 * value)
    #     start = 0
    #     end = h_value
    #     while end <= h2:
    #         mask[:, start:end, :] = fill
    #         start += int(2 * h2_value)
    #         end += int(2 * h2_value)
    return mask


def mask_noise(shape, param):
    mask = np.zeros(shape)
    mask.fill(non_masked_color)
    noise = np.random.choice((0, 1, 2), size=(shape[0], shape[1]), p=[param, (1 - param) / 2., (1 - param) / 2.])
    mask[noise == 1] = fill
    return mask


if __name__ == '__main__':
    C = Image.open(abs_path_images + dataset + '1.jpg')
    C = C.convert('RGB')
    C = np.asarray(C)
    mask = mask_half(C.shape, 0.3)
    mask = Image.fromarray(mask.astype(np.uint8))
    mask.show()

