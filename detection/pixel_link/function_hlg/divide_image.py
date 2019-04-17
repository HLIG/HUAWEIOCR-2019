import os
import shutil
g = os.walk(r"/media/scut214/file/HLG/Chinese_Recognition/single_64_long_3")

path_lists=[]
for path,dir_list,file_list in g:
    for file_name in file_list:
        if(os.path.join(path, file_name).endswith('.jpg')):
            #print(os.path.join(path, file_name))
            path_lists.append(os.path.join(path, file_name))
            # file_name = file_name[0:len(file_name)-4]
            # path_lists.append(file_name)

# total_images_num=10000
# division=2
# image_per_file=total_images_num//division
# print len(path_lists)
# for path_list in path_lists:
#     print path_list

end_in_name='img_calligraphy_89130_bg_2_7.jpg'#
test_filelist1 = sorted(path_lists)

end_in_index=test_filelist1.index('/media/scut214/file/HLG/Chinese_Recognition/single_64_long_3/'+end_in_name)
test_filelist1=test_filelist1[end_in_index:]

part1=test_filelist1[0:len(test_filelist1)//10*5]
part2=test_filelist1[len(test_filelist1)//10*5:len(test_filelist1)//10*8]
part3=test_filelist1[len(test_filelist1)//10*8:]
print(len(part1))
print(len(part2))
print(len(part3))
print(len(test_filelist1))
# for current_file in range(division):
target_dir1="/media/scut214/file/HLG/Chinese_Recognition/single_64_long_3_1/"
target_dir2="/media/scut214/file/HLG/Chinese_Recognition/single_64_long_3_2/"
target_dir3="/media/scut214/file/HLG/Chinese_Recognition/single_64_long_3_3/"
#     os.mkdir(target_dir)
#     for i in range(image_per_file):
#         image_name=path_lists[current_file*image_per_file+i]
#         shutil.copy(image_name, target_dir)


for i in part1:
    # print (i.split('/')[-1])
    # print(target_dir1+i.split('/')[-1])
    # print(i)
    shutil.copy(i, target_dir1+i.split('/')[-1])
for i in part2:
    shutil.copy(i, target_dir2+i.split('/')[-1])
for i in part3:
    shutil.copy(i, target_dir3+i.split('/')[-1])
