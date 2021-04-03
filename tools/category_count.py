#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Prints and plots all class quantities.

TODO
* Add deviation of instances and images per category
"""

import copy
import json
import argparse

parser = argparse.ArgumentParser(description='User args')
parser.add_argument('annotations', help='Path to dataset annotations')

args = parser.parse_args()

# Load annotations
with open(args.annotations, 'r') as f:
    dataset = json.loads(f.read())

anns = dataset['annotations']
scene_anns = dataset['scene_annotations']
imgs = dataset['images']
nr_images = len(imgs)

categories = {}
super_categories = {}
for cat in dataset['categories']:
    categories[cat['id']] = {'name': cat['name'], 'supercategory': cat['supercategory'], 'images': [], 'instances': []}
    super_categories[cat['supercategory']] = {'name': cat['supercategory'], 'images': [], 'instances': []}

"""
1. Save data of categories
* add image to set of category images
* add instance to category

2. Save data of super categories
* add image to set of super category images
* add instance to super category
"""
for a in anns:
    a_id = a["id"]
    im_id = a["image_id"]
    c_id = a["category_id"]
    sup_cat = categories[c_id]['supercategory']
    # add to categories
    categories[c_id]['instances'].append(a_id)
    if im_id not in categories[c_id]['images']:
        categories[c_id]['images'].append(im_id)

    # add to super categories
    super_categories[sup_cat]['instances'].append(a_id)
    if im_id not in super_categories[sup_cat]['images']:
        super_categories[sup_cat]['images'].append(im_id)

def print_info(categories, super_categories):
    # print category info
    c_cop = copy.deepcopy(categories)
    s_cop = copy.deepcopy(super_categories)
    for k, v in c_cop.items():
        v['image_count'] = len(v['images'])
        v['instance_count'] = len(v['instances'])
        v.pop('images')
        v.pop('instances')
    for k, v in s_cop.items():
        v['image_count'] = len(v['images'])
        v['instance_count'] = len(v['instances'])
        v.pop('images')
        v.pop('instances')
    print(c_cop)
    print(s_cop)

print_info(categories, super_categories)

category_count = {v['name']: len(v['instances']) for k, v  in categories.items()}
category_im_count = {v['name']: len(v['images']) for k, v  in categories.items()}
super_category_count = {k: len(v['instances']) for k, v in super_categories.items()}
super_category_im_count = {k: len(v['images']) for k, v in super_categories.items()}
# sort discts
category_count_sorted = sorted(category_count.items(), key=lambda item: item[1], reverse=True)
super_category_count_sorted = sorted(super_category_count.items(), key=lambda item: item[1], reverse=True)

sup_len = len(super_category_count)
sup_total = 0
print("format: (instance count, category name, image count)")
print(f"Super Categories: ({sup_len})")
for i, (cat, count) in enumerate(super_category_count_sorted):
    print(f"\t {count}: \t {cat} ({super_category_im_count[cat]})")
    sup_total += count
    if i == sup_len//2:
        sup_median = count
print(f"Super category mean: {sup_total/sup_len}, median: {sup_median}")

cat_len = len(category_count)
cat_total = 0
print(f"Categories: ({cat_len})")
for i, (cat, count) in enumerate(category_count_sorted):
    print(f"\t {count}: \t {cat} ({category_im_count[cat]})")
    cat_total += count
    if i == cat_len//2:
        cat_median = count
print(f"Category mean: {cat_total/cat_len}, median: {cat_median}")

# plot
import matplotlib.pyplot as plt
plt.style.use("seaborn-darkgrid")

plt.bar(categories.keys(), [len(c['images']) for c in categories.values()], label="Image count per category")
plt.ylabel("Quantity")
plt.xlabel("Category ID")
plt.legend()
plt.savefig("image_count.jpg", dpi=200, bbox_inches='tight')
plt.show()

plt.bar(categories.keys(), [len(c['instances']) for c in categories.values()], label='Instance count per category')
plt.ylabel("Quantity")
plt.xlabel("Category ID")
plt.legend()
plt.savefig("instance_count.jpg", dpi=200, bbox_inches='tight')
plt.show()
