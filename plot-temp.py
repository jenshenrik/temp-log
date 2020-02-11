from aux import data

in_file = data.get_in_file()
times, temps = data.read_file(in_file)
data.draw_line_graph(times, temps)
