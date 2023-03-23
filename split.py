import json, codecs

max = 500000

trimmed_data = []

# read json file
with open('alpaca_data_cleaned.json') as f:
    data = json.load(f)

    # Get total length
    # count = 0
    # for item in data:
    #     for component in item.values():
    #         count += len(component)

    # print(count)

    # Split into multiple files
    ind = 0
    count = 0
    for item in data:
        for key, value in item.items():
            count += len(value)

        if count < max:
            trimmed_data.append(item)
        else:
            json.dump(trimmed_data, codecs.open(f"dataset_splits/alpaca_data_cleaned_{ind}.json", 'w', encoding='utf-8'), sort_keys=True, indent=4)
            
            trimmed_data = []
            count = 0
            ind += 1