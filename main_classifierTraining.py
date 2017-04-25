from createBottleneck import create_bottleneck_folder
from createClassifier import textClassfier

IMG_DIR = '../image'
BOTTLENECK_DIR = '../bottleneck'
INCEPTION_PATH = '../classify_image_graph_def.pb'

create_bottleneck_folder(IMG_DIR, BOTTLENECK_DIR, INCEPTION_PATH)

myClassifier = textClassfier(BOTTLENECK_DIR)
myClassifier.start_training(step=100000, rate=0.03)
myClassifier.save_graph()
