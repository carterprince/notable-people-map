import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cross-verified-database.csv', encoding='latin1')

occupations = ['inventor', 'mathematician', 'physicist', 'philosopher', 'engineer', 'computer_scientist', 'biologist']
colors = ['#d6c400', 'blue', 'red', 'purple', 'orange', 'black', 'lime']

fig = go.Figure()

for occ, color in zip(occupations, colors):
    #filtered_df = df[(df['level3_main_occ'] == occ) & (df['birth'] >= 1960)]
    filtered_df = df[df['level3_main_occ'] == occ]
    fig.add_trace(go.Scattergeo(
        lat=filtered_df['bpla1'],
        lon=filtered_df['bplo1'],
        mode='markers',
        marker=dict(
            size=1.5,
            color=color,
            opacity=1
        ),
        name=occ.capitalize().replace("_", " "),
        hovertemplate='%{text}<extra></extra>',
        text=filtered_df['name'].str.replace('_', ' ')
    ))

fig.update_layout(
    title=dict(text='Birthplaces of notable inventors, mathematicians, and physicists', x=0.5, font=dict(size=24)),
    showlegend=True,
    geo=dict(
        scope='world',
        resolution=50,
        projection_type='natural earth',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        countrycolor='rgb(204, 204, 204)'
    )
)

fig.show()
