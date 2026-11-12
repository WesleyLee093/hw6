# 作業四：Stress Testing Coverage

組別／組員：（請填寫）

[繳交用報告與流程圖](REPORT.md)

[待測程式](checkout.py)加總購物車的商品單價。它用條件判斷檢查清單和價格，再用迴圈逐筆處理，函式本體有 16 行可執行敘述。[測試程式](test_stress_coverage.py)

## 有效範圍

| 資料 | 有效範圍 | 無效類別 |
| --- | --- | --- |
| 購物車 | Python `list` | 非清單 |
| 商品筆數 | 1～100 筆，含兩端 | 0 筆、超過 100 筆 |
| 每筆單價 | `int` 10～500 元，含兩端 | 非整數、低於 10、高於 500。布林值屬於非整數類別。 |

## 測試案例

| 案例 | Input values | Expected result | Test program’s result | Criteria analysis |
| --- | --- | --- | --- | --- |
| T1 | `[10]` | `10` | `10` | 有效最少筆數 1、有效最低單價 10。 |
| T2 | `[500] * 100` | `50000` | `50000` | 有效最多筆數 100、有效最高單價 500。 |
| T3 | `"10"` | `ValueError: prices must be a list` | `ValueError: prices must be a list` | 購物車型別無效。 |
| T4 | `[]` | `ValueError: at least 1 item is required` | `ValueError: at least 1 item is required` | 筆數低於下限。 |
| T5 | `[10] * 101` | `ValueError: at most 100 items are allowed` | `ValueError: at most 100 items are allowed` | 筆數高於上限。 |
| T6 | `[10.5]` | `ValueError: price must be an integer` | `ValueError: price must be an integer` | 單價型別無效。 |
| T7 | `[9]` | `ValueError: price must be at least 10` | `ValueError: price must be at least 10` | 單價低於下限。 |
| T8 | `[501]` | `ValueError: price must be at most 500` | `ValueError: price must be at most 500` | 單價高於上限。 |

## 最少案例與實測結果

至少需要 2 次有效呼叫，因為同一份購物車不能同時有 1 筆與 100 筆。T1、T2 同時覆蓋兩個單價極值。六種無效類別各觸發一個不同的錯誤，函式在第一個錯誤就停止，因此至少另需 6 次呼叫。**最少 8 例，涵蓋 10/10 個測試目標（100%）**。

```sh
python -m pytest hw4 -v --cov-branch
```

實測 **8 例通過**。測試同時比對例外型別和訊息，以確認觸發的是預定的驗證條件。
