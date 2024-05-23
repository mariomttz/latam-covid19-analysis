# Librerias y modulos
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from dash import Dash, html, dcc, Input, Output

# Datos
# Declaramos la ruta de los datos
path = 'C:\\Users\\Mario Martínez\\Documents\\latam-covid19-analysis\\data\\'

# Cargamos los datos
mexico = pd.read_csv(path + 'mexico\\covid_2020.csv', nrows = 10000)

# Creamos nuestro dashboard
app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

# Definimos el layout del dashboard
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('Dashboard COVID-19 México')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.H2('Casos confirmados'),
            html.H3(mexico.shape[0])
        ],
        width = 4),

        dbc.Col([
            html.H2('Casos activos')
        ],
        width = 4),

        dbc.Col([
            html.H2('Fallecimientos')
        ],
        width = 4),
    ]),

    dbc.Row([
        dbc.Col([
            html.H2('Distibución de las edades'),
            dcc.Graph(
                figure = px.histogram(mexico, x = 'EDAD', nbins = 50)
            )
        ],
        width = 6),

        dbc.Col([
            html.H2('Distribución de los casos por sexo'),
            dcc.Graph(
                figure = px.pie(mexico, names = 'SEXO')
            )
        ],
        width = 6),
    ]),
])

# Corremos el dashboard
if __name__ == '__main__':
    app.run_server(debug = True)