from dash import Dash, html, dcc
from DashApp.settings import DEBUG
from DashApp.exception.custom_exception import DashboardTypeException, LayoutNotListException
import plotly.express as px
from pandas import DataFrame as pd_DataFrame
from dataclasses import dataclass


@dataclass
class DashboardFigure(object):
    figure: px.bar
    figure_id: str

    def __init__(self, figure: px.bar, figure_id: str):
        self.figure = figure
        self.figure_id = figure_id


class CustomDash(object):
    def __init__(self, **options):
        self.app = options.get('app', Dash(__name__))
        self.port = options.get('port', 8051)
        self.host = options.get('host', '127.0.0.1')
        self.fig = options.get('fig', px.bar())
        self.title = options.get('title', 'Hello Dash App')
        self.layout = []
        self.dashboards = []

    def run_custom_server(self):
        self.set_lay_out()
        self.app.run_server(host=self.host, debug=DEBUG, port=self.port)

    def set_lay_out(self):
        my_dashboards = [
            html.Div(children=dashboard.create()) for dashboard in self.dashboards
        ]

        self.app.layout = html.Div(
            children=my_dashboards
        )

    def add_dashboard(self, dashboard):
        if not isinstance(dashboard, Dashboard):
            raise DashboardTypeException()

        self.dashboards.append(dashboard)


class Dashboard(object):
    def __init__(self, title=None):
        self.title = title or '''Dash: A web application framework for your data.'''
        self.figures = []

    def add_figure_from_data_frame(self, data_frame=None, figure_id="example"):
        pending_figure = Dashboard.get_figure(data_frame, figure_id=figure_id)
        if self.is_figure_id_duplicate(pending_figure):
            pending_figure.figure_id = pending_figure.figure_id + '_duplicate'

        self.figures.append(pending_figure)

    def is_figure_id_duplicate(self, pending_figure):
        return filter(lambda figure: figure.figure_id == pending_figure.figure_id, self.figures)

    def create(self):
        dashboard_title = html.Div(children=self.title)
        dashboard_figures = [dcc.Graph(
            id=figure.figure_id,
            figure=figure.figure
        ) for figure in self.figures]

        return [
            dashboard_title, *dashboard_figures
        ]

    @staticmethod
    def get_data_frame_from_dict(data_frame: dict = None):
        return pd_DataFrame(data_frame)

    @staticmethod
    def get_figure(data_frame=None, x=None, y=None, color=None,
                   barmode="group", figure_id="example") -> DashboardFigure:
        """
            Sets figure based on the data_frame.
            Assume that axes are the first, second, and third element of the data_frame unless it's defined.
        """
        if not data_frame:
            data_frame = {
                "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
                "Amount": [4, 1, 2, 2, 4, 5],
                "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
            }

        if isinstance(data_frame, dict):
            data_frame = Dashboard.get_data_frame_from_dict(data_frame)

        data_keys = data_frame.keys().tolist()
        x_axis_legend = x or data_keys[0]
        y_axis_legend = y or data_keys[1]
        color_legend = color or data_keys[2]

        return DashboardFigure(
            figure=px.bar(data_frame, x=x_axis_legend, y=y_axis_legend, color=color_legend, barmode=barmode),
            figure_id=figure_id)
