文字检测主要使用了浙大的pixellink

<https://github.com/ZJULearning/pixel_link>

在文字识别OCR模型上使用西安交通大学人工智能实践大赛第一名@ yinchangchang 的方案<https://github.com/yinchangchang/ocr_densenet>

针对本比赛的数据集，对代码进行了修改，改进的细节见代码和参考技术报告

<https://discussion.datafountain.cn/questions/1571/answers/22399>



# 安装步骤

## 1、首先代码的文件分为四个部分：

文字检测文件夹：detection

文字识别文件夹：recognition

存放测试图片的文件夹：test_images

最后结果和中间生成文件：intermediate_file

**注意：存放文件夹的路径不能带中文！！！！！！！**

## 2、安装步骤

所有的代码语言均为python2，系统环境为linux64

建议使用anaconda**分别创建**  **识别**和**检测**的环境

解压到文件夹，假设为`unzip_path`

首先，**安装文字检测环境**

打开终端，进入HUAWEI_OCR2019/detection，安装检测的环境并激活，设该终端为**文字检测终端**

```
conda env create --file detection.txt
source activate pixel_link
```



然后，**安装文字识别环境**

**新打开一个终端**，进入HUAWEI_OCR2019/recognition



进入HUAWEI_OCR2019/detection安装检测的环境并激活，设该终端为**文字识别终端**

```
conda create --name ocr_densenet python=2.7
source activate ocr_densenet
pip install recognition.txt
```



从百度云下载文字检测网络权重文件，放到路径HUAWEI_OCR2019\detection\pixel_link\checkpoint下

从百度云下载文字识别网络权重文件，放到路径HUAWEI_OCR2019\recognition\densenet\model下

https://pan.baidu.com/s/1LVbfVa5ieibFg_X6iIuWfw 

提取码：e8rd

至此，文字检测和文字识别的环境都装好了。



## 3、测试及相关命令



在创建了检测文字检测环境pixel_link，和文字识别网络环境ocr_densenet后

首先在**文字检测终端!!!!!!!!**，进入解压后的文件夹
`cd unzip_path/HUAWEI_OCR2019`

0. 把网站上下载的测试图片集中的图片放到`unzip_path/ HUAWEI_OCR2019/test_images`

1. 执行`python test_to_padding.py`
   功能：将测试图片填充，并将结果输出到`unzip_path/ HUAWEI_OCR2019/intermediate_file/padding_images_to_detection`
2. `cd unzip_path/HUAWEI_OCR2019/detection/pixel_link`
   执行脚本`./scripts/test_any.sh 3 checkpoint/model.ckpt-146343 ../../intermediate_file/padding_images_to_detection`，运行检测的`pixel link`网络
   功能：检测网络，将每一张填充后的图片的检测框信息输出到文件夹`unzip_path/HUAWEI_OCR2019/intermediate_file/detect_result/txt`中，将可视化的检测结果图片输出到`unzip_path/HUAWEI_OCR2019/intermediate_file/detect_result/images`中。
3. `cd unzip_path/HUAWEI_OCR2019`返回主目录
   双方案，B榜提交是方案1，但是更优秀的方案是2(方案2用了仿射变换，可以对倾斜的文字进行分割，由于时间仓促没用上)。
   1. （二选一）执行脚本`python crop_and_reshape.py`
      功能：将填充后的测试图片根据检测结果分割为子图片，并输出到`unzip_path/HUAWEI_OCR2019/intermediate_file/images_to_recognition`文件夹下。
   2. （二选一）执行脚本`python target_cut_test_many.py`
      功能：根据检测结果，将填充后的图片进行仿射变换后的分割，同样输出到`unzip_path/HUAWEI_OCR2019/intermediate_file/images_to_recognition`文件夹下。
4. `cd unzip_path/HUAWEI_OCR2019/recognition/densenet/code`
   在**文字识别终端!!!!!!!**切换到识别网络程序所在目录
   执行脚本`python main.py`
   功能：对切割后的图片进行神经网络识别，输出中间结果`result.csv`到`unzip_path/HUAWEI_OCR2019/intermediate_file/recognize_result`
5. 切换回**文字检测终端!!!!!!!!!**
   `cd unzip_path/HUAWEI_OCR2019`返回主目录
   执行`python txt_to_csv.py`
   功能：将检测结果的所有`.txt`文件转换为`padding_detect_result.csv`，并将结果输出到`unzip_path/HUAWEI_OCR2019/intermediate_file/detect_result/csv`文件夹下
6. 执行`python padding2unpadding_box.py`
   功能：将检测结果`padding_detect_result.csv`转换回未填充的结果`unpadding_detect_result.csv`，并将结果输出到`unzip_path/HUAWEI_OCR2019/intermediate_file/detect_result/csv`文件夹下
7. 执行`python get_predict_csv.py`
   功能：将未填充检测结果`unpadding_detect_result.csv`和识别结果`result.csv`文件组合为一个可提交的`predict.csv`文件，输出最终结果到`unzip_path/HUAWEI_OCR2019/intermediate_file/final_result/`文件夹下

在`unzip_path/HUAWEI_OCR2019/intermediate_file/final_result`文件夹下即为最终提交的`predict.csv`结果