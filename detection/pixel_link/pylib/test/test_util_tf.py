import util
def test_is_gpu_available():
#	for i in range(4):
	if(util.tf.is_gpu_available()):
		print "GPU is available, %s CUDA installed"%('with' if util.tf.is_gpu_available(True) else 'without');

def test_get_available_gpus():
    devices = util.tf.get_available_gpus();
    for d in devices:
        print d
        
if util.mod.is_main(__name__):
	test_is_gpu_available()
	test_get_available_gpus()
