# coding=utf8

import argparse

# 改
datadir = '../../densenet'
data_obs_dir='s3://densenet-214/out/model_15'
parser = argparse.ArgumentParser(description='medical caption GAN')

parser.add_argument(
    '--model',
    '-m',
    type=str,
    default='densenet',
    help='model'
)
parser.add_argument(
    '--data-dir',
    '-d',
    type=str,
    default=datadir + '/data/dataset/',
    help='data directory'
)
parser.add_argument(
    '--data-dir-obs',
    '-dd',
    type=str,
    default='s3://dataset-214/data/dataset',
    help='data directory'
)
parser.add_argument(
    '--save-dir-obs',
    type=str,
    default=data_obs_dir,
    help='data directory'
)
parser.add_argument(
    '--bg-dir',
    type=str,
    default=datadir + '/data/images',
    help='back groud images directory'
)
# 是否使用hard-mining
parser.add_argument(
    '--hard-mining',
    type=int,
    default=0,
    help='use hard mining'
)
parser.add_argument('--phase',
                    default='test',
                    type=str,
                    metavar='S',
                    help='pretrain/train/test phase')
# batchsize
parser.add_argument(
    '--batch-size',
    '-b',
    metavar='BATCH SIZE',
    type=int,
    default=32,
    help='batch size'
)
parser.add_argument('--save-dir',
                    default=datadir + '/data',
                    type=str,
                    metavar='S',
                    help='save dir')
parser.add_argument('--word-index-json',
                    default=datadir+'/files/alphabet_index_dict.json',
                    type=str,
                    metavar='S',
                    help='save dir')
parser.add_argument('--black-json',
                    default=datadir+'/files/black.json',
                    type=str,
                    metavar='S',
                    help='black_list json')
parser.add_argument('--image-hw-ratio-json',
                    default=datadir+'/files/image_hw_ratio_dict.json',
                    type=str,
                    metavar='S',
                    help='image h:w ratio dict')
parser.add_argument('--word-count-json',
                    default=datadir+'/files/alphabet_count_dict.json',
                    type=str,
                    metavar='S',
                    help='word count file')
parser.add_argument('--image-label-json',
                    default= datadir+'/files/train_alphabet.json',
                    type=str,
                    metavar='S',
                    help='image label json')
parser.add_argument('--resume',
                    default='../model/best_f1score_39.ckpt',#/home/work/user-job-dir/model/best_f1score.ckpt
                    type=str,
                    metavar='S',
                    help='start from checkpoints')
# 是否采用数据增强？
parser.add_argument('--no-aug',
                    default=0,
                    type=int,
                    metavar='S',
                    help='no augmentation')
parser.add_argument('--small',
                    default=1,
                    type=int,
                    metavar='S',
                    help='small fonts')
parser.add_argument('--difficult',
                    default=0,
                    type=int,
                    metavar='S',
                    help='只计算比较难的图片')
parser.add_argument('--hist',
                    default=0,
                    type=int,
                    metavar='S',
                    help='采用直方图均衡化')
parser.add_argument('--feat',
                    default=0,
                    type=int,
                    metavar='S',
                    help='生成LSTM的feature')
# parser.add_argument('--result-dir',
#        default='/home/tcd/train_dir/ocr_densenet/',
#        type=int,
#        metavar='S',
#        help='生成LSTM的feature')

#####
parser.add_argument('-j',
                    '--workers',
                    default=8,
                    type=int,
                    metavar='N',
                    help='number of data loading workers (default: 32)')
# 学习率
parser.add_argument('--lr',
                    '--learning-rate',
                    default=0.0001,
                    type=float,
                    metavar='LR',
                    help='initial learning rate')
# 迭代次数
parser.add_argument('--epochs',
                    default=100000,
                    type=int,
                    metavar='N',
                    help='number of total epochs to run')
# 保存频率
parser.add_argument('--save-freq',
                    default='5',
                    type=int,
                    metavar='S',
                    help='save frequency')
parser.add_argument('--save-pred-freq',
                    default='10',
                    type=int,
                    metavar='S',
                    help='save pred clean frequency')
parser.add_argument('--val-freq',
                    default='5',
                    type=int,
                    metavar='S',
                    help='val frequency')
parser.add_argument('--debug',
                    default=0,
                    type=int,
                    metavar='S',
                    help='debug')
parser.add_argument('--input-filter',
                    default=7,
                    type=int,
                    metavar='S',
                    help='val frequency')
parser.add_argument('--use-gan',
                    default=0,
                    type=int,
                    metavar='S',
                    help='use GAN')
parser.add_argument('--write-pred',
                    default=0,
                    type=int,
                    metavar='S',
                    help='writ predictions')
parser.add_argument(
    '--result-file',
    '-r',
    type=str,
    default=datadir + '/data/result/test_result.csv',
    help='result file'
)
parser.add_argument(
    '--output-file',
    '-o',
    type=str,
    default=datadir + '/data/result/test.csv',
    help='output file'
)
args, _ = parser.parse_known_args()
