import log
import dtype
import plt
import np
import img
_img = img
import dec
import rand
import mod
import proc
import test
import neighbour as nb
#import mask
import str_ as str
import io as sys_io
import io_ as io
import feature
import thread_ as thread
import caffe_ as caffe
import tf
import cmd
import ml
import sys
import url
import time_ as time
from progress_bar import ProgressBar
import cv2
import os
# log.init_logger('~/temp/log/log_' + get_date_str() + '.log')

def exit(code = 0):
    sys.exit(0)
    
is_main = mod.is_main
init_logger = log.init_logger

def get_temp_path(name = ''):
    _count = get_count();
    path = './sample_result/%s_%d_%s.png'%(log.get_date_str(), _count, name)
    return path
def sit(img = None, format = 'rgb', path = None, name = "",image_name="",bboxes=[]):
    if path is None:
        path = get_temp_path(name)
        
    if img is None:
        plt.save_image(path)
        return path
    
        
    if format == 'bgr':
        img = _img.bgr2rgb(img)
    if type(img) == list:
        plt.show_images(images = img, path = path, show = False, axis_off = True, save = True)
    else:
        # print path
        # cv2.imshow("test",img)
        # cv2.waitKey(0)
        # print os.path.abspath(path)
        image_path=path+'images/'+image_name
        # print image_path
        cv2.imwrite(image_path, img)
    
    def write_result_as_txt(image_name, bboxes, path):
        filename = io.join_path(path, '%s.txt'%(image_name))
        print 'path',path
        lines = []
        for b_idx, bbox in enumerate(bboxes):
              values = [int(v) for v in bbox]
              line = "%d, %d, %d, %d, %d, %d, %d, %d\n"%tuple(values)
              lines.append(line)
        io.write_lines(filename, lines)
        # print '1112222222222222'
        print 'result has been written to:', filename
    write_result_as_txt(image_name=image_name,path=path+'txt/',bboxes=bboxes)
    return path
_count = 0;

def get_count():
    global _count;
    _count += 1;
    return _count    

def cit(img, path = None, rgb = True, name = ""):
    _count = get_count();
    if path is None:
        img = np.np.asarray(img, dtype = np.np.uint8)
        path = '~/temp/no-use/images/%s_%s_%d.jpg'%(name, log.get_date_str(), _count)
        _img.imwrite(path, img, rgb = rgb)
    return path        

argv = sys.argv
    
