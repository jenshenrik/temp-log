import plotly.graph_objects as go
import sys
import csv

INDEX_ERROR_MESSAGE = """
IndexError caught. Are you sure your input file is correctly formatted?
"""

TOO_FEW_ARGUMENTS_ERROR_MESSAGE = """
Please pass the name of a csv file as an argument
"""

TOO_MANY_ARGUMENTS_ERROR_MESSAGE = """
Too many arguments passed. Please pass the name of a csv file as an argument
"""

def get_in_file():
    if len(sys.argv) < 2:
        print(TOO_FEW_ARGUMENTS_ERROR_MESSAGE)
        sys.exit(0)
    
    if len(sys.argv) > 2:
        print(TOO_MANY_ARGUMENTS_ERROR_MESSAGE)
        sys.exit(0)

    return sys.argv[1]

def read_file(filename):
    times = []
    temps = []
    
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        try:
            for row in csv_reader:
                times.append(row[0])
                temps.append(row[1])

            return times, temps
        except IndexError:
            print(INDEX_ERROR_MESSAGE)
            sys.exit(1)

def draw_line_graph(x_data, y_data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode="lines+markers"))
    fig.update_yaxes(range=[5,15])
    fig.show()
