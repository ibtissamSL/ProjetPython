from ctypes import alignment
from doctest import OutputChecker
from gc import callbacks
from turtle import left
import plotly.graph_objects as go
from dash import Dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt

#df = pd.read_csv(r"C:/Users/ibtis/OneDrive/Bureau/me/BettyM2_SISE/projet Python/env1/files/train.csv", sep=";")
df=pd.read_csv(r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/submissionsClean.csv',sep=',')
#df_ = df.drop_duplicates("iid").groupby(["wave"]).agg( {'iid' : 'count'}).sort_values(by ="iid", ascending =False)
#df_.insert(0,'wave',df_.index.tolist())
#df_=df_[['wave','iid']]

app = Dash(__name__)

colors = {
    'background': '#F0F8FF',
    #'text': '#7FDBFF'
}


def recode(age) :
    if age<25.0  :
        return "0-25 ans"
    elif age >25.0 and age<35.0 :
        return "26-35 ans"
    elif age >35.0 :
        return "plus de 35 ans"

df['age_recode'] = df['age'].apply(recode)
df_age = df.drop_duplicates('iid')['age_recode'].value_counts()


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

fig_pie = px.pie(df, values='career_c', names='career_c')
#fig.show()




app.layout = html.Div(style={'backgroundColor': '#F8F8FF' },children=
    
 
[





html.Div(children=[
dcc.Graph(
    id='graph_fig_logo2_2',
    figure=fig_logo2_2#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
    
),],),

html.Div(children=[
    
    html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#FFC0CB'}),
    html.H2(children='Prédire si l’amour va opérer entre deux personnes',style={'textAlign': 'center', 'color': '#8B008B'}),
    #dcc.Graph(
     #   id='graph_fig_im',
      #  figure=fig_im,
   # ),
   
    ]),


html.Div(children=[
dcc.Graph(
    id='graph_fig_im',
    figure=fig_im#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
    #"width": "100%", "display": "flex", 
),],style = {'margin-left' : '350px'}),

html.Div(children=[
dcc.RadioItems(options=['career_c','age','gender','race'],id='my-radio-btn'),],style = {'margin-left' : '350px'}),

#html.Div(dcc.RadioItems(options=['career','age','gender','race'],value=('career'),id='my-radio-btn'),)

#dcc.Markdown(children='',id='my-radio-btn'),

#'career','field','age','race','from' => barplot

# html.Div(children=[
# dcc.Graph(
#     id='graph_fig_pie',
#     #figure=fig_pie#style={'textAlign': 'center'}#'width':'75%', 'margin':25, 
#     #"width": "100%", "display": "flex", 
# ),],style = {'margin-left' : '350px'}),

html.Div(dcc.Graph(id='graph')),

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





# html.Div(children=[
#     #html.Img(src=app.get_asset_url('https://drive.google.com/file/d/1bYdHUNetNhSvCfCRCqhfzBHCKgrVUIpG/view?usp=sharing')),
    
#     #html.H1(children='EasyDate - AI match',style={'textAlign': 'center', 'color': '#7FDBFF'}),
#     #html.Div(children='Prédire si l’amour va opérer entre deux personnes'),

#     dcc.Graph(
#         id='graph_barchart',
#         figure=barchart,
#     ),]),

])

#callback pour changer le piechart selon la valeur selectionnée
@app.callback(

    Output(component_id='graph', component_property='figure'),
    Input(component_id='my-radio-btn',component_property='value')
)
def update_text(value) :#selected_text, selected_font_size
    #print(value)
    #fig_pie = px.pie(df, values=value, names=value)
    #return (fig_pie)
    #return(value)
    #print(selected_font_size)
    #if value == 'career':
        #dff = dff.groupby([ctg_value], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
        #df=pd.read_csv(r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/submissionsClean.csv',sep=',')

    if value=="gender" :
        fig_pie= px.pie(df.drop_duplicates('iid')['gender'].value_counts(),values='gender', names='gender') #,values='gender', names='gender'
    #fig_pie = plt.pie(df.drop_duplicates('iid')['gender'].value_counts(), labels = ["26-35 ans","0-25 ans","plus de 35 ans"]) #,values='gender', names='gender'
        return fig_pie
    if value =='age' :
        fig_pie = px.pie(df.drop_duplicates('iid')['age_recode'].value_counts(), values='age_recode', names='age_recode')
        return fig_pie
    else :
        fig_pie = px.pie(df, values=value, names=value)
        return fig_pie

    # fig_pie = px.pie(df, values=value, names=value)
    # return fig_pie

    # elif value == 'gender':
    #     # if len(s_value) == 0:
    #     #     return {}
    #     # else:
    #     #dff = dff.groupby([ctg_value, 'year'], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
    #     fig_pie = px.pie(df, values=value, names=value)
    #     return fig_pie
    # elif value == 'race':
    #     fig_pie = px.pie(df, values=value, names=value)
    #     return fig_pie


if __name__ == '__main__':
    app.run_server(debug=True)




#     '''html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div([
#         #dcc.Link('Video Games|', href='/apps/vgames'),
#         dcc.Link('Dashboard|', href='/apps/dashboard'),
#         dcc.Link('Prédictions', href='/apps/predict'),
#     ], className="row"),
#     html.Div(id='page-content', children=[])
# ]),'''