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


    #import plotly.graph_objects as go

# Create figure
#fig = go.Figure()

'''# Add trace
fig.add_trace(
    go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1])
)'''

# Add images
'''fig.add_layout_image(
        dict(
            source="C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/logo.png"
        )
)'''

# Set templates
#fig.update_layout(template="plotly_white")

'''fig.show()'''

'''test_png = 'https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')'''


'''app.layout = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(test_base64)),
    #html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), 
    ])'''


        #html.Div(html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing'))) #, style={'height':'2%', 'width':'2%'}
    '''html.Div(html.Img(src=app.get_asset_url(r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/logo.jpg'),),),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/logo.jpg')
        ], width=6)
    ]) #, style={'height':'2%', 'width':'2%'}'''


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
