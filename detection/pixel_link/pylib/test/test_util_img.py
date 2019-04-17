import numpy as np

import util.img
import util.plt
import util.dec
def test_ds_size():
    image_size = (15, 15)
    kernel_size = (2, 2)
    stride = (1, 1)
    np.testing.assert_equal(util.img.ds_size(image_size, kernel_size, stride), (14, 14))
    
    kernel_size = (2, 2)
    stride = (3, 3)
    np.testing.assert_equal(util.img.ds_size(image_size, kernel_size, stride), (5, 5))
    
    kernel_size = (3, 3)
    stride = (2, 2)
    np.testing.assert_equal(util.img.ds_size(image_size, kernel_size, stride), (7, 7))
    
    kernel_size = (3, 2)
    stride = (3, 2)
    np.testing.assert_equal(util.img.ds_size(image_size, kernel_size, stride), (5, 7))
    
    
@util.dec.print_test
def test_blur():
    image_path = '~/dataset/ICDAR2015/Challenge4/ch4_training_images/img_150.jpg'
    image = util.img.imread(image_path)
    blurred_3 = util.img.average_blur(image, (3, 3))
    blurred_5 = util.img.average_blur(image, (5, 5))
    util.plt.show_images(images = [image, blurred_3, blurred_5], titles = ['origin', '3x3', '5x5'], bgr2rgb = True, share_axis = True)
    
@util.dec.print_test
def test_rect_perimeter():
    p = util.img.rect_perimeter((5, 5), (80, 80))
    np.testing.assert_equal(p, 300)
    
    p = util.img.rect_perimeter((0, 0), (80, 80))
    np.testing.assert_equal(p, 320)

@util.dec.print_test
def test_rect_perimeter():
    lu, rb = (5, 5), (80, 80)
    p = util.img.rect_area(lu, rb)
    mask =  util.img.black((100, 100))
    util.img.rectangle(mask, lu, rb, border_width = -1, color = 1)
    util.test.assert_equal(p, np.sum(mask))
    
@util.dec.print_test
def _test_resize():
    size = np.array((100, 100))
    img = util.img.black(size)
    util.img.rectangle(img, (10, 10), (90, 90), color = 1, border_width = -1)
    util.img.rectangle(img, (20, 20), (80, 80), color = 2, border_width = -1)
    util.img.rectangle(img, (30, 30), (70, 70), color = 3, border_width = -1)
    util.img.rectangle(img, (40, 40), (60, 60), color = 4, border_width = -1)

    img1 = util.img.resize(img, f = 0.5)
    util.test.assert_equal(util.img.get_shape(img1), 0.5 * size)

    img2 = util.img.resize(img, fx = 0.1, fy = 1)
    print util.img.get_wh(img2), (0.1 * size[0], size[1])
    util.test.assert_equal(util.img.get_wh(img2), (0.1 * size[0], size[1]))

    img3 = util.img.resize(img, size = (300, 400))
    util.test.assert_equal(util.img.get_wh(img3), (300, 400))
#    util.plt.show_images([img, img1, img2, img3])

@util.dec.print_test
def _test_translate():
    img = util.img.white((100, 100))
    dst1 = util.img.translate(img, delta_x = 10, delta_y = 20)
    dst2 = util.img.translate(img, delta_x = 0, delta_y = -20)
    util.plt.show_images([img, dst1, dst2], gray = True)
    
@util.dec.print_test
def _test_get_cnt_rect_bbox():
    img = util.img.black((100, 100))
    util.img.circle(img, center = (50, 50), r = 20, color = 255, border_width = -1)
    util.img.imshow('image', img)

    cnt = util.mask.find_contour(img)[0]
    x,y, w, h = util.img.get_contour_rect_box(cnt)
    util.img.rectangle(img, left_up = (x, y), right_bottom =  (x + w, y + h), color = 200, border_width = 1)
    util.img.imshow('image', img)

@util.dec.print_test
def _test_get_cnt_region_in_rect():
    img = util.img.black((100, 100))
    util.img.rectangle(img, left_up = (50, 50), right_bottom = (90, 80), color = 255, border_width = -1)
    util.img.imshow('Image', img)
    img = util.img.rotate_about_center(img, angle = 30)
    util.img.imshow('Image', img)
    cnt = util.mask.find_contour(img)[0]
    min_area_region = util.img.get_contour_region_in_min_area_rect(img, cnt)
    util.img.imshow('Region', min_area_region)
    
    min_area_region = util.img.get_contour_region_in_rect(img, cnt)
    util.img.imshow('Region', min_area_region)

@util.dec.print_test
def _test_get_contour_region_iou():
    img = util.img.black((100, 100))
    rect1 = util.img.get_rect_points((10, 30), (60, 80))
    rect2 = util.img.get_rect_points((35, 5), (85, 55))
    #util.img.rectangle(img, rect1[0], rect1[-2], 1, -1)
    cnt1 = util.img.points_to_contour(rect1)
    cnt2 = util.img.points_to_contour(rect2)
    util.test.assert_almost_equal(util.img.get_contour_region_iou(img, cnt1, cnt2), 1. / 7, 1)


@util.dec.print_test
def _test_rect_iou():
    img = util.img.black((100, 100))
    rect1 = util.img.get_rect_points((10, 30), (60, 80))
    rect2 = util.img.get_rect_points((35, 5), (85, 55))
    cnt1 = util.img.points_to_contour(rect1)
    cnt2 = util.img.points_to_contour(rect2)
    # util.test.assert_almost_equal(util.img.get_contour_region_iou(img, cnt1, cnt2), 1. / 7, 1)
    iou = util.img.get_contour_region_iou(img, cnt1, cnt2)
    rects1 = [[10, 30, 60, 80], [35, 5, 85, 55], [90, 90, 95, 95]]
    rects2 = [[10, 30, 60, 80], [35, 5, 85, 55]]
    iou_matrix = util.img.get_rect_iou(rects1, rects2)
    print iou_matrix
    
    
@util.dec.print_test
def _test_contour_convex():
        
    mask = util.img.black((100, 100))
    util.img.rectangle(img = mask, left_up = (30, 30), right_bottom = (99, 99), color = 1, border_width = -1)
    util.img.rectangle(img = mask, left_up = (50, 50), right_bottom = (60, 60), color = 0, border_width = -1)
    util.img.rectangle(img = mask, left_up = (40, 20), right_bottom = (50, 40), color = 0, border_width = -1)

    # util.plt.show_images(images=[mask], titles=['Mask', 'Hole Mask'])

    contours = util.img.find_contours(mask)
    vis = util.img.black((100, 100))
    util.img.draw_contours(vis, contours, idx = 0, color = 1, border_width = 1)

    hull = util.img.convex_hull(contours[0])
    util.img.draw_contours(mask, [hull], idx = -1, color = 1, border_width = 1)
    util.plt.show_images(images = [mask, vis])

if util.mod.is_main(__name__):
    util.init_logger()
    #test_rect_perimeter()
    #test_ds_size()
    #test_blur()
    #test_rect_perimeter()
    #_test_resize()
    #_test_translate()
    #_test_get_cnt_rect_bbox()
    #_test_get_cnt_region_in_rect()
    #_test_get_contour_region_iou()
    #_test_rect_iou()
    _test_contour_convex()
