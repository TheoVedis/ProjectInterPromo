import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [html.Div(
            [html.Div([html.Div([html.H4("")],
                       className="seven columns main-title",),],className="twelve columns")],className="row",),
         html.Div([html.Div([html.H4("Dashboard Projet Interpromo SID 2022")],
                               className="seven columns main-title",),],
                       className="twelve columns",style={"padding-left": "0"}, ) ],  className="row",)
    return header
## Menu pour naviguer entre les groupes
def get_menu():
    menu = html.Div(
        [
        dcc.Link("G1 Outliers Supervisée",href="/pages/g1_template",className="tab",
            style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G2 Outliers Non Supervisé",href="/pages/g2_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G3 Clustering",href="/pages/g3_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G4 Intimité Différentielle",href="/pages/g4_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G5 Génération Observations",href="/pages/g5_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G6 Statistiques D",href="/pages/g6_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G7 Représ des parcours",href="/pages/g7_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G8 Préd sans webtracking",href="/pages/g8_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        dcc.Link("G9 Préd avec webtracking",href="/pages/g9_template",className="tab",
                style={ 'font-family': 'Arial, Helvetica, sans-serif','font-size':'15px','font-weight': 'bold'}),
        ],
        className="row all-tabs",
    )
    return menu
