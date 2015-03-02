hyper-drug-repeat
=======
## Usage

### step 1 
get hyper drug data from database (`get_hyper_data.sql`)
### step 2 
get hyper repeat drug data (`get_repeat_drug.py`)
### step 3 (optional) 
get subset data (`get_subset.py`)

## Output Format
```js
{
  "使用者ID": [
        [
          "使用者ID",
          "藥品名稱",
          "案件分類",
          "葯品使用頻率(支付成 數)",
          "葯品用量(診療部位)",
          "就醫日期 ",
          "調劑日期"
          "高血壓用藥類別"
        ],
        [
          ...
          ...
        ]
        ,.....
      ],
  "使用者ID":[   
}
```
