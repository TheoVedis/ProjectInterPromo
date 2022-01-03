import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
CARD_TEXT_STYLE = {'textAlign': 'center','color': '#0074D9'}


##### text
cont_txt_1 = dbc.Row([
    dbc.Col(dbc.Card( [dbc.CardBody( [html.H4('Remarques explication sur le graphe ', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text bla bla bla bla bla bala 1.', style=CARD_TEXT_STYLE),]),]),md=12),
])

cont_txt_2 = dbc.Row([
    dbc.Col(dbc.Card( [dbc.CardBody( [html.H4('Card Title de graphe', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text bla bla bla bla bla bal 2.', style=CARD_TEXT_STYLE),]),]),md=12),
])
