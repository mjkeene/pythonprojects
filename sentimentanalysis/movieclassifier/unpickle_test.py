import pickle
import numpy as np
import os
from vectorizer import vect

clf = pickle.load(open(
    os.path.join('pkl_objects',
                 'classifier.pkl'), 'rb'))

label = {0: 'negative', 1: 'positive'}
pos_example = ['I love this movie']
neg_example = ['I hate this movie']
X_pos = vect.transform(pos_example)
X_neg = vect.transform(neg_example)

test_list = [X_pos, X_neg]
for x in test_list:
    print('Prediction: %s\n Probability: %.2f%%' % \
      (label[clf.predict(x)[0]],
       np.max(clf.predict_proba(x))*100))

"""
Sample output:
mike@Michaels-MacBook-Pro movieclassifier % python3 unpickle_test.py
Prediction: positive
 Probability: 81.44%
Prediction: negative
 Probability: 57.76%

"""
