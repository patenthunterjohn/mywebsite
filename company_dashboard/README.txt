NVIDIA B案（共用框架 + JSON）測試包

結構
----
index.html                  公司入口頁
company.html                所有公司共用的儀表板框架
companies.json              公司索引
data/nvidia/summary.json    NVIDIA 摘要統計
data/nvidia/records.json    NVIDIA 9,522 件代表專利
data/nvidia/classification.json 分類資料
data/nvidia/qa_report.json  QA 報告（網站不會主動載入）

測試
----
因為瀏覽器 file:// 會限制 fetch()，不要直接雙擊 company.html。
在此資料夾執行：
  python -m http.server 8000
然後開：
  http://localhost:8000/
或：
  http://localhost:8000/company.html?c=nvidia

GitHub Pages
------------
整個資料夾內容放到 GitHub Pages 發布目錄即可。
未來新增 AMD 時只需新增 data/amd/ 的 JSON 並更新 companies.json；company.html 不需要複製。
