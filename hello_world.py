import streamlit as st 
import pandas as pd
import plotly.graph_objs as go


hackathon = pd.read_csv('hackathon_final.csv')
attended = hackathon[hackathon.iloc[:,-7]=='Asistido']
columns_to_drop = ['prov','Unnamed: 0', 'nombre_ev', 'prod_as_ev', 'fecha_ev', 'loc_ev','estado']
attended.drop(columns_to_drop,axis=1, inplace=True)
print(attended)

# Create a bar plot using Plotly
fig = go.Figure()

fig.add_trace(go.Bar(
    x=['Average Importe Activos 0', 'Average Importe Activos 1'],
    y=[sum(attended.iloc[:,5])/317, sum(attended.iloc[:,6])/317],
    text=[round(sum(attended.iloc[:,5])/317, 2), round(sum(attended.iloc[:,6])/317, 2)],
    textposition='auto',
    marker_color=['blue', 'green']
))

fig.update_layout(
    title='Average Importe Activos 0 and Importe Activos 1',
    yaxis=dict(title='Average Importe Activos'),
    xaxis=dict(title='Category')
)

fig.show()