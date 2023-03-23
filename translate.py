import json
import codecs
import six

from tqdm import tqdm
from google.cloud import translate_v2 as translate

# Change this!
file_to_translate = 'dataset_splits/alpaca_data_cleaned_0.json'

output_file = file_to_translate.replace('dataset_splits', 'translated_dataset_splits')

# Create translate client
translate_client = translate.Client()

with open(file_to_translate) as f:
    data = json.load(f)

    translated_arr = []

    for item in tqdm(data):
        translated_item = {}

        for key, value in item.items():
            # Check if value is not empty
            if (len(value) > 0):
                if isinstance(value, six.binary_type):
                    value = value.decode("utf-8")

                # Translate
                result = translate_client.translate(value, target_language='km', 
                                                    source_language='en', format_='text')
                translated_item[key] = result["translatedText"]
                # print(result)
            else:
                translated_item[key] = value

        translated_arr.append(translated_item)

    print('Saving to file')
    json.dump(translated_arr, codecs.open(output_file, 'w', encoding='utf-8'), sort_keys=True, indent=4)
    print('Saved!')
