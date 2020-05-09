import plotly.graph_objects as go
import pandas as pd
import os

# df = pd.read_csv('data/2014_world_gdp_with_codes.csv')
df = pd.read_csv('data/Exports_of_2002-2019.csv')

# fig = go.Figure(data=go.Choropleth(
#     locations = df['CODE'],
#     z = df['GDP (BILLIONS)'],
#     text = df['COUNTRY'],
#     colorscale = 'Blues',
#     autocolorscale=False,
#     reversescale=True,
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_tickprefix = '$',
#     colorbar_title = 'GDP<br>Billions US$',
# ))
for year in range(2002, 2019):
    fig = go.Figure(data=go.Choropleth(
        locations=df['CODE'],
        z=df[str(year)],
        text=df['Partner'],
        colorscale='Blues',
        autocolorscale=True,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix='$',
        colorbar_title='EXPORTS<br> US$',
    ))

    fig.update_layout(
        title_text=str(year) + ' Exports',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="#">\
                Data Source</a>',
            showarrow=False
        )]
    )

    # fig.show()
    fig.write_image(str(year) + ".png")




