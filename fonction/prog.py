# -*- coding: utf-8 -*-


from Machinelearning import testScore, Prediction

from CleanDataSET import CleanData
import pandas

#chargement des données
url = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/train.csv?raw=true'
url2 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissions.csv?raw=true'

data = pandas.read_csv(url, sep = ";",header=0)
submissions = pandas.read_csv(url2,sep = ";",header=0)

a=CleanData(data, submissions)


a[0].to_csv("https://github.com/Samibgh/ProjetM2Pythion/tree/main/datasets/submissionsClean.csv")

a[1].to_csv("https://github.com/Samibgh/ProjetM2Pythion/tree/main/datasets/XSubmission.csv")
a[2].to_csv("https://github.com/Samibgh/ProjetM2Pythion/tree/main/datasets/DataClean.csv")

#chargement des données
url = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/DataClean.csv?raw=true'
url2 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissionsClean.csv?raw=true'
url3 = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/XSubmission.csv?raw=true'


data = pandas.read_csv(url, sep = ",",header=0)
submissions = pandas.read_csv(url2,sep = ",",header=0)
XSub = pandas.read_csv(url3,sep = ",",header=0)

testScore(data,submissions,XSub)

sub = Prediction(data,submissions,XSub)

sub.to_csv("https://github.com/Samibgh/ProjetM2Pythion/tree/main/datasets/prediction.csv")
