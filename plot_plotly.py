import plotly.graph_objects as go
import pandas as pd
import os
import glob
# Data

# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

df = pd.read_excel(csv_files[0])
Zr1 = [0, 2, 6, 7, 9]
Zim1 = [2, 4, 12, 15, 20]

Zr2 = [5, 7, 13, 12, 14]
Zim2 = [6, 8, 16, 19, 24]

# Create traces
traces=[]
for i in range(0, df.shape[1], 2):
    x_col = list(df[df.columns[i]])
    y_col = list(df[df.columns[i+1]])
    traces.append(go.Scatter(x=x_col, y=y_col, mode='markers', name=df.columns[i+1]))


#trace1 = go.Scatter(x=Zr1, y=Zim1, mode='markers', name='Dataset 1')
#trace2 = go.Scatter(x=Zr2, y=Zim2, mode='markers', name='Dataset 2')

# Layout
layout = go.Layout(title='Zr vs Zim Interactive Plot',
                   xaxis=dict(title='Zr'),
                   yaxis=dict(title='Zim'),
                   hovermode='closest')

# Create figure
fig = go.Figure(data=traces, layout=layout)

# Show interactive plot in browser
fig.show()
