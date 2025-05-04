import dash
from dash import html
import os

# 初始化 Dash 應用
app = dash.Dash(__name__)

# 設定佈局
app.layout = html.Div([
    html.H1("PatentHunter Dash App"),
    html.P("這是部署在 Render 的 Dash 應用程式。")
])

# 這段程式碼可以省略
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
