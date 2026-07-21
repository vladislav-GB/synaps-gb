#app.py

from dash import Dash
from base import start_project

app = Dash(__name__, title="SYNAPS")

app.layout = start_project()

if __name__ == '__main__':
    app.run(debug=True)