

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#df = pd.read_csv("C:/Users/ibtis/Downloads/train.csv")

'''df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")'''

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
'''barchart.title('Nombre de personnes par vague')
barchart.xlabel('N° de la vague')
barchart.ylabel('Nombre de participants')'''
pio.show(barchart)

#sunburst
fig3 = px.sunburst(
    data_frame = df,
    path =['from','field','race'],
    color = 'from'
)



app.layout = html.Div(children=[
    html.H1(children='EasyDate - AI match'),

    html.Div(children='''
        Prédire si l’amour va opérer entre deux personnes.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=barchart
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)