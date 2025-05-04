import dash
from dash import html

from flask import Flask
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("Hello from Dash!"),
    html.P("這是部署在 Render 上的 Dash App。")
])

if __name__ == "__main__":
    app.run_server(debug=True)
