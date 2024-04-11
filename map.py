import pandas as pd
import plotly.express as px

df = pd.read_csv('cross-verified-database.csv', encoding='latin1')

filtered_df = df[df['level3_main_occ'].isin(['mathematician', 'inventor', 'physicist'])]

print("done filtering")

fig = px.scatter_geo(filtered_df,
                     lat='bpla1',
                     lon='bplo1',
                     size=[2] * len(filtered_df),
                     size_max=2,
                     color_discrete_sequence=['red'])
fig.update_layout(title=dict(text='Birthplaces of notable inventors, mathematicians, and physicists', x=0.5, font=dict(size=24)))
fig.show()
