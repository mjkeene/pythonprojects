import pickle
import os
from sgd_classifier import stop
from sgd_classifier import clf

dest = os.path.join('movieclassifier', 'pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(stop,
           open(os.path.join(dest, 'stopwords.pkl'), 'wb'), protocol=4)

pickle.dump(clf,
           open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol=4)
