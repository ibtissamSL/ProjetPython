

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio
import base64
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
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


#fig_img=px.imshow('logo.png').update_layout
app.layout = html.Div(children=[
    #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
    html.H1(children='EasyDate - AI match'),
    html.Div(children='Prédire si l’amour va opérer entre deux personnes'),
    dcc.Graph(
        id='example-graph',
        figure=barchart
    ),

])

fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/logo.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

##################image
# Create figure
fig_im = go.Figure()

# Constants
img_width = 1600
img_height = 900
scale_factor = 0.5

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig_im.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

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
        source="https://raw.githubusercontent.com/Samibgh/ProjetM2Pythion/main/logo.png")
)

# Configure other layout
fig_im.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
)

# Disable the autosize on double click because it adds unwanted margins around the image
# More detail: https://plotly.com/python/configuration-options/
fig_im.show(config={'doubleClick': 'reset'})

####################image



if __name__ == '__main__':
    app.run_server(debug=True)

    #brouillon 
    #https://community.plotly.com/t/adding-local-image/4896/5  pour insérer les images