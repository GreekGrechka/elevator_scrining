from numpy import *
from flask import *
from graphs import graph_1, graph_2, create_graph1, create_graph2

create_graph1()
create_graph2()

app = Flask(__name__)

@app.route('/graph1')
def get_graph1():
    return graph_1()

@app.route('/graph2')
def get_graph2():
    return graph_2()

@app.route('/')
def index():
    p = graph_1()
    p_2 = graph_2()

    return render_template('index_1.html', context={'p':p, 'p_2':p_2})

# Открытие приложения +
if __name__ == '__main__':
    app.run(debug=True)