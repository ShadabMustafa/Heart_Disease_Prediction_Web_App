# Libraries need to be imported for dash app to function as intended.
import base64
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, callback
from plotly.subplots import make_subplots
from sqlTab import hdPresent, hdNotPresent, ageVals, cpHDpresent2

# Basic Pie graph to describe presence of heart disease.
labels = ['Present', 'Not Present']
values = [hdPresent(), hdNotPresent()]
title = 'Heart Disease Present or Not Pie-graph'
df1 = pd.DataFrame(values, labels)
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=values, name=""),
              1, 1)
fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.update_layout(
    title_text=title)

# Basic histogram to describe distribution of age
df2 = pd.DataFrame(ageVals(), columns=['Age'])
fig2 = px.histogram(df2, title='Age Frequency Histogram', x='Age')

# Basic bar chart to describe relationship of chest pain type and heart disease
df3 = pd.DataFrame(cpHDpresent2(), columns=['Chest Pain Type', 'Heart Disease Present'])

fig3 = px.histogram(df3, x="Chest Pain Type",
                    color='Heart Disease Present', barmode='group', title='Heart Disease Frequency Per Chest Pain Type')

df4 = pd.read_csv('heart-diseaseV3.csv')

# Used to add interactivity to data set table.
@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else ""

# Function returns created and formatted dash app.
def createDashApp(flask_app):
    #Dash app is connected to flask app.
    dash_app = dash.Dash(server=flask_app,
                         name="Dashboard",
                         url_base_pathname=
                         "/dashboard/")

    # Used to format dash app to look as it should.
    with flask_app.app_context(), flask_app.test_request_context():
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        layout_dash = os.path.join(ROOT_DIR, "templates", "base_dash.html")
        with open(layout_dash, "r") as f:
            html_body = (f.read())

            dash_app.index_string = html_body

    dash_app.title = 'Dashboard'

    # Adds image of dataset variable correlation matrix.
    image_filename = 'static/HDcorMatrix.png'
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())

    # Dash app layout and proper formatting.
    dash_app.layout = html.Div(children=[
        html.H1(children='Data Visualizations and Dataset', style={'textAlign': 'center'}),

        html.Div(children='''
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        dcc.Graph(
            id='example-graph2',
            figure=fig2
        ),
        dcc.Graph(
            id='example-graph3',
            figure=fig3
        ),
        html.Br(),
        html.H3(children='Variable Correlation Matrix',style={'textAlign': 'center'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
        html.H2('Dataset:', style={'textAlign': 'center'}),
        dbc.Container([
            dbc.Label(''),
            dt.DataTable(
                id='tbl', data=df4.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df4.columns],
            ),
            dbc.Alert(id='tbl_out'),
        ])

    ], style={'background-color': 'ghostwhite', 'margin': '0 27%', 'border': '15px #070700'})

    return dash_app
