import pandas as pd
import plotly.express as px

tabela = pd.read_csv('vgsales.csv')
tabela1 = tabela[['Rank', 'Name', 'Platform', 'Global_Sales', 'Year', 'NA_Sales']]
tabela1 = tabela1[:30]

fig = px.bar(tabela1, x="Name", y="Global_Sales", color="Platform", title="Jogos mais vendidos",)
fig.update_layout(title_font_size = 22)
fig.update_xaxes(title = '', title_font_size= 22)
fig.update_yaxes(title = 'Unidades vendidas em milhões', title_font_size= 18)
fig.show()