"""
Random data splitting is bad. Use stratified sampling, splits classes proportionally.
"""


import os.path
import json
import argparse
import random
import copy

parser = argparse.ArgumentParser(description='User args')
parser.add_argument('--anns', type=str, help='Path to annotation file')

args = parser.parse_args()

# Load annotations
with open(args.anns, 'r') as f:
    dataset = json.load(f)

# select what images to use
demo_imgs = ["batch_15/000010.jpg", "batch_15/000020.jpg", "batch_9/000052.jpg", "batch_13/000038.jpg", "batch_13/000060.jpg", "batch_11/000076.jpg"]

new_anns = []
img_ids = []
images = []

# find images
for i in dataset["images"]:
    if i["file_name"] in demo_imgs:
        img_ids.append(i["id"])
        images.append(i)

# find annotations using images
for a in dataset["annotations"]:
    if a["image_id"] in img_ids:
        new_anns.append(a)

dataset["annotations"] = new_anns
dataset["images"] = images

not_found = set(demo_imgs) - set([i["file_name"] for i in images])
if len(not_found):
    print(f"{not_found} was not found")

with open("demo_anns.json", 'w') as f:
    json.dump(dataset, f)

exit()
