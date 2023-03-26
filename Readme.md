# Alpaca Khmer

An attempt to train an alpaca LORA on a Khmer machine translated of `alpaca_data_cleaned.json`. 

Disclaimer: This is just an experimental project. It may turn out ok or really bad.

---

Thank you to [SpeakTe](https://www.speakte.com) for sponsoring the translation!

<img src="img/speakte-banner.png" width="100" height="50" alt-text="speakte-banner"/>

## Results now:

Here are some samples. Q is the question. V(X) is the response from the model where X is version number.

```
Q: សួស្តី
V2: ខ្ញុំបានសួស្តីពីអ្វីដែលត្រូវបានប្រើដើម្បីបង្កើនប្រសិទ្ធភា
V3: ខ្ញុំសង្ឃឹមថាខ្ញុំអាចធ្វើអ្វីមួយដែលខ្ញុំអាចធ្វើដើម

Q: តើអាល់ប៉ាកាជាអ្វី?
V2: អាល់ប៉ាកាជាអ្វីអាចត្រូវបានប្រើដើម្បីកាត់បន្ថយភាពតានតឹង និ��
V3: អាល់ប៉ាកគឺជាបន្លែដែលមានសុខភាពល្អ។

Q: ផ្តល់គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាព
V2: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគួរតែត្រូវបានប្រើដើម្បីកាត់�
V3: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគឺ៖
    1. កំណត់គោលដៅ និងគោលដ��

Q: តើធ្វើដូចម្តេចដើម្បីដុតនំខេក?
V2: ធ្វើដូចម្តេចដើម្បីដុតនំខេកគឺដើម្បីបង្កើតប្រយោគដែល
V3: ដើម្បីធ្វើដូចម្តេចដើម្បីដុតនំខេក អ្នកនឹងត្រូវការដុតនំដ

Q: ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019
V2: ស្តេចបារាំងនៅឆ្នាំ 2019 គឺជាស្តេចបារាំងដ៏ល្អបំផុតនៅឆ្នាំ 2019 ដ��
V3: ស្តេចបារាំងនៅឆ្នាំ 2019 បានចាប់ផ្តើមជាមួយនឹងស្តេចបារាំងនៅឆ្នាំ 2

Q: តើ 2+2= ជាអ្វី?
V2: "អ្វី គឺជាអ្វីដែលត្រូវបានប្រើដើម្បីពិពណ៌នាអំពីអ្វីដែ��"
V3: 2+2=4 ។

Q: ប្រាប់ខ្ញុំអំពីប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 ។
V2: ប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 គឺជាប្រធានាធិបតីម៉ិកស៊ិកដ��
V3: ប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 គឺជាប្រធានាធិបតីម៉ិកស៊ិកដ៏
```


### Discussion

#### (26/Mar)

Another model has finished training for 10 epochs. We can observe that it is closer in answering questions than before. One thing of concern was how the text kept getting cut off mid response.

After this, I quickly tested and found that a lot of data were being cut off due to the context length being much longer than in English, most likely due to unicode encoding, causing a lot of data to be skipped.

#### (25/Mar)

The model V2 has been improved significantly since V1. It has been trained over the full dataset.

Unlike before, the model does not repeat the question back, but starts to spit out random text.

## History

- (26/Mar) V3: Full dataset. 10 epochs.

- (25/Mar) V2: Trained on full dataset. 3 epochs.

- (23/Mar) V1: Trained on single portion of dataset. 3 epochs.

## Credits
https://github.com/tatsu-lab/stanford_alpaca

https://github.com/tloen/alpaca-lora

https://github.com/huggingface/peft