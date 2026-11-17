# 作業六：Input Domain Characterization

組別：＿＿＿　組長：＿＿＿　組員：＿＿＿

對應老師題目第 5 項（5-1 Categorization、5-2 Combinatorial），日期標示為 11/20（碩士）、11/14（碩專）。因專案 HW5 已用於 Logical Expressions Coverage，本題新增為 HW6。
依據使用者提供的 Testing-Introduction.ppt p.65 摘錄設計；未取得原始投影片。

## 待測功能與規格

[course.py](course.py) 的 `summarize_course(level, major, students)` 接收課程等級、主修科系與學生編號清單，輸出課程代碼、學生人數、人數類別及原順序學生名單。課程代碼為大寫科系加等級，例如 `SWE-600`。零人回傳 `empty`，一人回傳 `single`，多人回傳 `multiple`。函式不修改輸入清單。
這是為本題建立的課程摘要示範功能；輸出規格由本作業定義。

## 輸入領域分類（System level）

| 輸入特性 | 類別 | 類別數 | 測試代表值 |
| --- | --- | ---: | --- |
| Level of course | 600、700、800 | 3 | 600、700、800 |
| Major | swe、cs、isa、infs | 4 | swe、cs、isa、infs |
| Number of students | 0、1、>1 | 3 | 0、1、3 |

學生清單分別為 `[]`、`["S001"]`、`["S001", "S002", "S003"]`。人數由實際清單長度決定，因此確實執行零筆、一筆、多筆資料處理。
各特性的類別互斥，並涵蓋本題有效輸入領域。假設三個特性可自由組合，沒有跨特性限制。未知科系、其他等級、錯誤型別等不在本題規格內，不宣稱已驗證無效輸入。多人類別使用 3 作代表，不代表測過所有大於 1 的整數。

## 5-1 Categorization：每個類別至少測一次

| 案例 | Level | Major | 人數 | 預期課程代碼 | 預期人數類別 | 實測 |
| --- | ---: | --- | ---: | --- | --- | --- |
| CAT01 | 600 | swe | 3 | SWE-600 | multiple | PASS |
| CAT02 | 700 | cs | 0 | CS-700 | empty | PASS |
| CAT03 | 800 | isa | 1 | ISA-800 | single | PASS |
| CAT04 | 600 | infs | 3 | INFS-600 | multiple | PASS |

等級涵蓋 3/3、科系涵蓋 4/4、人數涵蓋 3/3，合計 **10/10 個類別（100%）**。
至少需要 `max(3, 4, 3) = 4` 個案例，因為一次呼叫只能涵蓋一個科系，四個科系至少要四次。上表四例可達成所有類別，因此四例既足夠也是最少。
此集合只涵蓋 4/36 種完整組合，分類涵蓋 100% 不代表組合涵蓋 100%。

## 5-2 Combinatorial：全部類別組合都測過

完整組合數為 **3 × 4 × 3 = 36**，下表列出全部案例。每例也驗證回傳人數等於輸入清單長度、回傳名單與原清單相同且輸入未改動。

