#encoding=utf-8
import os
import csv
import io
path_lists=[]

def read_lines(txt_name=""):
    """return the text in a file in lines as a list """
    txt_name="./intermediate_file/detect_result/txt/"+txt_name
    f = open(txt_name,'rU')
    return f.readlines()

g = os.walk(r"./intermediate_file/detect_result/txt/")

for path,dir_list,file_list in g:
    for file_name in file_list:
        if(os.path.join(path, file_name).endswith('.txt')):
            #print(os.path.join(path, file_name))
            # path_list.append(os.path.join(path, file_name))
            # file_name = file_name[0:len(file_name)-4]
            path_lists.append(file_name)

csvFile = io.open('./intermediate_file/detect_result/csv/padding_detect_result.csv',"wb")
writer = csv.writer(csvFile,lineterminator='\n')
writer = csv.writer(csvFile)
writer.writerow(['filename', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4'])
for path_list in path_lists:
    lines=read_lines(path_list)
    for line in lines:
        csv_row=[]
        x_and_y=line.strip('\n').split(',')
        x=[int(i) for index,i in enumerate(x_and_y) if index%2==0]
        y=[int(i) for index, i in enumerate(x_and_y) if index % 2 == 1]
        coord_list=list(zip(x,y))
        # print 'x',x
        # print 'y',y
        sort_by_x = sorted(coord_list)
        sort_by_y=sorted(coord_list, key=lambda x: x[1])
        # print 'sort_by_x',sort_by_x
        # print 'sort_by_y',sort_by_y

        
        left_up_xy=list(list(sorted(sort_by_y[0:2]))[0])
        # print 'left_up_xy',left_up_xy
        right_up_xy=list(list(sorted(sort_by_y[0:2]))[1])
        # print 'right_up_xy',right_up_xy
        right_bottom_xy=list((list(sorted(sort_by_y[2:4]))[1]))
        # print 'right_bottom_xy',right_bottom_xy
        left_botton_xy=list((list(sorted(sort_by_y[2:4]))[0]))
        # print 'left_botton_xy',left_botton_xy,'\n'
        final_xy=left_up_xy+right_up_xy+right_bottom_xy+left_botton_xy
        # print path_list[0:len(path_list)-4]
        csv_row.append(path_list[0:len(path_list)-4])
        # csv_row.append(path_list)
        csv_row=csv_row+final_xy
        writer.writerow(csv_row)


# print path_lists

csvFile.close()

