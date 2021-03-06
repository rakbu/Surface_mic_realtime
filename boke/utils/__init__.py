from utils.models import load_model, MFCC13, process_data

import sys
sys.modules['__main__'].MFCC13 = MFCC13
model, preprocessor = load_model('utils/SVM-best.model')

from functools import partial
preprocessor = partial(process_data, preprocessor=preprocessor)

from utils.data import Sound
sound = Sound()
