import csv
if __name__=='__main__':
    csv_path='./intermediate_file/detect_result/csv/'
    csv_fn=csv_path+'padding_detect_result.csv'
    new_fn=csv_path+'unpadding_detect_result.csv'
    writer_file=open(new_fn, "w")
    writer=csv.writer(writer_file,lineterminator='\n')
    with open(csv_fn,'r') as f:
        reader=csv.reader(f)
        #if have head
        dict_key=next(reader)
        writer.writerow(dict_key)
        for row in reader:
            #print(row)
            img_fn=row[0]
            x1=int(row[1])
            y1=int(row[2])
            x2=int(row[3])
            y2=int(row[4])
            x3=int(row[5])
            y3=int(row[6])
            x4=int(row[7])
            y4=int(row[8])
            dir,num,ori_img_fn=img_fn.split('_',2)

            # label=row[9]

            int_num=int(num)
            if(dir=='h'):
                #image_h>image_w
                x1-=int_num
                x2-=int_num
                x3-=int_num
                x4-=int_num
            if(dir=='w'):
                #iamge_w>image_h
                y1-=int_num
                y2-=int_num
                y3-=int_num
                y4-=int_num
            # row_list=[ori_img_fn,x1,y1,x2,y2,x3,y3,x4,y4,label]
            row_list=[ori_img_fn,x1,y1,x2,y2,x3,y3,x4,y4]

            writer.writerow(row_list)
    writer_file.close()
    print('finish!')