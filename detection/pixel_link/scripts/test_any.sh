set -x
set -e

export CUDA_VISIBLE_DEVICES=1

python test_pixel_link_on_any_image.py \
            --checkpoint_path=$2 \
            --dataset_dir=$3 \
            --eval_image_width=2048\
            --eval_image_height=2048\
            --pixel_conf_threshold=0.8\
            --link_conf_threshold=0.8\
            --gpu_memory_fraction=0.9
            
#
            # --pixel_conf_threshold=0.7\
            # --link_conf_threshold=0.7\



            # --pixel_conf_threshold=0.8\
            # --link_conf_threshold=0.8\



            # --eval_image_width=1024\
            # --eval_image_height=1024\
            # --pixel_conf_threshold=0.7\
            # --link_conf_threshold=0.9\

#./scripts/test_any.sh 3 checkpoint/model.ckpt-146343 /media/scut214/file/HLG/Chinese_Recognition/dataset/padding_testset
#./scripts/test_any.sh 3 checkpoint/model.ckpt-146343 /media/scut214/file/HLG/Chinese_Recognition/pixel_link-master/samples/