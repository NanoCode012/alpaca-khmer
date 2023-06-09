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
V5:  សួស្តី​ពិពណ៌នា​អំពី​ការ​ប្រើ​ប្រាស់​បញ្ញាសិប្បនិម្មិត​ដើម្បី​ធ្វើ​ឱ្យ​វា​ត្រូវ​បាន​ប្រើ​ដើម្បី​ធ្វើ​ឱ្យ​វា​ត្រូវ​បាន​ប្រើ​ដើម្បី​ធ្វើ​ឱ្យ​វា​ត្រូវ​បាន​ប្រើ​ដើម្បី​ធ្វើ​ឱ្យ​វា​ត្រូវ​បាន​ប្រើ​​ (repeat many times)

Q: តើអាល់ប៉ាកាជាអ្វី?
V3: អាល់ប៉ាកគឺជាបន្លែដែលមានសុខភាពល្អ។
V4: អាល់ប៉ាកាគឺជាប្រភេទអាល់ប៉ាកដែលប្រើដើម្បីបង្កើតអគ្គិសនី។ វាត្រូវបានប្រើដើម្បីបង្កើតអគ្គិសនីដែលមានសុខភាពល្អ និងមានប្រសិទ្ធភាព។ វាត្រូវបានប្រើដើម្បីបង្កើតអគ្គិសនីដែលមានសុខភាពល្អ និងមានប្រសិទ្ធភាព។
V5: អាល់ប៉ាកាត្រូវបានបង្កើតឡើងដើម្បីធ្វើឱ្យវាត្រឹមត្រូវតាមវេយ្យាករណ៍។ អាល់ប៉ាកាត្រូវបានបង្កើតឡើងដើម្បីធ្វើឱ្យវាត្រឹមត្រូវតាមវេយ្យាករណ៍។ (repeat more times)

Q: ផ្តល់គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាព
V3: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគឺ៖
    1. កំណត់គោលដៅ និងគោលដ��
V4: គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាពគឺដើម្បីកាត់បន្ថយការប្រើប្រាស់ថាមពល កាត់បន្ថយការបំភាយឧស្ម័នផ្ទះកញ្ចក់ និងកាត់បន្ថយការបំភាយឧស្ម័នផ្ទះកញ្ចក់។
V5: 1. បង្កើតសុខភាពដ៏អស្ចារ្យដែលមានសុខភាពល្អ។
2. បង្កើតសុខភាពដ៏អស្ចារ្យដែលមានសុខភាពល្អ។
3. បង្កើតសុខភាពដ៏អស្ចារ្យដែលមានសុខភាពល្អ។

Q: តើធ្វើដូចម្តេចដើម្បីដុតនំខេក?
V3: ដើម្បីធ្វើដូចម្តេចដើម្បីដុតនំខេក អ្នកនឹងត្រូវការដុតនំដ
V4: ដើម្បីដុតនំខេក អ្នកនឹងត្រូវប្រមូលផ្តុំគ្រឿងផ្សំដូចខាងក្រោមៈ ម្សៅគ្រប់មុខ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ ម្សៅដុតនំ (repeat more times)
V5: ធ្វើដូចម្តេចដើម្បីដុតនំខេកគឺដើម្បីបង្កើតបញ្ជីដែលបានផ្តល់ឱ្យដោយផ្អែកលើបញ្ជីដែលបានផ្តល់ឱ្យ (repeat more times)

Q: ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019
V3: ស្តេចបារាំងនៅឆ្នាំ 2019 បានចាប់ផ្តើមជាមួយនឹងស្តេចបារាំងនៅឆ្នាំ 2
V4: ស្តេចបារាំងនៅឆ្នាំ 2019 បានចាប់ផ្តើមជាមួយនឹងការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ និងការប្រែប្រួលអាកាសធាតុ។ ការប្រែប្រួលអាកាសធាតុបានជះឥទ្ធិពលយ៉ាងខ្លាំងទៅលើការប្រែប្រួលអាកាសធាតុ ការប្រែប្រួលអាកាសធាតុ និងការប្រែប្រួលអាកាសធាតុ។ ការប្រែប្រ�
V5: ស្តេចបារាំងនៅឆ្នាំ 2019 គឺជាស្តេចបារាំងដ៏ល្អឥតខ្ចោះនៅឆ្នាំ 2019 ដែលមានសុខភាពល្អឥតខ្ចោះ។

Q: តើ 2+2= ជាអ្វី?
V3: 2+2=4 ។
V4: 2+2=4
V5: 2+2=4

Q: ប្រាប់ខ្ញុំអំពីប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 ។
V3: ប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 គឺជាប្រធានាធិបតីម៉ិកស៊ិកដ៏
V4: ប្រធានាធិបតីម៉ិកស៊ិកនៅក្នុងឆ្នាំ 2019 គឺលោក Boris Johnson ។
V5: ប្រធានាធិបតីម៉ិកស៊ិកក្នុងឆ្នាំ 2019 គឺជាប្រធានាធិបតីម៉ិកដ៏ល្អបំផុតដែលមានប្រធានាធិបតីម៉ិកដែលមានប្រធានាធិបតីម៉ិកដែលមានប្រធានាធិបតីម៉ិកដែលមានប្រធានាធិបតីម៉ិក (repeat many times)
```


### Discussion

#### (29/Mar)

From discussions in Discord with Sliden, it would be interesting to translate the prompt as well or to make it understand to answer in Khmer. Furthermore, it should be necessary to purge code from the dataset as it should not have been translated. 

Lastly, attempts should be made soon to translate the new update cleaned dataset. Perhaps, using diff to find the difference and only translating those rows. Maybe using a database to store this will be useful.

#### (28/Mar) - V5

Following discussions from days prior and studying the token lengths of the dataset, I found that the data is longer than the EN. I have now finished training a model with a much longer cut off length. 

The results are quite horrible. It repeats itself numerous times to reach output limit. Currently, some ideas would be to try with a shorter cut off length, or to limit the output.

#### (27/Mar) - V4

A model that has trained on twice the previous context length has finished. Furthermore, I fixed a bug where output has been limited to a low number.

First, the results do not contain as much leftover artifats. The artifacts are most likely due to being cutoff words. Second, it attempts to answer questions more now, however, it hallucinates. For example, it remembers the wrong person for the Mexican president in 2019. Thirdly, since the output limit has been lifted higher, it starts to repeat itself multiple times.

In a way, this revealed both the lack of HQ dataset and lack of quantity for model to understand the language.

#### (26/Mar) - V3

Another model has finished training for 10 epochs. We can observe that it is closer in answering questions than before. One thing of concern was how the text kept getting cut off mid response.

After this, I quickly tested and found that a lot of data were being cut off due to the context length being much longer than in English, most likely due to unicode encoding, causing a lot of data to be skipped.

#### (25/Mar) - V2

The model V2 has been improved significantly since V1. It has been trained over the full dataset.

Unlike before, the model does not repeat the question back, but starts to spit out random text.

## Credits
https://github.com/tatsu-lab/stanford_alpaca

https://github.com/tloen/alpaca-lora

https://github.com/huggingface/peft