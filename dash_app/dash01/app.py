import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div("Hello from Dash on Render!")

server = app.server  # for render to find the WSGI server

if __name__ == "__main__":
    app.run_server(debug=True)
