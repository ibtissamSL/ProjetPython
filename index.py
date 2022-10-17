#first page that will be loaded (interface)


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import dashboard, predict


from ctypes import alignment
from turtle import left
import plotly.graph_objects as go
from dash import Dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#df_
df = pd.read_csv(r"C:/Users/ibtis/OneDrive/Bureau/me/BettyM2_SISE/projet Python/env1/files/train.csv", sep=";")
df_ = df.drop_duplicates("iid").groupby(["wave"]).agg( {'iid' : 'count'}).sort_values(by ="iid", ascending =False)
df_.insert(0,'wave',df_.index.tolist())
df_=df_[['wave','iid']]


#barchart
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

##############################      fig_logo2_2    begin     ######################################
# Create figure
fig_logo2_2 = go.Figure()
fig_logo2_2.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/images/logo2.png",
       xref="paper", yref="paper",
       x=1, y=1.05,
       sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)
# Constants
img_width = 260#160
img_height = 180#90
scale_factor = 0.5

'''# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig_im.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)'''

# Configure axes
fig_logo2_2.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig_logo2_2.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig_logo2_2.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        #source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg")
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/images/logo2.png"),
        #xanchor = "center", #Sets the anchor for the x position. "left" | "center" | "right"
        #yanchor = "middle", #Sets the anchor for the y position. "top" | "middle" | "bottom"
        
)

# Configure other layout
fig_logo2_2.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
    #align="center"
    
)

##############################      fig_logo2_2    end    ######################################

##############################      fig_im    begin     ######################################
# Create figure
fig_im = go.Figure()

# Constants
img_width = 1600
img_height = 800
scale_factor = 0.5#0.5

'''# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig_im.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)'''

# Configure axes
fig_im.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig_im.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig_im.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        #source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg")
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/images/logo.png"),
        #xanchor = "center", #Sets the anchor for the x position. "left" | "center" | "right"
        #yanchor = "middle", #Sets the anchor for the y position. "top" | "middle" | "bottom"
        
)

# Configure other layout
fig_im.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
    #align="center"
    
)

##############################      fig_im    end    ######################################


##############################      fig_logo2    begin     ######################################

#fig_logo2
fig_logo2 = go.Figure()
fig_logo2.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/images/logo2.png",
       xref="paper", yref="paper",
       x=1, y=1.05,
       sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

##############################      fig_logo2    end    ######################################

app.layout = html.Div(style={'backgroundColor': '#F8F8FF' },children=[

    html.Div(children=[
dcc.Graph(
    id='graph_fig_logo2_2',
    figure=fig_logo2_2#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
    
),],),

html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    #html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#7FDBFF'}),
    #html.Div(children='Prédire si l’amour va opérer entre deux personnes'),
    
    html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#FFC0CB'}),
    html.H2(children='Prédire si l’amour va opérer entre deux personnes',style={'textAlign': 'center', 'color': '#8B008B'}),
    #dcc.Graph(
     #   id='graph_fig_im',
      #  figure=fig_im,
   # ),
   
    ]),



html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        #dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Dashboard   |   ', href='/apps/dashboard'),
        dcc.Link('Prédictions', href='/apps/predict'),
    ], className="row",style={'font-size': '40px'}),
    html.Div(id='page-content', children=[])
],style={'textAlign': 'center', 'color': '#7FDBFF'}),

html.Div(children=[
dcc.Graph(
    id='graph_fig_im',
    figure=fig_im#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
    #"width": "100%", "display": "flex", 
),],style = {'margin-left' : '350px'}),
                        


#,style = {"width": "100%", "display": "flex", "align-items": "center", "justify-content": "center"}'''
#fig_im

html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#7FDBFF'}),
    html.H4(children='Prédire si l’amour va opérer entre deux personnes',style={'textAlign': 'center', 'color': '#7FDBFF'}),
    dcc.Graph(
        id='graph_fig_logo2',
        figure=fig_logo2,
    ),]),




html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    #html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#7FDBFF'}),
    #html.Div(children='Prédire si l’amour va opérer entre deux personnes'),

    dcc.Graph(
        id='graph_barchart',
        figure=barchart,
    ),]),
    ])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    if pathname == '/apps/predict':
        return predict.layout
    else:
        #return "Welcome"
        return html.H1(children='Welcome',style={'textAlign': 'center', 'color': '#8B008B'}) # #7FDBFF


if __name__ == '__main__':
    app.run_server(debug=False)