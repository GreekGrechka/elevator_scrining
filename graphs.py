from bokeh.plotting import *

def create_graph1():
    p = figure(title='Пример линейного графика', x_axis_label='Время', y_axis_label='Шум (дБ)')
    x = [1, 2, 3, 4, 5]
    y = [25, 54, 34, 65, 23]
    p.line(x, y, legend_label='Линия', line_color='green', line_width=2)
    output_file('graphs/Noise_graph.html', title='Elevator sensor')
    save(p)

def create_graph2():
    p = figure(title='Пример линейного графика', x_axis_label='Время', y_axis_label='Вибрации (Гц)')
    x = [1, 2, 3, 4, 5]
    y = [465, 345, 1021, 678, 346]
    p.line(x, y, legend_label='Линия', line_color='green', line_width=2)
    output_file('graphs/Vibration_graph.html', title='Elevator sensor')
    save(p)

def graph_1():
    s = ''
    with open('graphs/Noise_graph.html') as f:
        for i in f.readlines():
            s += i
    return s

def graph_2():
    s = ''
    with open('graphs/Vibration_graph.html') as f:
        for i in f.readlines():
            s += i
    return s