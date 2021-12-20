from config import *
from image_gen import image_gen_main, get_list_images
from initial_data_dirs import initial_dirs
from format_name import rename_images_to_format
from shutil import copyfile


def copy_files(source_dir, destination_dir):
    sources = get_list_images(source_dir)
    for i in range(len(sources)):
        print("Copying " + str(i) + " image...")
        copyfile(source_dir + sources[i], destination_dir + sources[i])


if __name__ == '__main__':
    source_dir = "C:\\Users\\maste\\Documents\\images\\"     # Указать здесь исходную папку с изображениями в любом месте
    initial_dirs()
    copy_files(source_dir, abs_path_images + dataset)
    rename_images_to_format()
    image_gen_main()
