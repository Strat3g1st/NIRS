import matplotlib.pyplot as plt
import pickle


def load_metric(output_filename):
    with open(output_filename, 'rb') as f:
        ssim1_values = pickle.load(f)
        psnr1_values = pickle.load(f)
        ssim2_values = pickle.load(f)
        psnr2_values = pickle.load(f)
        ssim3_values = pickle.load(f)
        psnr3_values = pickle.load(f)
    return ssim1_values, psnr1_values, ssim2_values, psnr2_values, ssim3_values, psnr3_values


def plot_result(resuls1, resuls2, resuls3, text):
    N = len(resuls1)
    N = int(N / 10)
    plt.title(text)
    plt.plot(list(range(1, N + 1)), resuls1[:N], label='CRA')
    plt.plot(list(range(1, N + 1)), resuls2[:N], label='DFN')
    plt.plot(list(range(1, N + 1)), resuls3[:N], label='HII')
    plt.legend()
    plt.show()


def gen_graphic(output_filename, maskname):
    ssim1_values, psnr1_values, ssim2_values, psnr2_values, ssim3_values, psnr3_values = load_metric(output_filename)
    plot_result(ssim1_values, ssim2_values, ssim3_values, 'SSIM для случая восстановления вырезов типа ' + maskname)
    plot_result(psnr1_values, psnr2_values, psnr3_values, 'PSNR для случая восстановления вырезов типа ' + maskname)


if __name__ == '__main__':
    output_filename_frame = 'frame.pickle'
    output_filename_grid = 'grid.pickle'
    output_filename_noise = 'noise.pickle'
    output_filename_half = 'half.pickle'
    output_filename_rectangle1 = 'rectangle1.pickle'
    output_filename_rectangle2 = 'rectangle2.pickle'
    output_filename_rectangle5 = 'rectangle5.pickle'

    gen_graphic(output_filename_frame, 'frame')
    gen_graphic(output_filename_grid, 'grid')
    gen_graphic(output_filename_noise, 'noise')
    gen_graphic(output_filename_half, 'half')
    gen_graphic(output_filename_rectangle1, 'rectangle1')
    gen_graphic(output_filename_rectangle2, 'rectangle2')
    gen_graphic(output_filename_rectangle5, 'rectangle5')
