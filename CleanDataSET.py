# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:07:00 2022

@author: sibghi
"""

###Nettoyage des données

#importation des modules
from sklearn.impute import KNNImputer
import pandas, numpy as np

#chargement des données
url = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/train.csv?raw=true'
url2 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissions.csv?raw=true'

data = pandas.read_csv(url, sep = ";",header=0)
submissions = pandas.read_csv(url2,sep = ";",header=0)

pandas.set_option("display.max_columns",1000)
pandas.set_option("display.min_row",1000)

####recodage toutes les variables en quanti 

d = data.drop(data.iloc[:,1:64],axis = 1)
d.iloc[:,1:7]= d.iloc[:,1:7].replace(",",".",regex =True).astype(float)
data = data.drop(data.iloc[:,64:70],axis = 1)
#recodage toutes les variables en quanti 

data = data.drop(["field","from","career"],axis = 1)

for var in data.columns:
    if(data[var].dtype == np.float64 or data[var].dtype == np.int64):
           data[var]= data[var].astype(float)
    else:
          data[var]= data[var].str.replace(",",".",regex =True)
          data[var]= data[var].str.replace(".","",regex =True).astype(float).round(0) 

data = data.merge(d, on="iid_pid", how = 'left')

###recodage toutes les variables en quanti 

dsub = submissions.drop(submissions.iloc[:,1:57],axis = 1)
dsub.iloc[:,1:7]= dsub.iloc[:,1:7].replace(",",".",regex =True).astype(float)
submissions = submissions.drop(submissions.iloc[:,57:63],axis = 1)

submissions = submissions.drop(["field","from","career","expnum"],axis = 1)

for var in submissions.columns:
    if(submissions[var].dtype == np.float64 or submissions[var].dtype == np.int64):
           submissions[var]= submissions[var].astype(float)
    else:
          submissions[var]= submissions[var].str.replace(",",".",regex =True)
          submissions[var]= submissions[var].str.replace(".","",regex =True).astype(float).round(0) 

submissions = submissions.merge(dsub, on="iid_pid", how = 'left')

#imputation des NA
imputer1 = KNNImputer(n_neighbors=4)
data = pandas.DataFrame(imputer1.fit_transform(data), columns = data.columns)

###suppession des NA pour fichier train sur les variables iid et pid
data = data.dropna(subset = ["iid","pid"])
#Creation d'une variable IID-PID 
data["pid"] = data["pid"].astype(int)
data["IID_PID"] = np.where(data["iid"]> data["pid"],data["iid"].astype(str) + "-"+data["pid"].astype(str), data["pid"].astype(str) + "-"+data["iid"].astype(str))

data["match"] = data.match.astype(int).round(0)


#suppression des NA
imputer2 = KNNImputer(n_neighbors=4)
submissions = pandas.DataFrame(imputer2.fit_transform(submissions), columns = submissions.columns)
##suppession des NA pour fichier submission sur les variables iid et pid
submissions = submissions.dropna(subset = ["iid","pid"])
#Creation d'une variable IID-PID 
submissions["pid"] = submissions["pid"].astype(int)
submissions["IID_PID"] = np.where(submissions["iid"]> submissions["pid"],submissions["iid"].astype(str) + "-"+submissions["pid"].astype(str), submissions["pid"].astype(str) + "-"+submissions["iid"].astype(str))

#Suppression des variables inutiles 
XSub = submissions.drop(["iid_pid","IID_PID",'amb_o','attr_o','fun_o','id','iid','intel_o','pf_o_amb','pf_o_att','pf_o_fun','pf_o_int','pf_o_sha','pf_o_sin','pid','shar_o','sinc_o','zipcode'],axis = 1)


submissions.to_csv('C:/Users/sibghi/Downloads/submissionsClean.csv',header = True, index=False)
XSub.to_csv('C:/Users/sibghi/Downloads/XSubmission.csv',header = True, index=False)
data.to_csv('C:/Users/sibghi/Downloads/DataClean.csv',header = True, index=False)
