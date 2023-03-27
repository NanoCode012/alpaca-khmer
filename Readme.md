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
V3: ខ្ញុំសង្ឃឹមថាខ្ញុំអាចធ្វើអ្វីមួយដែលខ្ញុំអាចធ្វើដើម
V4: សូមស្វាគមន៍មកកាន់ហាងលក់គ្រឿងទេស!

Q: តើអាល់ប៉ាកាជាអ្វី?
V3: អាល់ប៉ាកគឺជាបន្លែដែលមានសុខភាពល្អ។
V4: អាល់ប៉ាកាគឺជាប្រភេទអាល់ប៉ាកដែលប្រើដើម្បីបង្កើតអគ្គិសនី។ វាត្រូវបានប្រើដើម្បីបង្កើតអគ្គិសនីដែលមានសុខភាពល្អ និងមានប្រសិទ្ធភាព។ វាត្រូវបានប្រើដើម្បីបង្កើតអគ្គិសនីដែលមានសុខភាពល្អ និងមានប្រសិទ្ធភាព។

Q: ផ្តល់គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាព
V3: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគឺ៖
    1. កំណត់គោលដៅ និងគោលដ��
V4: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគឺដើម្បីកាត់បន្ថយការប្រើប្រាស់ថាមពល កាត់បន្ថយការបំភាយឧស្ម័នផ្ទះកញ្ចក់ និងកាត់បន្ថយការបំភាយឧស្ម័នផ្ទះកញ្ចក់។

Q: តើធ្វើដូចម្តេចដើម្បីដុតនំខេក?
V3: ដើម្បីធ្វើដូចម្តេចដើម្បីដុតនំខេក អ្នកនឹងត្រូវការដុតនំដ
V4: ដើម្បីដុតនំខេក អ្នកនឹងត្រូវប្រមូលផ្តុំគ្រឿងផ្សំដូចខាងក្រោមៈ ម្សៅគ្រប់មុខ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុត

Q: ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019
V3: ស្តេចបារាំងនៅឆ្នាំ 2019 បានចាប់ផ្តើមជាមួយនឹងស្តេចបារាំងនៅឆ្នាំ 2
V4: ស្តេចបារាំងនៅឆ្នាំ 2019 បានចាប់ផ្តើមជាមួយនឹងការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ និងការប្រែប្រួលអាកាសធាតុ។ ការប្រែប្រួលអាកាសធាតុបានជះឥទ្ធិពលយ៉ាងខ្លាំងទៅលើការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ និងការប្រែប្រួលអាកាសធាតុ។ ការប្រែប្រ�

Q: តើ 2+2= ជាអ្វី?
V3: 2+2=4 ។
V4: 2+2=4

Q: ប្រាប់ខ្ញុំអំពីប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 ។
V3: ប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 គឺជាប្រធានាធិបតីម៉ិកស៊ិកដ៏
V4: ប្រធានាធិបតីម៉ិកស៊ិកនៅក្នុងឆ្នាំ 2019 គឺលោក Boris Johnson ។
```


### Discussion

### (27/Mar)

A model that has trained on twice the previous context length has finished. Furthermore, I fixed a bug where output has been limited to a low number.

First, the results do not contain as much leftover artifats. The artifacts are most likely due to being cutoff words. Second, it attempts to answer questions more now, however, it hallucinates. For example, it remembers the wrong person for the Mexican president in 2019. Thirdly, since the output limit has been lifted higher, it starts to repeat itself multiple times.

In a way, this revealed both the lack of HQ dataset and lack of quantity for model to understand the language.

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