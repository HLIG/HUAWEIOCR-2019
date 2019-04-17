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

def coord_fix(x,y):
    coord_list=list(zip(x,y))
    sort_by_x = sorted(coord_list)
    sort_by_y=sorted(coord_list, key=lambda x: x[1])
    left_up_xy=list(list(sorted(sort_by_y[0:2]))[0])
    right_up_xy=list(list(sorted(sort_by_y[0:2]))[1])
    right_bottom_xy=list((list(sorted(sort_by_y[2:4]))[1]))
    left_botton_xy=list((list(sorted(sort_by_y[2:4]))[0]))
    final_xy=left_up_xy+right_up_xy+right_bottom_xy+left_botton_xy
    X=[int(i) for index,i in enumerate(final_xy) if index%2==0]
    Y=[int(i) for index, i in enumerate(final_xy) if index % 2 == 1]
    return X,Y

def transform(x1,y1,x2,y2,x3,y3,x4,y4):
    height1 = np.sqrt((x1-x4)**2 + (y4-y1)**2)
    height2 = np.sqrt((x3-x2)**2 + (y3-y2)**2)
    h = max(height1,height2)

    width1 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    width2 = np.sqrt((x3-x4)**2 + (y3-y4)**2)
    w = max(width1,width2)

    Pts = np.float32(np.array([[0,0],[w,0],[w,h],[0,h]]))#顺时针
    return Pts,w,h

Label_list = os.listdir(Label_dataset_dir)
for i in range(len(Label_list)):
    # print i
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
            X,Y=coord_fix(X,Y)

                #放射变换截图
            Pts1 = np.float32(np.array([[X[0], Y[0]], [X[1], Y[1]], [X[2], Y[2]], [X[3], Y[3]]]))
            Pts2, W, H = transform(X[0], Y[0], X[1], Y[1], X[2], Y[2], X[3], Y[3])
            M = cv2.getPerspectiveTransform(Pts1, Pts2)
            #img1 = np.array(img)
            Dst = cv2.warpPerspective(img, M, (int(W), int(H)))
        

            img_new = cv2.flip(Dst, 1)
            img_new = cv2.transpose(img_new)
            img_new = Image.fromarray(img_new)            


            # img_new = img[int(Ymin):int(Ymax), int(Xmin):int(Xmax)]
            # img_new = cv2.flip(img_new, 1)
            # img_new = cv2.transpose(img_new)
            # img_new = Image.fromarray(img_new)
            names = str('img_calligraphy_'+str(name) + '_bg_'+str(count)+'.jpg')
            # print 'names',names
            count+=1
            print 'img_new.size[1]',img_new.size[1]
            p = img_new.size[1] / 64.0
            if p == 0:
                print'here'
                continue
            new_height = 64
            new_width = int(img_new.size[0] / p)
            if new_width>1300:
                new_width=1300
            new_1=img_new.resize((new_width, new_height))
            # try:
            new_1.save(os.path.join(crop_dataset_dir_vert, names))
                # f = codecs.open(os.path.join(crop_dataset_dir_vert, 'lable.txt'), 'a', encoding='utf-8')
                # f.write(str(crop_dataset_dir_vert + names + ',' + line))
            # except:
                # print 'error:',names
                # continue
            # f.close()