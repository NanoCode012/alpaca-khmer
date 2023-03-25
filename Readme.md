# Alpaca Khmer

An attempt to train an alpaca LORA on a Khmer machine translated of `alpaca_data_cleaned.json`. 

Disclaimer: This is just an experimental project. It may turn out ok or really bad.

---

Thank you to [SpeakTe](https://www.speakte.com) for sponsoring the translation!

<img src="img/speakte-banner.png" width="100" height="50" alt-text="speakte-banner"/>

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


### Discussion

The model has been improved significantly since V1. It has been trained over the full dataset.

Unlike before, the model does not repeat the question back, but starts to spit out random text.

## History

- (25/Mar) V2: Trained on full dataset. 3 epochs.

- (23/Mar) V1: Trained on single portion of dataset. 3 epochs.

## Credits
https://github.com/tatsu-lab/stanford_alpaca

https://github.com/tloen/alpaca-lora

https://github.com/huggingface/peft