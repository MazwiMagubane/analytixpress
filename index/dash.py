from dash import Dash, html, dcc
import django_plotly_dash

app = django_plotly_dash.DjangoDash("SimpleExample")

app.layout = html.Div([
    html.H1("Dash in Django"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}],
            'layout': {'title': 'Simple Graph'}
        }
    )
])
