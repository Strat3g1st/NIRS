path_img = "C:\\Users\\maste\\Documents\\materials\\images\\places2\\"
path_mask_frame = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_frame\\0.1_\\"
path_mask_grid = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_grid\\0.1_\\"
path_mask_noise = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_noise\\0.5_\\"
path_mask_half = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_half\\0.5_\\"
path_mask_rectangle1 = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_rectangle\\0.1_\\"
path_mask_rectangle2 = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_rectangle\\0.2_\\"
path_mask_rectangle5 = "C:\\Users\\maste\\Documents\\materials\\masks\\places2\\mask_rectangle\\0.5_\\"


def gen(path_mask, filename):
    f = open('samples/' + filename + '.txt', 'w')
    for i in range(1, 1001):
        s = path_img + str(i) + '.jpg ' + path_mask + str(i) + '.jpg\n'
        f.write(s)


gen(path_mask_frame, 'conf_frame')
gen(path_mask_grid, 'conf_grid')
gen(path_mask_noise, 'conf_noise')
gen(path_mask_half, 'conf_half')
gen(path_mask_rectangle1, 'conf_rectangle1')
gen(path_mask_rectangle2, 'conf_rectangle2')
gen(path_mask_rectangle5, 'conf_rectangle5')
