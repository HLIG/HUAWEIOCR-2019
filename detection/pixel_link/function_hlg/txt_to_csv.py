#encoding=utf-8
import os
import csv
import io
path_lists=[]

def read_lines(txt_name=""):
    """return the text in a file in lines as a list """
    txt_name="/media/scut214/file/HLG/Chinese_Recognition/test_result3/txt/"+txt_name
    f = open(txt_name,'rU')
    return f.readlines()

g = os.walk(r"/media/scut214/file/HLG/Chinese_Recognition/test_result3/txt/")

for path,dir_list,file_list in g:
    for file_name in file_list:
        if(os.path.join(path, file_name).endswith('.txt')):
            #print(os.path.join(path, file_name))
            # path_list.append(os.path.join(path, file_name))
            # file_name = file_name[0:len(file_name)-4]
            path_lists.append(file_name)

csvFile = io.open('/media/scut214/file/HLG/Chinese_Recognition/test_result3/detection_test.csv',"wb")
# writer = csv.writer(csvFile,lineterminator='\n')
writer = csv.writer(csvFile)
writer.writerow(['FileName', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4'])
for path_list in path_lists:
    lines=read_lines(path_list)
    for line in lines:
        csv_row=[]
        x_and_y=line.strip('\n').split(',')
        # print path_list[0:len(path_list)-4]
        csv_row.append(path_list[0:len(path_list)-4])
        # csv_row.append(path_list)
        csv_row=csv_row+x_and_y
        writer.writerow(csv_row)


# print path_lists

csvFile.close()

