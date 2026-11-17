# 軟體正規方法小組作業

- 程式語言為 Python。驗證環境為 Python 3.14.5。
- 單元測試使用 pytest，行與分支涵蓋率使用 pytest-cov（coverage.py）。
- [報告用 Markdown](REPORT.md)包含工具介紹、各作業結果、示範流程與使用心得。

| 作業 | 測試目標與結果 |
| --- | --- |
| [HW1 選擇語言與工具](hw1/README.md) | 工具介紹、功能說明及 4 例 Line Coverage 示範。 |
| [HW2 Line Coverage](hw2/README.md) | 5 例，16/16 行（100%）。 |
| [HW3 Graph Coverage](hw3/README.md) | Edge 1 例（13/13）、Edge-Pair 3 例（15/15）、Path 3 例（3/3），均為 100%。 |
| [HW4 Stress Testing Coverage](hw4/README.md) | 8 例，10/10 個有效極值與無效類別目標（100%）。[單項報告與流程圖](hw4/REPORT.md) |
| [HW5 Logical Expressions Coverage](hw5/README.md) | Predicate 2 例（2/2）、Clause 2 例（4/4）、Combinatorial 4 例（4/4），均為 100%。[單項報告與流程圖](hw5/REPORT.md) |
| [HW6 Input Domain Characterization](hw6/README.md) | Categorization 4 例（10/10 類別）、Combinatorial 36 例（36/36 組合），均為 100%。[中文報告](hw6/REPORT.md) |

## HW2 與 HW3 修正紀錄

- HW2 原本沿用 8 行且沒有迴圈的三角形示範。現在使用自己的三角形分類函式，逐邊檢查並收集不同邊長，函式本體有 15 行可執行敘述。Line Coverage 的最少案例數更新為 5。
- HW3 原本的函式只有 7 行，報告把實際位於迴圈內的獎勵判斷寫在迴圈外。現在把基本點數和獎勵分開計算，函式本體有 12 行可執行敘述，並依實際路徑更新 Edge、Edge-Pair 和 Path 的分析。

## 安裝與執行

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v --cov-branch
```

Windows PowerShell 可用 `py -m venv .venv` 建立環境，再用 `.\.venv\Scripts\python.exe` 執行安裝與測試指令。

`pytest` 會自動顯示涵蓋率與遺漏行號，並檢查 100% 門檻。可加上 `--cov-report=html` 產生有逐行標色的 `htmlcov/index.html`。各作業指定的涵蓋率依各自的案例表與分析計算。

## HW6 本機驗證

本次使用 Python 3.9.6，請依 [HW6 報告](hw6/REPORT.md) 安裝相容套件。全套 65 項通過，79/79 行、44/44 分支出口均為 100%。原 HW1～HW5 的環境與歷史結果保留於原報告。
