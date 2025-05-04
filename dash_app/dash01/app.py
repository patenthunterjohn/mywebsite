import dash
from dash import html

# 初始化 Dash 應用
app = dash.Dash(__name__)

# 設定佈局
app.layout = html.Div([
    html.H1("PatentHunter Dash App"),
    html.P("這是部署在 Render 的 Dash 應用程式。")
])

# 使用 Render 自動分配的端口
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
    # os.environ.get("PORT", 10000) 會首先從環境變數中讀取 PORT，如果沒有設置，則使用預設的端口 10000。這樣無論在哪個環境中運行，都能使用 Render 提供的端口。
