# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from pages import (
    g1_template,
    g2_template,
    g3_template,
    g4_template,
    g5_template,
    g6_template,
    g7_template,
    g8_template,
    g9_template
)

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],)

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
,style={'background-image': 'url("/assets/credit1.png")',
'background-repeat': 'no-repeat','background-position': 'right top',
        'background-size': '250px 150px'})

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/pages/g1_template":
        return g1_template.create_layout(app)
    elif pathname == "/pages/g2_template":
        return g2_template.create_layout(app)
    elif pathname == "/pages/g3_template":
        return g3_template.create_layout(app)
    elif pathname == "/pages/g4_template":
        return g4_template.create_layout(app)
    elif pathname == "/pages/g5_template":
        return g5_template.create_layout(app)
    elif pathname == "/pages/g6_template":
        return g6_template.create_layout(app)
    elif pathname == "/pages/g7_template":
        return g7_template.create_layout(app)
    elif pathname == "/pages/g8_template":
        return g8_template.create_layout(app)
    elif pathname == "/pages/g9_template":
        return g9_template.create_layout(app)
    else:
        return g1_template.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)