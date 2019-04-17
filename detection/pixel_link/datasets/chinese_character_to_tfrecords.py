#encoding=utf-8
import numpy as np
import tensorflow as tf
import util
from dataset.dataset_utils import int64_feature, float_feature, bytes_feature, convert_to_example
import config
import pandas as pd

def cvt_to_tfrecords(output_path , data_path):
    if data_path.find('train_image')>0 :
        image_csv=pd.read_csv(data_path+'train_lable.csv')
        # print image_csv
    elif data_path.find('verify_image') >0:
        image_csv = pd.read_csv(data_path + 'verify_lable.csv')
        # print image_csv
    image_path_csv = image_csv[image_csv.columns[0]]
    image_path_csv = image_path_csv.values.tolist()
    image_csv=image_csv.values.tolist()

    # print image_path_csv
    image_names = util.io.ls(data_path, '.jpg')#[0:10];
    image_names_np=np.array(image_names)
    image_path_csv_np=np.array(image_path_csv)
    image_path_index=[np.where(image_path_csv_np == image_name) for image_name in image_names]
    # print image_path_index[1][0].tolist()
    print "%d images found in %s"%(len(image_names), data_path);
    with tf.python_io.TFRecordWriter(output_path) as tfrecord_writer:
        for idx, image_name in enumerate(image_names):
            oriented_bboxes = [];
            bboxes = []
            labels = [];#sada
            labels_text = [];
            path = util.io.join_path(data_path, image_name);
            print "\tconverting image: %d/%d %s"%(idx, len(image_names), image_name);
            image_data = tf.gfile.FastGFile(path, 'r').read()#read image
            
            image = util.img.imread(path, rgb = True);
            shape = image.shape
            h, w = shape[0:2];
            h *= 1.0;
            w *= 1.0;



            # gt_filepath = util.io.join_path(gt_path, gt_name);
            # lines = util.io.read_lines(gt_filepath);
                
            for index in image_path_index[idx][0].tolist():
                image_label=image_csv[index]
                # print image_label[0]
                # line = util.str.remove_all(line, '\xef\xbb\xbf')
                # gt = util.str.split(line, ',');
                oriented_box = [int(image_label[i+1]) for i in range(8)];
                oriented_box = np.asarray(oriented_box) / ([w, h] * 4);
                oriented_bboxes.append(oriented_box);
                
                xs = oriented_box.reshape(4, 2)[:, 0]                
                ys = oriented_box.reshape(4, 2)[:, 1]
                print xs
                xmin = xs.min()
                xmax = xs.max()
                ymin = ys.min()
                ymax = ys.max()
                bboxes.append([xmin, ymin, xmax, ymax])

                # might be wrong here, but it doesn't matter because the label is not going to be used in detection
                labels_text.append(image_label[-1]);
                ignored = util.str.contains(image_label[-1], '###')
                if ignored:
                    labels.append(config.ignore_label);
                else:
                    labels.append(config.text_label)
            example = convert_to_example(image_data, image_name, labels, labels_text, bboxes, oriented_bboxes, shape)
            tfrecord_writer.write(example.SerializeToString())
        
if __name__ == "__main__":
    root_dir = util.io.get_absolute_path('/media/scut214/file/HLG/Chinese_Recognition/dataset/')
    output_dir = util.io.get_absolute_path('/media/scut214/file/HLG/Chinese_Recognition/dataset/tfrecord/')
    util.io.mkdir(output_dir);
    print 'kaishile'
    training_data_dir = util.io.join_path(root_dir, 'train_image/')

    cvt_to_tfrecords(output_path = util.io.join_path(output_dir, 'train.tfrecord'), data_path = training_data_dir)
    print 'wanle'
    # verify_data_dir = util.io.join_path(root_dir, 'verify_image/')

    # cvt_to_tfrecords(output_path = util.io.join_path(output_dir, 'verify.tfrecord'), data_path = verify_data_dir)
