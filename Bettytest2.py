#this is a copy of the test2.py

"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
import pandas as pd
import plotly.graph_objs as go
import io
import base64
import plotly.express as px
import matplotlib.pyplot as plt
from Activite import ActSub,ActTrain,Nuagemot , FreqDate, FreqSortie,carSub,carTrain

app = dash.Dash(external_stylesheets=[dbc.themes.MATERIA])
server = app.server

#urlSub= 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/submissionsClean.csv?raw=true'
df = pd.read_csv(r"C:/Users/samib/Documents/GitHub/ProjetM2Pythion/submissionsClean.csv",sep = ",",header=0)
df["iid_pid"] = df["iid_pid"].astype(int)

#urlSub= 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/DataClean.csv?raw=true'
Train = pd.read_csv(r"C:/Users/samib/Documents/GitHub/ProjetM2Pythion/DataClean.csv",sep = ",",header=0)

#urlPred= 'https://github.com/Samibgh/ProjetM2Pythion/blob/main/prediction.csv?raw=true'
pred = pd.read_csv(r"C:/Users/samib/Documents/GitHub/ProjetM2Pythion/prediction.csv",sep = ",",header=0)

df = pred.merge(df, on="iid_pid", how = 'left')

def recode(age) :
    if age<25.0  :
        return "0-25 ans"
    elif age >25.0 and age<35.0 :
        return "26-35 ans"
    elif age >35.0 :
        return "plus de 35 ans"

df['age_recode'] = df['age'].apply(recode)
df_age = df.drop_duplicates('iid')['age_recode'].value_counts()

Train['age_recode'] = Train['age'].apply(recode)
Train_age = Train.drop_duplicates('iid')['age_recode'].value_counts()



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

##############################      fig_im    begin     ######################################
# Create figure
fig_im = go.Figure()

# Constants
img_width = 1600
img_height = 800
scale_factor = 0.5#0.5

# '''# Add invisible scatter trace.
# # This trace is added to help the autoresize logic work.
# fig_im.add_trace(
#     go.Scatter(
#         x=[0, img_width * scale_factor],
#         y=[0, img_height * scale_factor],
#         mode="markers",
#         marker_opacity=0
#     )
# )'''

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

# '''# Add invisible scatter trace.
# # This trace is added to help the autoresize logic work.
# fig_im.add_trace(
#     go.Scatter(
#         x=[0, img_width * scale_factor],
#         y=[0, img_height * scale_factor],
#         mode="markers",
#         marker_opacity=0
#     )
# )'''

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

##############################      fig_logo2_2    end     ####################################################

#Appel des fonctions
ActS = ActSub(df)
ActT = ActTrain(Train)
Nuagemot(ActT,ActS, 'tab20b','tab20b' )
FreqSortie(df)
FreqDate(df)
carTrain(Train)
carSub(df)

tab = html.Div(
    [
        html.H2("Speed Dating", style = {"font-size" : 50, "text-align": "center"}),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label = "Acceuil", tab_id="Acceuil"),
                dbc.Tab(label = "DashBoard", tab_id="DashBoard"),
                dbc.Tab(label = "Prediction", tab_id="prediction"),
            ],
            id = "onglet", active_tab="Acceuil"
        ),
    ], style = {"color": "black"}
)


CountMatch = pd.DataFrame(pred["target"].value_counts())
CountMatch = CountMatch.reset_index()
CountMatch.columns = ["Match","target"]

