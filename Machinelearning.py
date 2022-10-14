# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:07:29 2022

@author: sibghi
"""

"""###Partie Machine Learning"""

##Importation des modules 
import pandas
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import plot_confusion_matrix
from sklearn import metrics

#chargement des données
url = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/DataClean.csv?raw=true'
url2 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissionsClean.csv?raw=true'
url3 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/XSubmission.csv?raw=true'


data = pandas.read_csv(url, sep = ",",header=0)
submissions = pandas.read_csv(url2,sep = ",",header=0)
XSub = pandas.read_csv(url3,sep = ",",header=0)


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

#Mise en place du modele 
clf = AdaBoostClassifier(n_estimators = 300,random_state=0).fit(X_train_resampled,y_train_resampled)
y_pred = clf.predict(Xtest)
print(plot_confusion_matrix(clf, Xtest, ytest))
print(metrics.classification_report(ytest, y_pred))

#performance du modele
print(f1_score(ytest, y_pred, average='macro'))

#prediction avec submission
y_pred2 = clf.predict(XSub)
y_pred2 = pandas.DataFrame(y_pred2)

submissions.iid_pid=submissions.iid_pid.astype(int,0)
sub = pandas.DataFrame(submissions.iid_pid)

sub = pandas.concat([sub,y_pred2], axis=1)


sub.columns = ["iid_pid","target"]
sub

#exportation des fichiers 
sub.to_csv('prediction.csv',header = True, index=False)