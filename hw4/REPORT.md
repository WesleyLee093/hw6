# 作業四｜Stress Testing Coverage

組別：＿＿＿＿　組長：＿＿＿＿　組員：＿＿＿＿

## 1. 測試目標與有效範圍

測試購物車金額函式 `checkout_total(prices)`。依作業規格，檢查有效範圍內的最低單價、最高單價、最少筆數及最多筆數，並驗證六種無效輸入。全部共 10 個涵蓋目標。

| 資料 | 有效條件 | 無效類別 |
| --- | --- | --- |
| 購物車型別 | Python `list` | 非清單 |
| 商品筆數 | 1～100 筆，含兩端 | 0 筆、超過 100 筆 |
| 每筆單價 | 10～500 元的整數，含兩端 | 非整數、低於 10、高於 500 |

有效購物車回傳所有單價的總和。函式依序驗證清單型別、筆數，再逐筆驗證單價，遇到第一個錯誤就拋出對應的 `ValueError`。單價使用 `type(price) is int` 的型別規則，因此浮點數與布林值都歸入非整數類別。

## 2. 待測程式與流程

函式本體有 16 行可執行敘述，包含 `if` 條件判斷及 `for` 迴圈。 [待測程式](https://github.com/alanlu01/software-normalize/blob/main/hw4/checkout.py)

```python
def checkout_total(prices: list[int]) -> int:
    if not isinstance(prices, list):
        raise ValueError("prices must be a list")
    if len(prices) < 1:
        raise ValueError("at least 1 item is required")
    if len(prices) > 100:
        raise ValueError("at most 100 items are allowed")
    total = 0
    for price in prices:
        if type(price) is not int:
            raise ValueError("price must be an integer")
        if price < 10:
            raise ValueError("price must be at least 10")
        if price > 500:
            raise ValueError("price must be at most 500")
        total += price
    return total
```

流程圖中的 T1～T8 對應下一節的測試案例。

```mermaid
flowchart TD
    START(["開始：輸入 prices"]) --> LIST{"prices 是清單？"}
    LIST -->|否| E1(["ValueError：非清單（T3）"])
    LIST -->|是| EMPTY{"筆數少於 1？"}
    EMPTY -->|是| E2(["ValueError：0 筆（T4）"])
    EMPTY -->|否| LIMIT{"筆數超過 100？"}
    LIMIT -->|是| E3(["ValueError：超過上限（T5）"])
    LIMIT -->|否| INIT["總額設為 0"]
    INIT --> NEXT{"還有下一筆商品？"}
    NEXT -->|否| RETURN(["回傳總額（T1、T2）"])
    NEXT -->|是| TYPE{"該筆單價是 int？"}
    TYPE -->|否| E4(["ValueError：非整數（T6）"])
    TYPE -->|是| LOW{"單價低於 10？"}
    LOW -->|是| E5(["ValueError：低於下限（T7）"])
    LOW -->|否| HIGH{"單價高於 500？"}
    HIGH -->|是| E6(["ValueError：高於上限（T8）"])
    HIGH -->|否| ADD["將單價加到總額"]
    ADD --> NEXT
```

## 3. 測試案例

| 案例 | Input values | Expected result | Test program’s result | Criteria analysis |
| --- | --- | --- | --- | --- |
| T1 | `[10]` | `10` | `10` | 有效最少筆數 1、有效最低單價 10。 |
| T2 | `[500] * 100` | `50000` | `50000` | 有效最多筆數 100、有效最高單價 500。 |
| T3 | `"10"` | `ValueError: prices must be a list` | `ValueError: prices must be a list` | 購物車型別錯誤。 |
| T4 | `[]` | `ValueError: at least 1 item is required` | `ValueError: at least 1 item is required` | 商品筆數低於下限。 |
| T5 | `[10] * 101` | `ValueError: at most 100 items are allowed` | `ValueError: at most 100 items are allowed` | 商品筆數高於上限，單價維持有效。 |
| T6 | `[10.5]` | `ValueError: price must be an integer` | `ValueError: price must be an integer` | 商品單價為浮點數。 |
| T7 | `[9]` | `ValueError: price must be at least 10` | `ValueError: price must be at least 10` | 單價低於下限，筆數與單價型別維持有效。 |
| T8 | `[501]` | `ValueError: price must be at most 500` | `ValueError: price must be at most 500` | 單價高於上限，筆數與單價型別維持有效。 |

## 4. 涵蓋率與最少案例數

- **有效極值至少需要 2 例。** 同一份清單無法同時有 1 筆和 100 筆。T1、T2 分別命中兩個筆數極值，並合併測到兩個單價極值。
- **六種無效類別至少需要 6 例。** 每次呼叫在第一個驗證錯誤就停止，只會出現一種錯誤結果。T3～T8 分別觸發六個錯誤出口。
- **最少共 8 例，涵蓋率為 10/10（100%）。** 兩個有效案例涵蓋四個有效極值，六個無效案例各涵蓋一種無效類別。

## 5. 工具驗證

使用 Python 3.14.5、pytest 與 pytest-cov。安裝專案的 `requirements.txt` 後，在專案根目錄執行下列指令。 [測試程式](https://github.com/alanlu01/software-normalize/blob/main/hw4/test_stress_coverage.py)

```sh
python -m pytest hw4 -v --cov-branch
```

實測 **8 例通過**，程式敘述涵蓋 17/17 行，分支出口涵蓋 14/14。測試同時比對無效案例的例外型別與訊息，確定各案例觸發指定的驗證條件。Stress Testing 的 10 個涵蓋目標由案例表逐項核對。
