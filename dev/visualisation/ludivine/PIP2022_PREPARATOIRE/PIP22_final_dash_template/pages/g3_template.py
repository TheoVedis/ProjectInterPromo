
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from utils import Header
from text import txt_g3 ## import le modul txt_g1 pour utiliser les cases text
from graphes import graphe_g3 ## import le modul des graphes 

##############################################################################################################"# 
## exemple de contenu de tamplate pour ce groupe
content = html.Div([            
##########################################################################################################
########## Premier ligne de contenu layout contient deux graphes avec deux cases text pour l'explication        
                      html.Div([ ### les 2graphes
                        html.Div([dcc.Graph(figure=graphe_g3.fig7),],className="six columns",), ## graphe fig1           
                        html.Div([dcc.Graph(figure=graphe_g3.fig6),],className="six columns",), ## graphe fig3
                        ],
                        className="row ",),
        
                   html.Div([
                            ### les deux cases textes.
                            html.Div([txt_g3.cont_txt_1] ,className="six columns",),  ## text 1
                            html.Div([txt_g3.cont_txt_1],className="six columns",),  ## text 2
                        ],
                        className="row ",),
 ##############################################################################################################"#     
 ###### deuxiéme ligne de contenu layout de ce groupe contient 3 graphe avec 3 cases du text pour l'explication.  
        
                      html.Div([ ### les graphes
                        html.Div([dcc.Graph(figure=graphe_g3.fig7),],className="four columns",), ## graphe fig7
                         
                        html.Div([dcc.Graph(figure=graphe_g3.fig6),],className="four columns",), ## graphe fig6
                         
                        html.Div([dcc.Graph(figure=graphe_g3.fig3),],className="four columns",), ## graphe fig4
                        ],
                        className="row ",),
     
                        html.Div([ ## les trois cases
                            html.Div([txt_g3.cont_txt_1],className="four columns",),
                            html.Div([txt_g3.cont_txt_1],className="four columns",),
                            html.Div([txt_g3.cont_txt_1],className="four columns",),
                        ],
                        className="row ",),        
 ##############################################################################################################"#
######### troisième ligne de contenu layout contient un graphe avec une de text pour l'explication.  
                       html.Div([
                            html.Div([html.Br([]),
#                                     html.Strong("Titre comm 2",style={"color": "#3a3a3a"}, ),
                                    dcc.Graph(figure=graphe_g3.fig4),],className="twelve columns",), ##fig 2
                                 ], className="row ",),
     
                        html.Div([
                            html.Div([txt_g3.cont_txt_1],className="twelve columns",),  ## casetext 
                        ], className="row ",),
  
    ])
##############################################################################################################"# 
##############################################################################################################"# 
def create_layout(app):
    # Page layouts de Groupe
    return html.Div(
        [html.Div([Header(app)]), 
               html.Div([html.Div( [html.H5("Objectif du groupe 3"),html.Br([]), html.P("\L'objectif du groupe est de ....", 
                      style={"color": "#ffffff"},className="row",), ],className="product",style={'backgroundColor':'darkcyan'}) ],className="row", ),
         content,])


#                             html.Div([html.Br([]),
#                                     html.Strong("Titre comm 2",style={"color": "#3a3a3a"}, ),
#                                     dcc.Graph(figure=fig1),],className="six columns",), ##fig 2
#                                         ], className="row ",),