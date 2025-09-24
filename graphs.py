from bokeh.plotting import *

def create_graph1():
    x = []
    y = []
    with open('data/file_2.txt', 'r') as f:
        while True:
            s = f.readline()
            if not s:
                break
            s = s[:-1]
            s = s.split(' ')
            for i in range(len(s)):
                if i == 0:
                    y.append(s[i])
                elif i == 2:
                    x.append(s[i])
    p = figure(title='График шума', x_axis_type="datetime", x_axis_label='Время', y_axis_label='Шум (дБ)')
    p.line(x, y, legend_label='Линия', line_color='green', line_width=2)
    for i in range(len(y)):
        if int(y[i]) >= 75:
            p.scatter(x[i], int(y[i]), marker='circle', size=7, color='red')
        else:
            p.scatter(x[i], int(y[i]), marker='circle', size=7, color='green')
    output_file('graphs/Noise_graph.html', title='Elevator sensor')
    save(p)

def create_graph2():
    x = []
    y = []
    with open('data/file_2.txt', 'r') as f:
        while True:
            s = f.readline()
            if not s:
                break
            s = s[:-1]
            s = s.split(' ')
            for i in range(len(s)):
                if i == 1:
                    y.append(s[i])
                elif i == 2:
                    x.append(s[i])
    p = figure(title='График вибрации', x_axis_type="datetime", x_axis_label='Время', y_axis_label='Вибрации (Гц)')
    p.line(x, y, legend_label='Линия', line_color='green', line_width=2)
    for i in range(len(y)):
        if int(y[i]) >= 1000:
            p.scatter(x[i], int(y[i]), marker='circle', size=7, color='red')
        else:
            p.scatter(x[i], int(y[i]), marker='circle', size=7, color='green')
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