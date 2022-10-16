import pandas as pd

df_pred = pd.read_csv(r'C:/Users/ibtis/OneDrive/Documents/GitHub/ProjetM2Pythion/prediction.csv')#,sep=","
#print(df_pred.head())

#df_pred_1 = df_pred.groupby()
#df_pred_1 = df_pred.groupby(["target"]).agg( {'iid' : 'count'}).sort_values(by ="iid", ascending =False)
df_pred_1 = df_pred.groupby(['target'],as_index=False).agg( {'target' : 'count'})#.sum()
#print(df_pred_1.head())

print(df_pred)













