#!flask/bin/python

from flask import Flask
from flask import request
from flask import abort
import random
import subprocess
import urllib

app = Flask(__name__)

VALID_EXTENSIONS = ['jpg', 'png', 'jpeg']

def execute_command(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    return stdoutdata

def is_image(URL):
	extension = URL.rsplit('.')[-1]
	returnValue = extension in VALID_EXTENSIONS
	print returnValue
	return returnValue


@app.route('/nsfw/api/v1.0/rating', methods=['GET'])
def index():
	URL = request.headers.get('url')
	hash_code = '%08x' % random.getrandbits(32)
	print hash_code
	print URL
	if not is_image(URL):
		abort(400)
	print 'Hello'
	try:
		urllib.urlretrieve(URL, "images/_%s.jpg" % hash_code)
	except IOError:
		abort(400)
	command = 'docker run --rm --volume=$(pwd):/workspace caffe:cpu python ./classify_nsfw.py --model_def nsfw_model/deploy.prototxt --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel images/_%s.jpg' % hash_code
	print command
	return execute_command(command)

if __name__ == '__main__':
	app.run(debug=True)