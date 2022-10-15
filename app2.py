from turtle import width
import dash_bootstrap_components as dbc
from dash import html
from dash import Dash, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H2("Easy Date"),width={'size': 6, 'offset': 5},),),
        dbc.Row(dbc.Col(html.P("Prédire si l'amour va opérer entre 2 personnes"),width={'size': 6, 'offset': 4},),),
        dbc.Button("1er graphe", outline=True, color="primary", className="me-1",),
        dbc.Button("2ème graphe", outline=True, color="secondary", className="me-1"),
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
