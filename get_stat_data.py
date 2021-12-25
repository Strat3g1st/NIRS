import cv2
from skimage.metrics import structural_similarity as compare_ssim
from config import *
from image_gen import get_list_images
import pickle
# from skimage import io


def ssim(path1, path2):
    img1 = cv2.cvtColor(cv2.imread(path1), cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(cv2.imread(path2), cv2.COLOR_BGR2GRAY)
    return compare_ssim(img1, img2, full=False)


def psnr(path1, path2):
    img1 = cv2.cvtColor(cv2.imread(path1), cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(cv2.imread(path2), cv2.COLOR_RGB2BGR)
    return cv2.PSNR(img1, img2)


def calc_metric(path1, path2):
    ssim_values = []
    psnr_values = []
    images = get_list_images(path1)
    images_masked = get_list_images(path2)
    for i in range(len(images)):
        ssim_values.append(ssim(path1 + images[i], path2 + images_masked[i]))
        psnr_values.append(psnr(path1 + images[i], path2 + images_masked[i]))
    return ssim_values, psnr_values


def dump_metric(output_filename, path_etalon, path_three_method):
    with open(output_filename, 'wb') as f:
        for path in path_three_method:
            print(path)
            ssim_values, psnr_values = calc_metric(path_etalon, path)
            pickle.dump(ssim_values, f)
            pickle.dump(psnr_values, f)


if __name__ == '__main__':
    path_etalon = abs_path_images + dataset

    path_cra_frame = abs_path_result + dataset + 'CRA\\' + path_recovery_frame + '0.1_\\'
    path_cra_grid = abs_path_result + dataset + 'CRA\\' + path_recovery_grid + '0.1_\\'
    path_cra_noise = abs_path_result + dataset + 'CRA\\' + path_recovery_noise + '0.5_\\'
    path_cra_half = abs_path_result + dataset + 'CRA\\' + path_recovery_half + '0.5_\\'
    path_cra_rectangle1 = abs_path_result + dataset + 'CRA\\' + path_recovery_rectangle + '0.1_\\'
    path_cra_rectangle2 = abs_path_result + dataset + 'CRA\\' + path_recovery_rectangle + '0.2_\\'
    path_cra_rectangle5 = abs_path_result + dataset + 'CRA\\' + path_recovery_rectangle + '0.5_\\'

    path_dfn_frame = abs_path_result + dataset + 'DFN\\' + path_recovery_frame + '0.1_\\' + 'result\\'
    path_dfn_grid = abs_path_result + dataset + 'DFN\\' + path_recovery_grid + '0.1_\\' + 'result\\'
    path_dfn_noise = abs_path_result + dataset + 'DFN\\' + path_recovery_noise + '0.5_\\' + 'result\\'
    path_dfn_half = abs_path_result + dataset + 'DFN\\' + path_recovery_half + '0.5_\\' + 'result\\'
    path_dfn_rectangle1 = abs_path_result + dataset + 'DFN\\' + path_recovery_rectangle + '0.1_\\' + 'result\\'
    path_dfn_rectangle2 = abs_path_result + dataset + 'DFN\\' + path_recovery_rectangle + '0.2_\\' + 'result\\'
    path_dfn_rectangle5 = abs_path_result + dataset + 'DFN\\' + path_recovery_rectangle + '0.5_\\' + 'result\\'

    path_hii_frame = abs_path_result + dataset + 'HII\\' + path_recovery_frame + '0.1_\\'
    path_hii_grid = abs_path_result + dataset + 'HII\\' + path_recovery_grid + '0.1_\\'
    path_hii_noise = abs_path_result + dataset + 'HII\\' + path_recovery_noise + '0.5_\\'
    path_hii_half = abs_path_result + dataset + 'HII\\' + path_recovery_half + '0.5_\\'
    path_hii_rectangle1 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.1_\\'
    path_hii_rectangle2 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.2_\\'
    path_hii_rectangle5 = abs_path_result + dataset + 'HII\\' + path_recovery_rectangle + '0.5_\\'

    output_filename_frame = 'frame.pickle'
    output_filename_grid = 'grid.pickle'
    output_filename_noise = 'noise.pickle'
    output_filename_half = 'half.pickle'
    output_filename_rectangle1 = 'rectangle1.pickle'
    output_filename_rectangle2 = 'rectangle2.pickle'
    output_filename_rectangle5 = 'rectangle5.pickle'

    dump_metric(output_filename_frame, path_etalon, [path_cra_frame, path_dfn_frame, path_hii_frame])
    print('frame dumped')
    dump_metric(output_filename_grid, path_etalon, [path_cra_grid, path_dfn_grid, path_hii_grid])
    print('grid dumped')
    dump_metric(output_filename_noise, path_etalon, [path_cra_noise, path_dfn_noise, path_hii_noise])
    print('noise dumped')
    dump_metric(output_filename_half, path_etalon, [path_cra_half, path_dfn_half, path_hii_half])
    print('half dumped')
    dump_metric(output_filename_rectangle1, path_etalon, [path_cra_rectangle1, path_dfn_rectangle1, path_hii_rectangle1])
    print('rectangle 0.1 dumped')
    dump_metric(output_filename_rectangle2, path_etalon, [path_cra_rectangle2, path_dfn_rectangle2, path_hii_rectangle2])
    print('rectangle 0.2 dumped')
    dump_metric(output_filename_rectangle5, path_etalon, [path_cra_rectangle5, path_dfn_rectangle5, path_hii_rectangle5])
    print('rectangle 0.5 dumped')
