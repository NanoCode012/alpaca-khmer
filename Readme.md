# Alpaca Khmer
---

An attempt to train the alpaca LLM on a Khmer machine translated of `alpaca_data_cleaned.json`. 

Disclaimer: This is just an experimental project. It may turn out ok or really bad. 

## Required help :

- 👥 crowd translating dataset to Khmer. Progress: 1/35

There are approximately 18 million characters within the dataset. Due to costs, it would be quite expensive to translate it entirely on my own.

As of now, Google Cloud Translate API provides free 500k characters per month. It would be great if others can help translate a portion with their free credits and make a PR.

## Setup to translate
1. `python3 -m venv venv`
2. Activate env
3. `pip install google-cloud-translate tqdm`
4. Authenticate to Google Cloud
5. Edit `translate.py` to the desired dataset split
    - Note: Make sure to not choose a split that has already been translated!
6. Run `python translate.py`

## Credits
https://github.com/tatsu-lab/stanford_alpaca
https://github.com/tloen/alpaca-lora