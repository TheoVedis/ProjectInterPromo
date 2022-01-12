## exemple des graphe
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
#from plotly.offline import iplot
#from plotly.offline import iplot
### PREMIER GRAPHE 

df_fig1 = pd.read_csv("data/G2_ACP.csv" , sep =';')
df_ech = df_fig1.sample(100000)
df_ech.columns = ["Axe_1", "Axe_2", "Axe_3", "F/NF"]
fig1  = go.Figure([ go.Scatter(
                 mode = 'markers',
                 x = df_ech[df_ech["F/NF"]=='Not_Fraude']["Axe_1"],
                 y = df_ech[df_ech["F/NF"]=='Not_Fraude']["Axe_2"],
                 marker = dict(
                           opacity = 0.2
                         )),
             go.Scatter(
                 mode = 'markers',
                 x = df_ech[df_ech["F/NF"]=='Fraude']["Axe_1"],
                 y = df_ech[df_ech["F/NF"]=='Fraude']["Axe_2"],
                 
                 marker = dict(
                           opacity = 0.5
                          ))
       ])
#iplot(data)

### exemple graphe 
df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
### exemple graphe 
df = px.data.tips()
fig3 = px.box(df, x="time", y="total_bill", points="all")

### exemple graphe 
df = px.data.stocks()
fig4 = px.line(df, x='date', y="GOOG")

### exemple graphe 
long_df = px.data.medals_long()

fig5 = px.bar(long_df, x="nation", y="count", color="medal", title="titre graphe")

### exemple graphe
df = px.data.tips()
fig6 = px.pie(df, values='tip', names='day', color='day',
             color_discrete_map={'Thur':'lightcyan',
                                 'Fri':'cyan',
                                 'Sat':'royalblue',
                                 'Sun':'darkblue'})
### exemple graphe
data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
fig7 = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
               )
fig7.update_xaxes(side="top")



