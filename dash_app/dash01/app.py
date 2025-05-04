import dash
from dash import html
from flask import Flask

# 這個 server 是給 Render 用來掛 Flask 的
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("PatentHunter Dash App"),
    html.P("這是部署在 Render 的 Python Dash 應用程式。")
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=10000)
    # host='0.0.0.0' 和 port=10000 是因為 Render 會將 PORT 設定為環境變數（下一步會處理）
