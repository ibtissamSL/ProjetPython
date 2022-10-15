from turtle import width
import dash_bootstrap_components as dbc
from dash import html
from dash import Dash, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3("Easy Date"),width={'size': 6, 'offset': 5},),),
        dbc.Button("Primary", outline=True, color="primary", className="me-1",),
        dbc.Button("Secondary", outline=True, color="secondary", className="me-1"),
        dbc.Button("Success", outline=True, color="success", className="me-1"),
        dbc.Button("Warning", outline=True, color="warning", className="me-1"),
        dbc.Button("Danger", outline=True, color="danger", className="me-1"),
        dbc.Button("Info", outline=True, color="info", className="me-1"),
        dbc.Button("Light", outline=True, color="light", className="me-1"),
        dbc.Button("Dark", outline=True, color="dark"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
