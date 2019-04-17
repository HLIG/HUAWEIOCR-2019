import numpy as np

import matplotlib.pyplot as plt
import util

def test_to_ROI():
    image_path = '~/dataset/ICDAR2015/Challenge4/ch4_training_images/img_150.jpg'
    image = util.img.imread(image_path, rgb = True)
    ax = plt.subplot(111)
    ax.imshow(image)
    ROI = [(53, 113), (377, 275)]
    util.plt.to_ROI(ax, ROI)
    plt.show()


@util.dec.print_test
def test_save_images():
    path = '~/temp/result/test.png'
    shape = (100, 100, 3)
    white = util.img.white(shape)
    black = util.img.black(shape)
    util.plt.show_images(images = [white, black], titles = ['white', 'black'], show = False, save = True, path = path, axis_off = True)
    #util.plt.save_images(path = path)

test_save_images()

#test_to_ROI()
