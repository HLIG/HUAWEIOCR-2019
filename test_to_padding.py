import cv2
import os
import numpy as np

#coding=utf-8
def get_file_name(path):
    file_list=[]
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            #full_file=os.path.join(root,file)
            file_list.append(file)
    return file_list

if __name__=='__main__':
    ori_path='./test_images'
    pad_path='./intermediate_file/padding_images_to_detection'
    if not os.path.isdir(pad_path):
        os.mkdir(pad_path)
    files=get_file_name(ori_path)
    count=0
    for file in files:
        image=cv2.imdecode(np.fromfile(os.path.join(ori_path,file),dtype=np.uint8),-1)
        #print(file,'shape is ',image.shape)
        h,w,_=image.shape
        new_fn=file
        if h>w:
            #higher
            diff=(h-w)//2
            biger_image=cv2.copyMakeBorder(image,0, 0, diff, diff, cv2.BORDER_REPLICATE)
            new_fn='h_'+str(diff)+'_'+new_fn
        else:
            #wider
            diff=(w-h)//2
            biger_image=cv2.copyMakeBorder(image,diff, diff, 0, 0, cv2.BORDER_REPLICATE)
            new_fn='w_'+str(diff)+'_'+file
        new_fn=os.path.join(pad_path,new_fn)
        #print(new_fn,'shape is',biger_image.shape)

        cv2.imencode('.jpg', biger_image)[1].tofile(new_fn)
        #count+=1
        #if count>10:
        #    break
    print('save')