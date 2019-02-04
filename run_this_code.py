from __future__ import division
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
#from sklearn.cross_validation import StratifiedKFold # Add important libs
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix

train=[]
test=[]         #Array Definition
path1 =  r'C:\Users\Megha Agrawal\Desktop\project\codes\total_data_set\train_0.csv'     #Address Definition
path2 =  r'C:\Users\Megha Agrawal\Desktop\project\codes\total_data_set\test_0.csv'
with open(path1, 'r') as f1:    #Open File as read by 'r'
    reader = csv.reader(f1)     
    for row in reader:          #fill array by file info by for loop
        train.append(row)
    train = np.array(train)       	
	
with open(path2, 'r') as f2:
    reader2 = csv.reader(f2)
    for row2 in  reader2:
        test.append(row2)
    test = np.array(test)

parameter_gridsearch = {
                 'max_depth' : [5, 4,6,7,8,9,10,11],  #depth of each decision tree
                 'n_estimators': [50, 20,45],  #count of decision tree
                 'max_features': ['sqrt', 'auto', 'log2'],      
                 'min_samples_split': [2],      
                 'min_samples_leaf': [2],
                 'bootstrap': [True, False],
                 }

randomforest = RandomForestClassifier()
#crossvalidation = StratifiedKFold(train[::,-1], 5)

gridsearch = GridSearchCV(randomforest,             #grid search for algorithm optimization
                               scoring='accuracy',
                               param_grid=parameter_gridsearch,
                               cv=None)


gridsearch.fit(train[0::,0:13:], train[::,-1])    #train[0::,0] is as target
model = gridsearch
print model
parameters = gridsearch.best_params_
print parameters
print('Best Score: {}'.format(gridsearch.best_score_))


path3 =  r'C:\Users\Megha Agrawal\Desktop\project\codes\Random_forest\test\result.csv'

output = gridsearch.predict(test[0::,0:13:])
print output


Actual=test[::,-1]
eff=0
total=0
for i in Actual :
    
    if i == output[total]:
        eff=eff+1
    total=total+1

accuracy1=(eff/total)

print("accuracy : "+ str(accuracy1)+ "\n")
k=confusion_matrix(test[::,-1], output)
print k

print('True Positives:'+str(k[0][0]))
print('False Positives:'+str(k[0][1]))
print('False Negatives:'+str(k[0][1]))
print('True Negatives:'+str(k[1][1]))
