'''
python sub_set <sub_set_size>
'''

import sys
from lib import json_io


if len(sys.argv) < 1:
    sys.exit(1)

data = json_io.read_json('hyper_drug_repeat.json')
new_data = {}
count = 0
for key, values in data.iteritems():
    new_data[key] = values
    count += 1
    if count >= int(sys.argv[1]):
        break

json_io.write_json('hyper_drug_repeat_subset.json', new_data)
        
