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
# Create traces
#visible='legendonly' disables all legends by default so they need to be turned on interactively
traces=[]
marker_size=4
for i in range(0, df.shape[1], 2):
    x_col = list(df[df.columns[i]])
    y_col = list(df[df.columns[i+1]])
    traces.append(go.Scatter(x=x_col, y=y_col, mode='markers', marker=dict(size=marker_size), visible='legendonly',name=df.columns[i+1]))

# Layout
layout = go.Layout(title='Hall-Heroult Impedance Measurements Lit. Review',
                   xaxis=dict(title='Zr'),
                   yaxis=dict(title='-Zim'),
                   hovermode='closest'
                   )

# Create figure
fig = go.Figure(data=traces, layout=layout)

# Show interactive plot in browser
fig.show()
