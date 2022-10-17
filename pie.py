import plotly.express as px
import pandas as pd 
# This dataframe has 244 lines, but 4 distinct values for `day`

df = pd.read_csv(r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/submissionsClean.csv',sep=',')

#df = pd.read_csv(r'/content/submissionsClean.csv',sep=',')

fig = px.pie(df, values='career_c', names='career_c')
fig.show()


