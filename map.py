import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cross-verified-database.csv', encoding='ISO-8859-1')

df['name'] = df['name'].apply(lambda x: x.encode('ISO-8859-1').decode('utf-8', 'ignore'))

occ_colors = {
    'philosopher': 'purple',
    'geneticist': 'green',
    'biologist': 'lime',
    'computer_scientist': 'black',
    'inventor': '#d6c400',
    'engineer': 'orange',
    'mathematician': 'blue',
    'physicist': 'red',
}

def add_actual_trace(fig, occupation, color):
    filtered_df = df[df['level3_main_occ'] == occupation]
    fig.add_trace(go.Scattergeo(
        lat=filtered_df['bpla1'],
        lon=filtered_df['bplo1'],
        mode='markers',
        marker=dict(
            size=1.5,
            color=color,
            opacity=1
        ),
        name=occupation.capitalize().replace("_", " "),
        hovertemplate='%{text}<extra></extra>',
        text=filtered_df['name'].str.replace('_', ' '),
        legendgroup=occupation, 
        showlegend=False
    ))

def add_dummy_trace(fig, occupation, color):
    fig.add_trace(go.Scattergeo(
        lat=[None],
        lon=[None],
        mode='markers',
        marker=dict(
            size=10,
            color=color
        ),
        name=occupation.capitalize().replace("_", " "),
        legendgroup=occupation,
        showlegend=True
    ))

fig = go.Figure()

for occ, color in occ_colors.items():
    add_actual_trace(fig, occ, color)
    add_dummy_trace(fig, occ, color)

fig.update_layout(
    title=dict(text='Birthplaces of notable people in STEM and Philosophy', x=0.5, font=dict(size=24)),
    showlegend=True,
    geo=dict(
        scope='world',
        resolution=50,
        projection_type='natural earth',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        showcountries=True,
        countrycolor='rgb(204, 204, 204)',
        countrywidth=0.5
    )
)

fig.show()
