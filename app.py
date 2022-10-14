

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio
import base64
#import pygame

app = Dash(__name__)

#image=pygame.image.load("C:\Users\ibtis\OneDrive\Bureau\me\BettyM2_SISE\projet Python\drive-download-20221014T165149Z-001\logo.png")
#app.layout = 

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#df = pd.read_csv("C:/Users/ibtis/Downloads/train.csv")


df = pd.read_csv(r"C:/Users/ibtis/OneDrive/Bureau/me/BettyM2_SISE/projet Python/env1/files/train.csv", sep=";")

fig = px.bar(df, x="wave", y="iid_pid", color="gender", barmode="group")

#fig2 = plt.pie(df["gender"].value_counts(),labels=round(df["gender"].value_counts(normalize=True)*100,2))
fig2 = px.pie(df, values='gender', names='gender')
#plt.title('Répartition des genres')
#plt.show()

#nombre de personnes par vague
df_ = df.drop_duplicates("iid").groupby(["wave"]).agg( {'iid' : 'count'}).sort_values(by ="iid", ascending =False)
df_.insert(0,'wave',df_.index.tolist())
df_=df_[['wave','iid']]
#print(df_)
barchart = px.bar(
    data_frame=df_,
    x='wave',
    y='iid',
    #color="gender",
    opacity=0.9,
    orientation="v",
    barmode="overlay",
    title="Nombre de personnes par vague",
    labels='N° de la vague',
    color_discrete_map={1:"yellow", 0:"blue"}
    #...
)
'''barchart.title('Nombre de personnes par vague')
barchart.xlabel('N° de la vague')
barchart.ylabel('Nombre de participants')'''
#pio.show(barchart)

#sunburst
'''fig3 = px.sunburst(
    data_frame = df,
    path =['from','field','race'],
    color = 'from',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth=-1
)'''


app.layout = html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    html.H1(children='EasyDate - AI match'),
    html.Div(children='Prédire si l’amour va opérer entre deux personnes'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing'))) #, style={'height':'2%', 'width':'2%'}
])

test_png = 'https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')


app.layout = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(test_base64)),
    ])

if __name__ == '__main__':
    app.run_server(debug=True)