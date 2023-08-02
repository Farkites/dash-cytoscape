import dash
from dash import (
    html,
    callback,
    clientside_callback,
    ClientsideFunction,
    Input,
    Output,
    State,
    dcc,
)
import dash_cytoscape as cyto
import dash_leaflet as dl
from dash_cy_leaflet import DashCyLeaflet

cyto.load_extra_layouts()

app = dash.Dash(__name__)
server = app.server


elements = [
    {"data": {"id": "a", "label": "Node A", "lat": 28.4636, "lon": -16.2518}},
    {"data": {"id": "b", "label": "Node B", "lat": 28.4636, "lon": -16.2525}},
    {"data": {"id": "ab", "source": "a", "target": "b"}},
]

cy_stylesheet = [
    {
        "selector": "node",
        "style": {
            "width": "20px",
            "height": "20px",
        },
    },
    {
        "selector": "edge",
        "style": {
            "width": "10px",
        },
    },
    {
        "selector": "node",
        "style": {
            "label": "data(label)",
        },
    },
]

default_div_style = {
    "height": "600px",
    "width": "800px",
    "border": "2px solid gray",
    "padding": "10px",
    "margin": "5px",
}

# App
app.layout = html.Div(
    [
        html.Div(
            DashCyLeaflet(
                id="my-cy-leaflet",
                cytoscape_props=dict(
                    elements=elements,
                    stylesheet=cy_stylesheet,
                ),
            ),
            style=default_div_style,
        ),
        html.Div(id="bounds-display"),
    ],
)


@callback(
    Output("bounds-display", "children"),
    Input({"id": "my-cy-leaflet", "sub": "leaf"}, "bounds"),
)
def display_leaf_bounds(bounds):
    return "Leaflet bounds:" + str(bounds)


if __name__ == "__main__":
    app.run_server(debug=True)
