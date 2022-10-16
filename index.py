#first page that will be loaded (interface)


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import dashboard, predict


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        #dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Dashboard|', href='/apps/dashboard'),
        dcc.Link('Prédictions', href='/apps/predict'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    if pathname == '/apps/predict':
        return predict.layout
    else:
        return "Welcome"


if __name__ == '__main__':
    app.run_server(debug=False)