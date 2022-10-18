from doctest import DocFileCase
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def ActSub(df):
    #Les activités les plus populaires - Submissions
    Activites=df.iloc[:,35:53]
    Activites["iid"] = df["iid"]
    Activites.drop_duplicates("iid").groupby(["sports",	"tvsports",	"exercise",	"dining",	"museums",	"art"	,"hiking","gaming"	,"clubbing","reading",	"tv",	"theater"	,"movies",	"concerts",	"music",	"shopping",	"yoga"	]).mean()
    Activites = Activites.drop('career_c',axis=1)

    liste=[]
    for i in Activites:
        Moy=round(Activites.drop_duplicates("iid")[i].mean(),2)
        liste.append(Moy)
    liste= liste[:-1]
    MoyAct = pd.DataFrame(liste)
    Activites =Activites.loc[:,Activites.columns!="iid"]
    MoyAct.index = Activites.columns
    MoyAct.columns = ["Moy"]
    MoyAct.sort_values(by ="Moy", ascending =False)

    MoyAct = pd.DataFrame(MoyAct)
    
    return (MoyAct)

def ActTrain(df): 
    Activites=df.iloc[:,41:61]
    Activites["iid"] = df["iid"]
    Activites.drop_duplicates("iid").groupby(["sports",	"tvsports",	"exercise",	"dining",	"museums",	"art"	,"hiking","gaming"	,"clubbing",
                                        "reading",	"tv",	"theater"	,"movies",	"concerts",	"music",	"shopping",	"yoga","exphappy","expnum"	]).mean()

    liste=[]
    for i in Activites:
        Moy=round(Activites.drop_duplicates("iid")[i].mean(),2)
        liste.append(Moy)
    liste= liste[:-1]
    MoyAct = pd.DataFrame(liste)
    Activites =Activites.loc[:,Activites.columns!="iid"]
    MoyAct.index = Activites.columns
    MoyAct.columns = ["Moy"]
    MoyAct.sort_values(by ="Moy", ascending =False)

    MoyAct = pd.DataFrame(MoyAct)

    return (MoyAct)




def Nuagemot(Train, Sub, color1, color2):
    
    cloud_generator1 = WordCloud(background_color='white',
                            random_state=1, colormap = color1)
    cloud_generator2 = WordCloud(background_color='white',
                            random_state=1,  colormap = color2)

    wordcloud_image = cloud_generator1.fit_words(Train.Moy)
    plt.imshow(wordcloud_image, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("assets/Trainmots.png") #enregistrement de l'image
    plt.clf()

    wordcloud_image = cloud_generator2.fit_words(Sub.Moy)
    plt.imshow(wordcloud_image, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("assets/Submots.png") #enregistrement de l'image
    plt.clf()


def FreqSortie(df):
    d = pd.crosstab(df.go_out,df.target)
    plt.plot(d)
    plt.legend(['No Match','Match'])
    plt.title("Fréquence des sorties")
    plt.savefig("assets/FreqSortie.png") #enregistrement de l'image
    plt.clf()

def FreqDate(df): 
    d = pd.crosstab(df.date,df.target)
    plt.plot(d)
    plt.legend(['No Match','Match'])
    plt.title("Fréquence des dates")
    plt.savefig("assets/FreqDate.png") #enregistrement de l'image
    plt.clf()


def carSub(df):
    carriere = pd.DataFrame(df.career_c)

    carriere = carriere.value_counts().sort_index()
    carriere.index = ["Lawyer" ,"Academic/Research", "Psychologist" ,"Doctor/Medicine", "Engineer", "CreativeArts/Entertainment", "Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/" ,"International/HumanitarianAffairs", "Undecided" ,"SocialWork","Politics","Other","Journalism"]
    carriere.columns = ["carriere", "count"]
    carriere = carriere.sort_values(ascending = False)

    fig = plt.figure()
    ax = fig.add_axes([0,0,5,2])
    ax.bar(list(carriere.index) ,list(carriere.values))
    plt.savefig("assets/carSub.png") #enregistrement de l'image
    plt.clf()

def carTrain(df):
    df["career_c"] = df.career_c.astype(int)
    carriere = pd.DataFrame(df.career_c)
    carriere = carriere.value_counts().sort_index()
    carriere.index =["Lawyer" ,"Academic/Research", "Psychologist" ,"Doctor/Medicine", "Engineer", "Creative/Arts/Entertainment", "Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/" ,"Admin Real Estate" ,"International/HumanitarianAffairs", "Undecided" ,"SocialWork","SpeechPathology","Politics","Prosports/Athletics","Other","Architecture"]
    carriere.columns = ["carriere", "count"]
    carriere = carriere.sort_values(ascending = False)

    fig = plt.figure()
    ax = fig.add_axes([0,0,5,2])
    ax.bar(list(carriere.index) ,list(carriere.values))
    plt.savefig("carriereTrain.png") #enregistrement de l'image
    plt.clf()