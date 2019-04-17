
import tensorflow as tf
import cv2

def date_reader(fn,batch_size=128):
    '''
    阅读tfrecord文件，返回image,label的batch
    fn:
    batch_size:

    '''
    files = tf.train.match_filenames_once(fn)
    filename_queue = tf.train.string_input_producer(files, shuffle=False)
    reader = tf.TFRecordReader()
    _,serialized_example = reader.read(filename_queue)

    features = tf.parse_single_example(
    serialized_example,
    features={
        'image_raw':tf.FixedLenFeature([],tf.string),
        'label':tf.FixedLenFeature([],tf.int64)
    })

    images=tf.decode_raw(features['image_raw'],tf.uint8)
    labels = tf.cast(features['label'], tf.int64)
    image_float=tf.cast(images,tf.float32)

    images.set_shape([199*79])
    min_after_dequeue = 10000
    capacity = min_after_dequeue + 3 * batch_size

    image_batch, label_batch = tf.train.shuffle_batch([images, labels],
                                                  batch_size=batch_size, 
                                                    capacity=capacity, 
                                                    min_after_dequeue=min_after_dequeue)

    return image_batch,label_batch

tfRecord_fn='train.tfrecords'
#files = tf.train.match_filenames_once(tfRecord_fn)

#filename_queue = tf.train.string_input_producer(files, shuffle=False)

#reader = tf.TFRecordReader()
#_,serialized_example = reader.read(filename_queue)

#features = tf.parse_single_example(
#    serialized_example,
#    features={
#        'image_raw':tf.FixedLenFeature([],tf.string),
#        'label':tf.FixedLenFeature([],tf.int64)
#    })
#images=tf.decode_raw(features['image_raw'],tf.uint8)
#image_float=tf.cast(images,tf.float32)

#labels = tf.cast(features['label'], tf.int64)
#min_after_dequeue = 10000
#batch_size = 100
#capacity = min_after_dequeue + 3 * batch_size
#images.set_shape([199*79])
#image_batch, label_batch = tf.train.shuffle_batch([images, labels],
#                                                  batch_size=batch_size, 
#                                                    capacity=capacity, 
#                                                    min_after_dequeue=min_after_dequeue)
#image_batch, label_batch = date_reader(tfRecord_fn)



#with tf.Session() as sess:
#    sess.run((tf.global_variables_initializer(),
#              tf.local_variables_initializer()))
#    coord=tf.train.Coordinator()
#    threads=tf.train.start_queue_runners(sess=sess,coord=coord)
#	#开启多线程
#    image_=image_batch
#    label_ = label_batch
#    print(image_.shape,image_.dtype)
#    image=image_[0].eval(session=sess).reshape([79,199])
#    label=label_[0].eval(session=sess)
#    print(image.shape)
#    print(label)
#    cv2.imshow('source',image)
#    cv2.waitKey()

#    image=image_[0].eval(session=sess).reshape([79,199])
#    label=label_[0].eval(session=sess)
#    print(image.shape)
#    print(label)
#    cv2.imshow('source',image)
#    cv2.waitKey()
#    #等待线程退出
#    coord.request_stop()
#    coord.join(threads)
#cv2.destroyAllWindows()