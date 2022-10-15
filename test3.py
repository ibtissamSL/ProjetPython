import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os 
from PIL import Image
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html

#os.chdir(os.path.dirname(os.path.abspath(__file__)))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Img(src ='C:/Users/lhaton/Desktop/Dash/venv1/Scripts/logo.png')
])

if __name__ == "__main__":
    app.run_server(debug=True)
