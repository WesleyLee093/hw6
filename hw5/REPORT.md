# 作業五｜Logical Expressions Coverage

組別：＿＿＿＿　組長：＿＿＿＿　組員：＿＿＿＿

## 1. 測試目標與折扣規則

測試 `checkout_with_discount(prices, is_member)` 的折扣判斷。函式先以迴圈加總商品單價。當顧客是會員，且購物小計至少為 1,000 元時，折抵小計的 10%，折扣金額無條件捨去至整數。最後加上固定運費 60 元。

| 符號 | 意義 | 何時為真 |
| --- | --- | --- |
| A | `is_member` | 顧客是會員。 |
| B | `meets_threshold` | 商品小計大於或等於 1,000 元。 |
| P | `A & B` | A 與 B 皆為真。 |

兩個運算元皆為布林值。`&` 在這裡執行布林 AND，每次判斷都會評估 A 與 B。測試目標為整體判斷的真假、各子條件的真假、兩個子條件的所有組合。

## 2. 待測程式與流程

函式本體有 12 行可執行敘述，包含加總商品的 `for` 迴圈，以及第 10 行含兩個子條件的 `if` 判斷。 [待測程式](https://github.com/alanlu01/software-normalize/blob/main/hw5/discount.py)

```python
def checkout_with_discount(prices: list[int], is_member: bool) -> int:
    discount_threshold = 1_000
    discount_percent = 10
    shipping_fee = 60
    subtotal = 0
    for price in prices:
        subtotal += price
    meets_threshold = subtotal >= discount_threshold
    discount = 0
    if is_member & meets_threshold:
        discount = subtotal * discount_percent // 100
    discounted_subtotal = subtotal - discount
    return discounted_subtotal + shipping_fee
```

```mermaid
flowchart TD
    START(["開始：輸入單價清單與會員資格 A"]) --> INIT["設定門檻、折扣與運費，小計設為 0"]
    INIT --> NEXT{"還有下一筆商品？"}
    NEXT -->|是| ADD["將單價加到小計"]
    ADD --> NEXT
    NEXT -->|否| CHECK["計算 B（小計至少 1,000 元），折扣設為 0"]
    CHECK --> P{"A 與 B 皆為真？"}
    P -->|真：T4| DISCOUNT["折扣設為小計的 10%，捨去小數"]
    P -->|假：T1、T2、T3| TOTAL["計算小計減折扣，再加 60 元運費"]
    DISCOUNT --> TOTAL
    TOTAL --> RETURN(["回傳應付金額"])
```

## 3. 測試案例與真值表

| 案例 | Input values（單價清單、會員） | Expected result | Test program’s result | Criteria analysis |
| --- | --- | --- | --- | --- |
| T1 | `[400, 500], False` | 960 元 | 960 元 | 小計 900。A=F、B=F、P=F，折扣 0 元。 |
| T2 | `[500, 700], False` | 1,260 元 | 1,260 元 | 小計 1,200。A=F、B=T、P=F，折扣 0 元。 |
| T3 | `[400, 500], True` | 960 元 | 960 元 | 小計 900。A=T、B=F、P=F，折扣 0 元。 |
| T4 | `[500, 700], True` | 1,140 元 | 1,140 元 | 小計 1,200。A=T、B=T、P=T，折扣 120 元。 |

## 4. 涵蓋率與最少案例數

| 測試準則 | 涵蓋目標 | 最少案例 | 涵蓋率 | 最少案例數的依據 |
| --- | --- | --- | --- | --- |
| Predicate Coverage | P 為真及為假 | T1、T4，共 2 例 | 2/2（100%） | 每次呼叫只有一個 P 結果。T1 使 P 為假，T4 使 P 為真。 |
| Clause Coverage | A 為真及為假，B 為真及為假 | T1、T4，共 2 例 | 4/4（100%） | 每次呼叫為 A、B 各提供一個值。T1 同時測到兩個假，T4 同時測到兩個真。 |
| Combinatorial Coverage | (F,F)、(F,T)、(T,F)、(T,T) | T1～T4，共 4 例 | 4/4（100%） | 兩個獨立布林值有 2 × 2 種組合。每次呼叫只能命中一種。 |

四個案例合起來就能同時達到三種準則的 100%。Combinatorial Coverage 需要全部四例，因此共用集合最少也需要四例。

## 5. 工具驗證

### 環境與指令

實測環境為 Python 3.14.5、pytest 9.1.1、pytest-cov 7.1.0 與 coverage.py 7.16.2。從專案根目錄建立虛擬環境並安裝依賴。

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell 使用 `py -m venv .venv`，後續以 `.\.venv\Scripts\python.exe` 取代各指令中的 `python`。

### HW5 完整測試

```sh
python -m pytest hw5 -v --cov-branch --color=no
```

終端輸出節錄如下。

```text
hw5/test_logical_coverage.py::test_logical_expressions[T1] PASSED        [ 25%]
hw5/test_logical_coverage.py::test_logical_expressions[T2] PASSED        [ 50%]
hw5/test_logical_coverage.py::test_logical_expressions[T3] PASSED        [ 75%]
hw5/test_logical_coverage.py::test_logical_expressions[T4] PASSED        [100%]

Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
hw5/discount.py      13      0      4      0   100%
-------------------------------------------------------------
TOTAL                13      0      4      0   100%
Required test coverage of 100.0% reached. Total coverage: 100.00%
============================== 4 passed in 0.03s ===============================
```

### Predicate 與 Clause 的共用最小集合

```sh
python -m pytest hw5 -v --cov-branch -k "T1 or T4" --color=no
```

終端輸出節錄如下。

```text
hw5/test_logical_coverage.py::test_logical_expressions[T1] PASSED        [ 50%]
hw5/test_logical_coverage.py::test_logical_expressions[T4] PASSED        [100%]

Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
hw5/discount.py      13      0      4      0   100%
-------------------------------------------------------------
TOTAL                13      0      4      0   100%
Required test coverage of 100.0% reached. Total coverage: 100.00%
======================= 2 passed, 2 deselected in 0.03s ========================
```

完整測試 4 例皆通過，13 個程式敘述與 4 個分支出口皆有執行。只跑 T1 和 T4 時，2 例通過、2 例未選取，工具仍顯示 100%。由真值表可得 Predicate 2/2、Clause 4/4、Combinatorial 2/4（50%）。 [測試程式](https://github.com/alanlu01/software-normalize/blob/main/hw5/test_logical_coverage.py)

### HTML 涵蓋率報表

```sh
python -m pytest hw4 hw5 --cov-branch --cov-report=term-missing --cov-report=html
```

合跑實測為 `12 passed`，`30` 個程式敘述、`18` 個分支出口皆有執行。開啟 `htmlcov/index.html` 後，點選待測檔案可查看逐行標色。終端的 `Missing` 欄列出漏測的行或分支。
