from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
url = 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissionsClean.csv?raw=true'
submission = pd.read_csv(url,sep = ",",header=0)


fig = px.bar(submission, x="gender", y="income", color="gender", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Speed Dating'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)