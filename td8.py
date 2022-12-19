# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:12:09 2022

@author: Romain
"""
from dash import Dash, dash_table
import pandas as pd

df = pd.read_excel("velib.xlsx")

print(df)

app = Dash(__name__)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{"name": i, "id": i} for i in df.columns],

    style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white'
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    },
)

if __name__ == '__main__':
    app.run_server(debug=True)