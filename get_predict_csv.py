import cv2
import os
import numpy as np
import csv
if __name__=='__main__':
    csv_path='./intermediate_file'
    #detection result
    ori_label_csv_fn='/detect_result/csv/unpadding_detect_result.csv'
    #recognize result
    single_csv_fn='/recognize_result/result.csv'
    #build dict
    single_dict={}
    with open(csv_path+single_csv_fn,'r') as f:
        reader_single=csv.reader(f)
        dict_key=next(reader_single)
        for row in reader_single:
            # print row
            key,_=row[0].split('.')
            single_dict[key]=row[1]
    #print(len(list(single_dict.values())))
    keys_list=list(single_dict.keys())
    # keys_list=sorted(keys_list)
    # print 'keys_list',keys_list
    img_fn_set=set()
    i=1
    # for k in keys_list:
    #    print k
    best_csv_fn='/final_result/predict.csv'
    writer_file=open(csv_path+best_csv_fn, "w")
    writer=csv.writer(writer_file,lineterminator='\n')

    with open(csv_path+ori_label_csv_fn,'r') as f_ori:
        reader_ori=csv.reader(f_ori)
        #if detection have file head
        dict_key_ori=next(reader_ori)
        dict_key_ori.append('text')
        writer.writerow(dict_key_ori)
        # 
        for row in reader_ori:

            img_fn=row[0]
            # print 'img_fn',img_fn
            x1=int(row[1])
            y1=int(row[2])
            x2=int(row[3])
            y2=int(row[4])
            x3=int(row[5])
            y3=int(row[6])
            x4=int(row[7])
            y4=int(row[8])
            # if no label
            # label=row[9]
            label=''
            if not img_fn in img_fn_set:
                # print 'here'
                i=1
                img_fn_set.add(img_fn)
            else:
                i+=1
            key_cur=img_fn.split('.')[0]+'_{}'.format(i)
            # print key_cur,type(key_cur)
            if key_cur in keys_list:
                # print 'here'
                label=single_dict[key_cur]
                # print 'label',label
            row_list=[img_fn,x1,y1,x2,y2,x3,y3,x4,y4,label]
            writer.writerow(row_list)
    writer_file.close()
    print 'finish!'