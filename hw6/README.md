# HW6 輸入領域與變異測試完整作業

本資料夾完成老師題目 5 的兩組 Input Domain Characterization，以及題目 6 Mutation Testing Coverage。

## 最新文件

- [完整 PDF 報告含截圖](HW6_完整作業報告.pdf)
- [可編輯 Word 報告含截圖](HW6_完整作業報告.docx)
- [線上完整案例與變異表](REPORT.md)
- [實際測試截圖與紀錄](evidence/)

## 結果

| 項目 | 結果 |
| --- | --- |
| 課程分類與全部組合 | 4 例、36 例 |
| F(X,Y) 分類與不同輸入組合 | 5 例、15 例 |
| 題目 2×5×3 補充檢查 | 30 項，兩種觀察焦點各跑 15 組輸入 |
| 逐敘述變異 | 12 個變異版本，12/12 被殺死 |
| HW6 | 105 項通過 |
| 全專案 | 129 項通過，92 行與 52 分支出口皆 100% |

**數量說明：** F 的 X 有 5 類、Y 有 3 類，所以不同輸入為 15 組。題目所列 30 在本作業額外實作為兩個觀察焦點的檢查，並不宣稱是 30 組不同輸入，詳見報告。

## 執行

在專案根目錄執行：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r hw6/requirements-py39.txt
.venv/bin/python -m pytest hw6 -v --cov-branch
.venv/bin/python -m pytest -q --cov-branch
```

[課程程式](course.py) · [F 原始程式](function_xy.py) · [12 個變異版本](mutants/) · [變異測試](test_mutation.py)
