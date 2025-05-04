import dash
from dash import html

# 初始化 Dash 應用
app = dash.Dash(__name__)

# 設定佈局
app.layout = html.Div([
    html.H1("PatentHunter Dash App"),
    html.P("這是部署在 Render 的 Dash 應用程式。")
])

# 只在本地運行時才啟動伺服器
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=10000)
    # host='0.0.0.0' 和 port=10000 是因為 Render 會將 PORT 設定為環境變數（下一步會處理）
