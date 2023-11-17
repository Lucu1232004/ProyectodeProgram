import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('Traffic_Crashes_-_Crashes.csv')

mes = df['CRASH_MONTH'].value_counts()
dia = df['CRASH_DAY_OF_WEEK'].value_counts()
hora = df['CRASH_HOUR'].value_counts()
crash = df['CRASH_TYPE'].value_counts()
climaticas = df['WEATHER_CONDITION'].value_counts()

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div(children=[
    html.H1(children='Estadísticas de Accidentes'),

    # Gráfico de barras por mes
    dcc.Graph(
        id='mes-graph',
        figure=px.bar(x=mes.index, y=mes.values, labels={'x': 'Mes del Accidente', 'y': 'Cantidad de Accidentes'},
                      title='Distribución de Accidentes por mes', color_discrete_sequence=['skyblue'])
    ),

    # Gráfico de barras por día
    dcc.Graph(
        id='dia-graph',
        figure=px.bar(x=dia.index, y=dia.values, labels={'x': 'Día del Accidente', 'y': 'Cantidad de Accidentes'},
                      title='Distribución de Accidentes por día', color_discrete_sequence=['skyblue'])
    ),

    # Gráfico de pastel por hora
    dcc.Graph(
        id='hora-pie-chart',
        figure=px.pie(values=hora, names=hora.index, title='Distribución de Accidentes por Hora')
    ),

    # Gráfico de pastel por tipo de accidente
    dcc.Graph(
        id='crash-pie-chart',
        figure=px.pie(values=crash, names=crash.index, title='Tipos de Accidentes')
    ),

    # Gráfico de pastel por condiciones climáticas
    dcc.Graph(
        id='climaticas-pie-chart',
        figure=px.pie(values=climaticas, names=climaticas.index, title='Condiciones Climáticas')
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)