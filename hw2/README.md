# 作業二：Line Coverage

組別／組員：（請填寫）

[待測程式](triangle.py)接收三個整數邊長。它用迴圈檢查每條邊是否為正數，並收集不同的邊長。接著檢查三角不等式，再依相異邊長數分類。函式本體有 15 行可執行敘述，含 `for` 和 `if`。[測試程式](test_line_coverage.py)

## 測試案例

第 1 行的函式定義在匯入模組時執行。表中列的是呼叫函式後走到的行號。

| 案例 | Input values `(a, b, c)` | Expected result | Test program’s result | Criteria analysis |
| --- | --- | --- | --- | --- |
| T1 | `(1, 0, 2)` | `invalid` | `invalid` | 第 2–7 行。第二條邊為零，在第 6 行返回。 |
| T2 | `(1, 1, 3)` | `invalid` | `invalid` | 第 2–5、7–10 行。兩短邊之和不足，在第 10 行返回。 |
| T3 | `(2, 2, 2)` | `equilateral` | `equilateral` | 第 2–5、7–9、11–13 行。只有一種邊長。 |
| T4 | `(2, 2, 3)` | `isosceles` | `isosceles` | 第 2–5、7–9、11、12、14、15 行。有兩種邊長。 |
| T5 | `(3, 4, 5)` | `scalene` | `scalene` | 第 2–5、7–9、11、12、14、16 行。三條邊長都不同。 |

## 最少案例與實測結果

第 6、10、13、15、16 行各有一個 `return`。一次呼叫最多執行其中一行，至少要 5 個案例。T1～T5 各命中一個 `return`，合計涵蓋第 1–16 行。實測 **5 例通過，Line Coverage 16/16（100%）**。

```sh
python -m pytest hw2 -v
```

可加上 `-k T1` 只跑一例，從 `Missing` 欄核對該例走到的行。單例低於專案的 100% 門檻時，pytest 會回報涵蓋率未達標。
