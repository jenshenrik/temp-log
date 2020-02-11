import plotly.graph_objects as go
import csv

times = []
temps = []

with open('temp-log.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        times.append(row[0])
        temps.append(row[1])

fig = go.Figure()
fig.add_trace(go.Scatter(x=times, y=temps, mode="lines+markers", name="Temperaturudvikling"))
fig.show()
