## Building docker image from local Dockerfile
docker build -t caffe:cpu - < Dockerfile

## Cleaning exited docker containers
# Using --rm argument
docker run --rm -a stdout --volume=$(pwd):/workspace caffe:cpu python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel image.jpg
