# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:07:29 2022

@author: sibghi
"""

"""###Partie Machine Learning"""

##Importation des modules 
from curses import KEY_SRIGHT
import pandas
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold


def testScore(data,submissions,XSub) : 

  #selection des variables avec une correlation positive a match 
  matrice = data.corr()
  corrMatch = matrice.match.sort_values(ascending=False)
  corrMatch = pandas.DataFrame(corrMatch)
  corrMatch.iloc[:,0][corrMatch.match > 0]
  dataModele = corrMatch.index


  #création de la variable cible 
  Y=data["match"]
  #création de la matrice X
  X=data[dataModele] #filtre avec les variables selectionnees au-dessus
  X = data.drop(["iid_pid","iid","pid","id","match","wave","dec_o", 'expnum', 'order', 'positin1', 'position', 'round',"IID_PID",'fun_o', 'attr_o', 'shar_o', 'intel_o', 'sinc_o','amb_o',"pf_o_att",	"pf_o_sin",	"pf_o_int",	"pf_o_fun",	"pf_o_amb",	"pf_o_sha","zipcode"],axis = 1)


  #On supprime les variables qu'il n'y a pas dans Xsub
  for k in X.columns : 
    if (k not in XSub.columns) : 
      del X[k]

  #separation des fichier train et test 
  Xtrain, Xtest,ytrain,ytest = train_test_split(X,Y,train_size=0.5,random_state=0,stratify=Y)

  #Over sampling avec SMOTE
  smote = SMOTE(sampling_strategy=0.5, k_neighbors = 5, random_state = 0)
  X_train_resampled,y_train_resampled = smote.fit_resample(Xtrain,ytrain)


  ada = AdaBoostClassifier()
  boost = GradientBoostingClassifier()
  tree = DecisionTreeClassifier()
  Rtree = RandomForestClassifier()
  knn = KNeighborsClassifier()

  models = [ada,boost,tree,Rtree,knn]
  score = []
  for model in models:
        model.fit(X_train, y_train) # fit the model
        y_pred= model.predict(X_test) # then predict on the test set
        s= round(f1_score(y_test, y_pred, average='macro'),2) # this gives us how often the algorithm predicted correctly

        score.append(s)
  return (score)

def Prediction(data,submissions,XSub):
  
  matrice = data.corr()
  corrMatch = matrice.match.sort_values(ascending=False)
  corrMatch = pandas.DataFrame(corrMatch)
  corrMatch.iloc[:,0][corrMatch.match > 0]
  dataModele = corrMatch.index


  #création de la variable cible 
  Y=data["match"]
  #création de la matrice X
  X=data[dataModele] #filtre avec les variables selectionnees au-dessus
  X = data.drop(["iid_pid","iid","pid","id","match","wave","dec_o", 'expnum', 'order', 'positin1', 'position', 'round',"IID_PID",'fun_o', 'attr_o', 'shar_o', 'intel_o', 'sinc_o','amb_o',"pf_o_att",	"pf_o_sin",	"pf_o_int",	"pf_o_fun",	"pf_o_amb",	"pf_o_sha","zipcode"],axis = 1)


  #On supprime les variables qu'il n'y a pas dans Xsub
  for k in X.columns : 
    if (k not in XSub.columns) : 
      del X[k]

  #separation des fichier train et test 
  Xtrain, Xtest,ytrain,ytest = train_test_split(X,Y,train_size=0.5,random_state=0,stratify=Y)

  #Over sampling avec SMOTE
  smote = SMOTE(sampling_strategy=0.5, k_neighbors = 5, random_state = 0)
  X_train_resampled,y_train_resampled = smote.fit_resample(Xtrain,ytrain)

  crossvalidation=KFold(n_splits=5,shuffle=True,random_state=1)
  ada=GradientBoostingClassifier()
  search_grid={'n_estimators' : [100, 300, 700, 1000, 2000]}
  search=GridSearchCV(estimator=ada,param_grid=search_grid,scoring='f1_weighted',n_jobs=1,cv=crossvalidation)

  #Mise en place du modele 
  clf = AdaBoostClassifier(n_estimators = 300,random_state=0).fit(X_train_resampled,y_train_resampled)
  y_pred = clf.predict(Xtest)


  #prediction avec submission
  y_pred2 = clf.predict(XSub)
  y_pred2 = pandas.DataFrame(y_pred2)

  submissions.iid_pid=submissions.iid_pid.astype(int,0)
  sub = pandas.DataFrame(submissions.iid_pid)

  sub = pandas.concat([sub,y_pred2], axis=1)


  sub.columns = ["iid_pid","target"]

  return (sub)

