masked_color = 0
non_masked_color = 255

dataset = "places2\\"

methods_inpaint = ["CRA", "DFN", "HII"]

abs_path = "C:\\Users\\maste\\Documents\\materials\\"   # Указать здесь папку, где будет находится БД изображений

abs_path_masks = abs_path + "masks\\"
abs_path_images = abs_path + "images\\"
abs_path_fragmented = abs_path + "fragmented\\"
abs_path_result = abs_path + "results\\"

path_mask_frame = "mask_frame\\"
path_mask_noise = "mask_noise\\"
path_mask_rectangle = "mask_rectangle\\"
path_mask_grid = "mask_grid\\"
path_mask_half = "mask_half\\"

path_image_frame = "image_frame\\"
path_image_noise = "image_noise\\"
path_image_rectangle = "image_rectangle\\"
path_image_grid = "image_grid\\"
path_image_half = "image_half\\"

path_recovery_frame = "recovery_frame\\"
path_recovery_noise = "recovery_noise\\"
path_recovery_rectangle = "recovery_rectangle\\"
path_recovery_grid = "recovery_grid\\"
path_recovery_half = "recovery_half\\"

params_small = [0.05, 0.1, 0.2]
params = [0.1, 0.2, 0.3, 0.4, 0.5]
params_img = [str(x) + "_" for x in params]
params_small_img = [str(x) + "_" for x in params_small]
