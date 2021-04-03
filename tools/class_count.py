"""
Prints class count of annotation file.
"""

import json
import argparse

parser = argparse.ArgumentParser(description='User args')
parser.add_argument('--annotations', required=True, help='Path to dataset annotations')
# taco class count is 60
parser.add_argument('--class_count', default=60, help='Class count of annotations')

args = parser.parse_args()

# Load annotations
with open(args.annotations, 'r') as f:
    dataset = json.loads(f.read())

anns = dataset['annotations']

def category_counter(annotations):
    """
    Counts categories within annotations, and returns a dict of category_id: category_count
    """
    category_count= {}

    for a in annotations:
        c_id = a["category_id"]
        if c_id not in category_count:
            category_count[c_id] = 0
        category_count[c_id]+=1
    return category_count

cat_count = category_counter(anns)

print(f"Category count: {len(cat_count)}")

for id in range(args.class_count):
    if id in cat_count:
        print(cat_count[id], end=', ')
    else:
        print('0', end=', ')
print()
