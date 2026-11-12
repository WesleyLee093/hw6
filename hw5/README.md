# 作業五：Logical Expressions Coverage

組別／組員：（請填寫）

[繳交用報告與流程圖](REPORT.md)

[待測程式](discount.py)以迴圈累加商品金額。會員且小計至少 1,000 元時享九折，折扣金額無條件捨去至整數，最後加 60 元運費。函式本體有 12 行可執行敘述。[測試程式](test_logical_coverage.py)

第 10 行的判斷式有兩個獨立子條件。A 是是否為會員（`is_member`），B 是小計是否至少 1,000 元（`meets_threshold`）。A 和 B 都是布林值，使用 `A & B` 做布林 AND，每次判斷都會評估兩個運算元。

## 測試案例

| 案例 | Input values（單價清單、會員） | Expected result（應付） | Test program’s result（應付） | Criteria analysis（A、B、整體結果） |
| --- | --- | ---: | ---: | --- |
| T1 | `[400, 500], False` | 960 | 960 | F、F、F |
| T2 | `[500, 700], False` | 1260 | 1260 | F、T、F |
| T3 | `[400, 500], True` | 960 | 960 | T、F、F |
| T4 | `[500, 700], True` | 1140 | 1140 | T、T、T |

## 最少案例與實測結果

| 測試目標 | 最少案例 | 涵蓋率 | 最少案例數的依據 |
| --- | --- | --- | --- |
| Predicate | T1、T4，共 2 例 | 2/2（100%） | 一次判斷只產生一個結果，至少要一次 F 和一次 T。 |
| Clause | T1、T4，共 2 例 | 4/4（100%） | 每個子條件都需要 F 和 T，T1 與 T4 剛好涵蓋兩個子條件的兩種值。 |
| Combinatorial | T1～T4，共 4 例 | 4/4（100%） | 兩個獨立布林子條件共有四種組合，一次呼叫只能命中其中一種。 |

```sh
python -m pytest hw5 -v --cov-branch
python -m pytest hw5 -v -k "T1 or T4"
```

完整執行 **4 例通過**。第二條指令可單獨驗證 Predicate 和 Clause 的共用最小集合。涵蓋率依表中的子條件與整體結果計算。