| 案例 | Level | Major | 人數 | 預期課程代碼 | 預期人數類別 | 實測 |
| --- | ---: | --- | ---: | --- | --- | --- |
| COM01 | 600 | swe | 0 | SWE-600 | empty | PASS |
| COM02 | 600 | swe | 1 | SWE-600 | single | PASS |
| COM03 | 600 | swe | 3 | SWE-600 | multiple | PASS |
| COM04 | 600 | cs | 0 | CS-600 | empty | PASS |
| COM05 | 600 | cs | 1 | CS-600 | single | PASS |
| COM06 | 600 | cs | 3 | CS-600 | multiple | PASS |
| COM07 | 600 | isa | 0 | ISA-600 | empty | PASS |
| COM08 | 600 | isa | 1 | ISA-600 | single | PASS |
| COM09 | 600 | isa | 3 | ISA-600 | multiple | PASS |
| COM10 | 600 | infs | 0 | INFS-600 | empty | PASS |
| COM11 | 600 | infs | 1 | INFS-600 | single | PASS |
| COM12 | 600 | infs | 3 | INFS-600 | multiple | PASS |
| COM13 | 700 | swe | 0 | SWE-700 | empty | PASS |
| COM14 | 700 | swe | 1 | SWE-700 | single | PASS |
| COM15 | 700 | swe | 3 | SWE-700 | multiple | PASS |
| COM16 | 700 | cs | 0 | CS-700 | empty | PASS |
| COM17 | 700 | cs | 1 | CS-700 | single | PASS |
| COM18 | 700 | cs | 3 | CS-700 | multiple | PASS |
| COM19 | 700 | isa | 0 | ISA-700 | empty | PASS |
| COM20 | 700 | isa | 1 | ISA-700 | single | PASS |
| COM21 | 700 | isa | 3 | ISA-700 | multiple | PASS |
| COM22 | 700 | infs | 0 | INFS-700 | empty | PASS |
| COM23 | 700 | infs | 1 | INFS-700 | single | PASS |
| COM24 | 700 | infs | 3 | INFS-700 | multiple | PASS |
| COM25 | 800 | swe | 0 | SWE-800 | empty | PASS |
| COM26 | 800 | swe | 1 | SWE-800 | single | PASS |
| COM27 | 800 | swe | 3 | SWE-800 | multiple | PASS |
| COM28 | 800 | cs | 0 | CS-800 | empty | PASS |
| COM29 | 800 | cs | 1 | CS-800 | single | PASS |
| COM30 | 800 | cs | 3 | CS-800 | multiple | PASS |
| COM31 | 800 | isa | 0 | ISA-800 | empty | PASS |
| COM32 | 800 | isa | 1 | ISA-800 | single | PASS |
| COM33 | 800 | isa | 3 | ISA-800 | multiple | PASS |
| COM34 | 800 | infs | 0 | INFS-800 | empty | PASS |
| COM35 | 800 | infs | 1 | INFS-800 | single | PASS |
| COM36 | 800 | infs | 3 | INFS-800 | multiple | PASS |

組合涵蓋率為 **36/36（100%）**。每次呼叫只涵蓋一種組合，因此全部組合至少需要 36 例。這裡指三個輸入特性的笛卡兒積，不是科系或等級的位置交換，也不是只測兩兩配對。

## 執行與實測結果

測試檔：[test_input_domain.py](test_input_domain.py)。在專案根目錄執行：

```sh
.venv/bin/python -m pytest hw6 -v --cov-branch
.venv/bin/python -m pytest hw6 -v -k categorization --cov-branch
.venv/bin/python -m pytest hw6 -v -k combinatorial --cov-branch
.venv/bin/python -m pytest -v --cov-branch
```

本次環境為 Python 3.9.6、pytest 8.4.2、pytest-cov 6.3.0、coverage.py 7.10.7。原專案 requirements.txt 的 pytest 9 不支援本機 Python 3.9，因此保留原設定並提供 [requirements-py39.txt](requirements-py39.txt) 供重現：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r hw6/requirements-py39.txt
```

HW6 共 41 項檢查通過：4 個分類案例、36 個組合案例、1 項測試集合完整性檢查。最後一項只檢查測試資料設計，不列入 4／36 個功能測試案例數。分類集合與組合集合有四組重複輸入，分開執行以展示兩種準則。
全專案共 **65 項通過**，79/79 行、44/44 個分支出口涵蓋率皆為 100%。HW6 為 12/12 行、6/6 個分支出口。程式碼涵蓋率是輔助結果；本題的分類與組合涵蓋率是根據上述輸入領域計算。

## 報告口頭說明

先把輸入依資料特性分成課程等級三類、科系四類、人數三類。Categorization 只要求每類出現過，因此四例就能全部涵蓋；Combinatorial 要求三個特性的每種組合都出現，因此需要三乘四乘三，共三十六例。測試除了執行程式，也比對課程代碼、人數、名單與人數分類的預期結果。
