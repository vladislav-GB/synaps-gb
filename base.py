#base.py

from dash import html

from components.sidebar import Sidebar
from components.content import Content
from components.statistic_status import RightPanel


def start_project():
    return html.Div(
        [
            Sidebar(),
            Content(),
            RightPanel()
        ],
        className="main"
    )

