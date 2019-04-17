# -*- coding: utf-8 -*-
"""
usage: change your own data dir and it works
"""
import numpy as np
import os
from collections import namedtuple
from PIL import Image
import cv2
import matplotlib.pylab as plt
import codecs


Img_dataset_dir = './intermediate_file/padding_images_to_detection/'
Label_dataset_dir = './intermediate_file/detect_result/txt/'
crop_dataset_dir_vert = './intermediate_file/images_to_recognition/'


Label_list = os.listdir(Label_dataset_dir)
for i in range(len(Label_list)):
    count=1
    image_name=Label_list[i].split('.txt')[0]
    name=Label_list[i].split('_')[4]
    with open(os.path.join(Label_dataset_dir,Label_list[i]))  as f:
        for line in f.readlines():
            img=cv2.imdecode(np.fromfile(Img_dataset_dir+image_name,dtype=np.uint8),-1)
            # img = cv2.imread(Img_dataset_dir+image_name)
            coordinates = line.split(',')[0:8]
            coord = namedtuple('coord', ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4'])
            coordinate= coord(coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4],coordinates[5],coordinates[6],coordinates[7])
            X = list(map(float, [coordinate.x1, coordinate.x2, coordinate.x3, coordinate.x4]))
            Y = list(map(float, [coordinate.y1, coordinate.y2, coordinate.y3, coordinate.y4]))
            Xmin = min(X)
            Xmax = max(X)
            Ymin = min(Y)
            Ymax = max(Y)
            img_new = img[int(Ymin):int(Ymax), int(Xmin):int(Xmax)]
            img_new = cv2.flip(img_new, 1)
            img_new = cv2.transpose(img_new)
            img_new = Image.fromarray(img_new)
            names = str('img_calligraphy_'+str(name) + '_bg_'+str(count)+'.jpg')
            count+=1
            p = img_new.size[1] / 64
            if p == 0:
                continue
            new_height = 64
            new_width = int(img_new.size[0] / p)
            if new_width>1300:
                new_width=1300
            new_1=img_new.resize((new_width, new_height))
            try:
                new_1.save(os.path.join(crop_dataset_dir_vert, names))
                # f = codecs.open(os.path.join(crop_dataset_dir_vert, 'lable.txt'), 'a', encoding='utf-8')
                # f.write(str(crop_dataset_dir_vert + names + ',' + line))
            except:
                continue
            # f.close()