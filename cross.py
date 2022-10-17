# import dash_core_components as dcc
#import dash_html_components as html
# from dash.dependencies import Input, Output

# Connect to main app.py file
# from app import app
# from app import server

# # Connect to your app pages
# from apps import dashboard, predict


# from ctypes import alignment
# from turtle import left
import plotly.graph_objects as go
from dash import Dash
from dash import Dash, html, dcc
# import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

app = Dash(__name__)

df=pd.read_csv('C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/submissionsClean.csv',sep=',',header=0)
df['iid_pid']=df['iid_pid'].astype(int)

pred=pd.read_csv('C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/prediction.csv',sep=',',header=0)

df = pred.merge(df, on='iid_pid',how='left')
#print(df.head())

d = pd.crosstab(df.go_out, df.target)
#plt.plot(d)

barplot=go.Figure()

barplot = d.plot.bar(rot=0)
#plt.show()

app.layout = html.Div(children=
    
 
[

html.Div(children=[
    
    html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#FFC0CB'}),
    html.H2(children='Prédire si l’amour va opérer entre deux personnes',style={'textAlign': 'center', 'color': '#8B008B','font-family':'Lucida Handwriting'}),

   
    ]),


html.Div(children=[
    dcc.Graph(
        id='graph_barchart',
        figure=barplot,
    ),]),

])


if __name__ == '__main__':
    app.run_server(debug=True)
