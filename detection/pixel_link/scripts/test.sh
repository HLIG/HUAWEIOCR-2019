set -x
set -e
export CUDA_VISIBLE_DEVICES=$1
/home/scut214/anaconda3/envs/pixel_link/bin/python2.7 test_pixel_link.py \
     --checkpoint_path=$2 \
     --dataset_dir=$3\
     --gpu_memory_fraction=-1
     

