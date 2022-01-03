## exemple des graphe
import plotly.graph_objs as go
import plotly.express as px
### exemple graphe 
data_canada = px.data.gapminder().query("country == 'Canada'")
fig1 = px.bar(data_canada, x='year', y='pop')
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
