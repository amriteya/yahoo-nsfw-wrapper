import subprocess

def runCommandAndGetOuput(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    print stderrdata
    return stdoutdata

print "\n\n\n\n\n\nHello World"
kabali=runCommandAndGetOuput("docker run --volume=$(pwd):/workspace caffe:cpu python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel image.jpg")
#kabali=runCommandAndGetOuput("ls -lrt")
print "\n\n\n\n\n\nHello WWWWW"
print kabali
