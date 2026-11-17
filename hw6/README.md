# HW6：Input Domain Characterization

對應老師題目 5-1／5-2。沿用專案編號，新增為 HW6。

- [完整中文報告與 4／36 例案例表](REPORT.md)
- [待測程式：課程資料摘要](course.py)
- [可執行測試](test_input_domain.py)

分類：Level `{600, 700, 800}`、Major `{swe, cs, isa, infs}`、學生人數 `{0, 1, >1}`（多人以 3 人代表）。
Categorization：4 例涵蓋 10/10 類別。Combinatorial：36 例涵蓋 36/36 組合。
另有 1 項測試集合完整性檢查，共 41 項通過。

在專案根目錄執行：

```sh
.venv/bin/python -m pytest hw6 -v --cov-branch
```

本機 Python 3.9 的套件安裝方式及完整測試指令見報告。

## 作業說明文件與截圖

[下載 Word 作業說明文件](HW6_作業說明含截圖.docx)：說明本次完成內容、測試設計、實測結果及重現步驟，附 4 張截圖。

截圖來源為程式碼及實際 pytest 輸出的本機網頁畫面；[原始測試紀錄與圖片](document_assets/)一併保留供核對。

[開啟含截圖的 PDF 版本](HW6_作業說明含截圖.pdf)：固定版面共 5 頁，截圖在第 2～4 頁；若 Word 預覽沒有顯示圖片，可直接查看這份 PDF。
