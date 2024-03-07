import pickle
import numpy as np
import os
from vectorizer import vect

clf = pickle.load(open(
    os.path.join('pkl_objects',
                 'classifier.pkl'), 'rb'))

label = {0: 'negative', 1: 'positive'}
pos_example = ['I love this movie, it\'s awesome']
neg_example = ['I hate this movie, it sucks']
X_pos = vect.transform(pos_example)
X_neg = vect.transform(neg_example)

# these are real movie reviews found online for Airplane vs. Volcano
# okay fine the positive one was actually from Interstellar since I couldn't find
# a good positive one for Airplane vs. Volcano
pos_real = ['Definitely one of the best films of its decade! Nolan manages to nail the balance '
            'between theoretical quantum physics, and all the elements which make up a visual '
            'masterpiece through well-paced storytelling and a fantastic, gripping plot about '
            'the power of love which crosses beyond the boundaries of distance and interstellar '
            'travel. Truly one of Nolan\'s greatest works!']
neg_real = ['This has to be the worst film ever, through terrible cgi, shocking acting, '
            'hilarious incorrect information such as there\'s a code for the autopilot '
            'no one seems to know to the military personal getting the aircraft wrong. '
            'Absolutely shocking, avoid if you can']
X_pos_real = vect.transform(pos_real)
X_neg_real = vect.transform(neg_real)

test_list = [X_pos, X_neg, X_pos_real, X_neg_real]
for x in test_list:
    print('Prediction: %s\n Probability: %.2f%%' % \
      (label[clf.predict(x)[0]],
       np.max(clf.predict_proba(x))*100))

"""
Sample output: (all of the predictions are correct)
mike@Michaels-MacBook-Pro movieclassifier % python3 unpickle_test.py
Prediction: positive
 Probability: 89.13%
Prediction: negative
 Probability: 70.02%
Prediction: positive
 Probability: 95.53%
Prediction: negative
 Probability: 94.44%
"""
