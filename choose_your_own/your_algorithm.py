#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from time import time

### AdaBoost
#from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier(n_estimators=20, learning_rate = 0.8)

### Rndom Forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 20, min_samples_split = 50, min_impurity_decrease = 0.01)
t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
print "Model fitting time:", round(t1-t0, 3), "s"
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print accuracy







try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
