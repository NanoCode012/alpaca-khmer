import json, codecs

json_file = 'translated_dataset_splits/alpaca_data_cleaned_0.json'

# read json file
with open(json_file) as f:
    data = json.load(f)

    # Read each value
    for item in data:
        for val in item.values():
            print(val)

