#from ctypes import alignment
import plotly.graph_objects as go
from dash import Dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#app = Dash(__name__)


layout = html.Div([

    html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#FFC0CB'}),
    html.H2(children='Prédire si l’amour va opérer entre deux personnes',style={'textAlign': 'center', 'color': '#8B008B'}),
    ]),
    
    ])

#if __name__ == '__main__':
 #   app.run_server(debug=True)