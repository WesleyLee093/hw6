# 軟體正規方法小組專題｜HW1–HW5 階段報告

組別：＿＿＿　組長：＿＿＿　組員：＿＿＿

程式與測試案例可在 [GitHub 專案](https://github.com/alanlu01/software-normalize) 查閱。實測使用 Python 3.14.5、pytest 9.1.1、pytest-cov 7.1.0 與 coverage.py 7.16.2。

## 測試工具

pytest 用 `assert` 比對預期值和實際結果。參數化測試可以用一個函式執行多組資料，並在輸出中個別列出 T1、T2 等案例。無效輸入可用 `pytest.raises` 驗證例外型別，再比對訊息確認是哪一條驗證規則拒絕輸入。

pytest-cov 把 coverage.py 整合到 pytest。終端報表的 `Cover` 顯示涵蓋率，`Missing` 列出漏測行號。HTML 報表可逐行查看顏色標記，`--cov-branch` 可檢查分支出口。專案設定 100% 門檻，低於門檻時命令會以失敗結束。

## 各作業的測試結果

| 作業 | 待測功能 | 最少案例與涵蓋率 |
| --- | --- | --- |
| HW1 工具選擇與示範 | 用 pytest 和 pytest-cov 測試三角形分類 | 4 例，Line 8/8（100%） |
| HW2 Line Coverage | 用迴圈檢查三邊並分類 | 5 例，Line 16/16（100%） |
| HW3 Graph Coverage | 健走集點，每天最多採計兩圈 | Edge 1 例（13/13）；Edge-Pair 3 例（15/15）；Path 3 例（3/3），各 100% |
| HW4 Stress Testing Coverage | 購物車單價與筆數的有效極值與無效類別 | 8 例，10/10 個目標（100%） |
| HW5 Logical Expressions Coverage | 會員且消費達門檻時給折扣 | Predicate 2 例（2/2）；Clause 2 例（4/4）；Combinatorial 4 例（4/4），各 100% |

### HW2｜Line Coverage

三角形分類有五個互斥的返回位置。輸入 `(1, 0, 2)` 在迴圈內被拒絕，`(1, 1, 3)` 因不滿足三角不等式被拒絕，其餘三例 `(2, 2, 2)`、`(2, 2, 3)`、`(3, 4, 5)` 分別得到正三角形、等腰三角形、不等邊三角形。每次呼叫只執行一個 `return`，五個返回位置至少需要五例。 [HW2 案例與行號](https://github.com/alanlu01/software-normalize/tree/main/hw2)

### HW3｜Graph Coverage

用 0、1、4 圈得到 0、1、3 點，依序走完零圈、一圈及採計兩圈三條完整路徑。4 圈的案例在採計第一圈時略過獎勵，第二圈時加點，離開迴圈後回傳，因此單獨涵蓋全部 13 條邊。零圈直接離開、一圈略過獎勵後離開、兩圈進入獎勵三種路徑各有專屬邊對，所以 Edge-Pair 和 Path 都需要三例。 [HW3 路徑與邊對](https://github.com/alanlu01/software-normalize/tree/main/hw3)

### HW4｜Stress Testing Coverage

購物車可有 1～100 筆商品，單價為 10～500 元的整數。`[10]` 回傳 10 元，同時涵蓋有效最少筆數和最低單價。`[500] * 100` 回傳 50,000 元，同時涵蓋有效最多筆數和最高單價。六例分別測購物車型別錯誤、零筆、101 筆、非整數單價、9 元及 501 元，各觸發指定的錯誤。兩個有效極端要分兩次呼叫，每個無效類別也要單獨觸發一次，因此最少八例。 [HW4 有效範圍與案例](https://github.com/alanlu01/software-normalize/tree/main/hw4)

### HW5｜Logical Expressions Coverage

A 為會員資格，B 為購物車小計是否達 1,000 元。兩個布林運算元都會被評估。折扣條件只在 A 和 B 同時為真時成立。

| 案例 | A | B | 判斷結果 | 實際應付 |
| --- | :-: | :-: | :-: | ---: |
| T1 | F | F | F | 960 |
| T2 | F | T | F | 1,260 |
| T3 | T | F | F | 960 |
| T4 | T | T | T | 1,140 |

T1、T4 同時讓整體判斷及每個子條件各出現一次真、一次假。兩個子條件共有四種組合，每次呼叫只命中一種，因此 Combinatorial Coverage 需要四例。 [HW5 輸入與預期結果](https://github.com/alanlu01/software-normalize/tree/main/hw5)

## 工具示範

在專案目錄內，安裝 `requirements.txt` 並啟用虛擬環境後執行：

```sh
python -m pytest hw1 -v
python -m pytest hw2 -v --cov-report=html
python -m pytest hw3 -v -s --cov-branch
python -m pytest hw4 -v --cov-branch
python -m pytest hw5 -v --cov-branch
```

執行 HW2 後打開 `htmlcov/index.html`，點選 `hw2/triangle.py` 查看逐行涵蓋。可再執行 `python -m pytest hw2 -v -k "not T5" --cov-report=html`，觀察第 16 行的 `scalene` 被標成漏測，且 100% 門檻檢查失敗。HW3 用 `-s` 顯示實際輸出，再對照完整路徑表。HW4 查看 T1～T8 各自對應的極值或錯誤。HW5 可用 `python -m pytest hw5 -v -k "T1 or T4"` 示範兩例集合，再與四種組合的完整結果比較。

全套執行 `python -m pytest -v --cov-branch`，共 **24 例通過**，涵蓋 **67/67 行、38/38 個分支出口**。

## 使用心得

- HW2 拿掉 T5 後只漏第 16 行，終端的 `Missing` 和 HTML 的逐行標記可以直接定位少了哪種分類。
- HW3 的報告曾把獎勵判斷畫在迴圈外。逐行核對執行順序後，Edge 的最少案例數從兩例改為一例，Edge-Pair 則需要三例。
- HW5 的 T1、T4 已經能走到整體判斷的兩個分支，四種子條件組合仍要用真值表逐一核對。

## 8 分鐘口頭報告安排

| 時間 | 內容 |
| --- | --- |
| 0:00–1:15 | HW1 工具介紹，展示 pytest 輸出及涵蓋率欄位 |
| 1:15–2:30 | HW2 五個返回位置與 HTML 漏測示範 |
| 2:30–4:15 | HW3 三條完整路徑與三項最少案例數 |
| 4:15–5:45 | HW4 有效範圍、兩個極值案例與六種無效類別 |
| 5:45–7:15 | HW5 真值表，對照兩例與四例的涵蓋結果 |
| 7:15–8:00 | 工具使用心得與全套實測結果 |
