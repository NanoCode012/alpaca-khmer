# Alpaca Khmer

An attempt to train an alpaca LORA on a Khmer machine translated of `alpaca_data_cleaned.json`. 

Disclaimer: This is just an experimental project. It may turn out ok or really bad.

---

## Results now:

Here are some samples trained on translated dataset:

```
Q: "សួស្តី"
A: "ខ្ញុំបានសួស្តីពីអ្វីដែលត្រូវបានប្រើដើម្បីបង្កើនប្រសិទ្ធភា"


Q: "តើអាល់ប៉ាកាជាអ្វី?"
A: "អាល់ប៉ាកាជាអ្វីអាចត្រូវបានប្រើដើម្បីកាត់បន្ថយភាពតានតឹង និ��"


Q: "ផ្តល់គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាព"
A: "គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគួរតែត្រូវបានប្រើដើម្បីកាត់�"


Q: "តើធ្វើដូចម្តេចដើម្បីដុតនំខេក?"
A: "ធ្វើដូចម្តេចដើម្បីដុតនំខេកគឺដើម្បីបង្កើតប្រយោគដែល"


Q: "ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019"
A: "ស្តេចបារាំងនៅឆ្នាំ 2019 គឺជាស្តេចបារាំងដ៏ល្អបំផុតនៅឆ្នាំ 2019 ដ��"
```

There seems to be problems with the model. Unlike before, it does not repeat the question, but starts to spit out random text.

## Credits
https://github.com/tatsu-lab/stanford_alpaca

https://github.com/tloen/alpaca-lora