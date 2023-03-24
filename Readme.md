# Alpaca Khmer
---

An attempt to train a LORA on the alpaca LLM on a Khmer machine translated of `alpaca_data_cleaned.json`. 

Disclaimer: This is just an experimental project. It may turn out ok or really bad. 

## Required help :

- 👥 crowd translating dataset to Khmer. Progress: 1/35

There are approximately 18 million characters within the dataset. Due to costs, it would be quite expensive to translate it entirely on my own.

As of now, Google Cloud Translate API provides free 500k characters per month. It would be great if others can help translate a portion with their free credits and make a PR.

# Progress so far:

Trained a simple LORA on the first translated portion.

Here are some samples:

```
Q: សួស្តី
A: សួស្តី

--

Q: តើធ្វើដូចម្តេចដើម្បីដុតនំខេក?
A: ដូចម្តេចដើម្បីដុតនំខេក

-- 

(From train dataset)

Q: ផ្តល់គន្លឹះបីយ៉ាងដើម្បីរក្សាសុខភាព
A: ការបញ្ជាក់ដើម្បីរក្សាសុខភាព

--

Q: ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019
A: ប្រាប់ខ្ញុំអំពីស្តេចបារាំងនៅឆ្នាំ 2019

```

As of now, the results show that it's mainly rephrasing the question. However, the fact that it answers in Khmer is a really good sign since the base model was trained on Latin/Cryllic languages.

## Setup to translate
1. `python3 -m venv venv`
2. Activate env
3. `pip install google-cloud-translate tqdm`
4. Authenticate to Google Cloud
5. In `translate.py`, edit `file_to_translate` to the desired dataset split
    - Note: Make sure to not choose a split that has already been translated!
    - Only file0 has been translated!
6. Run `python translate.py`

## Credits
https://github.com/tatsu-lab/stanford_alpaca

https://github.com/tloen/alpaca-lora