content = dbc.Container( 

    [
        
        html.Div([
  
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
            #     ),
   
        ]),


        html.Div(children=[
        dcc.Graph(
            id='graph_fig_im',
            figure=fig_im#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
            #"width": "100%", "display": "flex", 
        ),],style = {'margin-left' : '350px'}),
                        
    ],
        id= "active_accueil"
    ),
    html.Div([

        #Liste déroulante pour sélection du fichier Train ou Submission
         html.Div([
            html.Br(),
            dcc.Dropdown(['Train', 'Submissions'], id='dropdown', value='Submissions'),
         ],
         style = {'width' : '350px'}
         ),

        #RadioItems pour sélection des données à afficher
        html.Div(children=[
        dcc.RadioItems(options=['career_c','age','gender','race','field_cd'],id='my-radio-btn',value='career_c'),],style = {'margin-top' : '35px','margin-left' : '35px'}),

        #affichage du graphe après sélection des 3 paramètres 
        html.Br(),
        html.Div(dcc.Graph(id='graph')),

        html.Div([
            html.H3('Nuage de mots Train'),
           html.Img(src=r"assets/Trainmots.png",alt="image",style ={ "text-align" : "center" }),

         ], style= {"width" : 550, "display" : "inline-block" , "margin"  : 5}),

         html.Div([
             html.H3('Nuage de mots Submissions'),
             html.Img(src=r"assets/Submots.png",alt="image",style ={"text-align" : "center" })
         ],  style= {"width" : 550, "display" : "inline-block" , "margin"  : 5})
    ],
    id="active_dashboard"
    ),
    html.Div([
        html.Br(),

        html.Br(),
        html.H4("Répartition des matchs prédis : "),
        dbc.Table.from_dataframe(CountMatch, striped=True, bordered=True, hover=True),
        html.Br(),

        html.Div([
            html.H3('Nuage de mots Train'),
           html.Img(src=r"assets/FreqSortie.png",alt="image",style ={ "text-align" : "center" }),

         ], style= {"width" : 500, "display" : "inline-block" , "margin"  : 5}),

         html.Div([
             html.H3('Nuage de mots Submissions'),
             html.Img(src=r"assets/FreqDate.png",alt="image",style ={"text-align" : "center" })
         ],  style= {"width" : 500, "display" : "inline-block" , "margin"  : 5})

    ],
    id="active_pred"
    )
    ]
 )

app.layout = html.Div([tab, content])


@app.callback([Output("active_accueil", "style"),Output("active_dashboard", "style"), Output("active_pred", "style")],
                                                                [Input("onglet","active_tab")])
def render_tab_content(active_tab):

    on = {"display":"block"}

    off = {"display":"none"}

    if active_tab is not None:

        if active_tab == "Acceuil":

            return on, off, off

        elif active_tab == "DashBoard":

            return off, on, off

        elif active_tab == "prediction":

            return off, off,on

    return "No tab selected"




@app.callback(Output(component_id='graph', component_property='figure'), 
    [Input(component_id='my-radio-btn',component_property='value'),Input(component_id='dropdown',component_property='value')])

def update_output(value,value2):
 
    if value2 == "Train":
        if value=="gender" :
            fig_pie= px.pie(Train.drop_duplicates('iid')['gender'].value_counts(),values='gender', names='gender',color_discrete_sequence=px.colors.sequential.RdBu) #,values='gender', names='gender'
            #fig_pie = plt.pie(df.drop_duplicates('iid')['gender'].value_counts(), labels = ["26-35 ans","0-25 ans","plus de 35 ans"]) #,values='gender', names='gender'
            return fig_pie
        if value =='age' :
            fig_pie = px.pie(Train.drop_duplicates('iid')['age_recode'].value_counts(), values='age_recode', names='age_recode',color_discrete_sequence=px.colors.sequential.RdBu)
            return fig_pie
        if value == "career_c" : 
            im = html.Img(src=r"assets/carriereTrain.png",alt="image",style ={"text-align" : "center" })
            return im
        else :
            fig_pie = px.pie(Train.drop_duplicates('iid')[value].value_counts(), values=value, names=value,color_discrete_sequence=px.colors.sequential.RdBu)
            return fig_pie
            
    else :
        if value=="gender" :
            fig_pie= px.pie(df.drop_duplicates('iid')['gender'].value_counts(),values='gender', names='gender',color_discrete_sequence=px.colors.sequential.Viridis) #,values='gender', names='gender'
            #fig_pie = plt.pie(df.drop_duplicates('iid')['gender'].value_counts(), labels = ["26-35 ans","0-25 ans","plus de 35 ans"]) #,values='gender', names='gender'
            return fig_pie
        if value =='age' :
            fig_pie = px.pie(df.drop_duplicates('iid')['age_recode'].value_counts(), values='age_recode', names='age_recode',color_discrete_sequence=px.colors.sequential.Viridis)
            return fig_pie
        if value == "career_c" : 
            im = html.Img(src=r"assets/FreqDate.png",alt="image",style ={"text-align" : "center" })
            return im
        else :
            fig_pie = px.pie(df, values=value, names=value,color_discrete_sequence=px.colors.sequential.Viridis)
            return fig_pie



if __name__ == "__main__":
    app.run_server(debug = True)