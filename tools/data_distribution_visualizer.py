#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Uses matplotlib to visualize info about train, val, and test data.
"""

import matplotlib.pyplot as plt
import os.path
import json
import argparse

def images_per_category(annotations):
    """
    Iterates through all annotations and counts image occursences of all categories.
    Returns dict sorted on ascending amount of image occurences.
    """
    res = {}
    for a in annotations:
        img_id = a['image_id']
        cat_id = a['category_id']
        if cat_id not in res:
            res[cat_id] = []
        if img_id not in res[cat_id]:
            res[cat_id].append(img_id)
    res = {k: v for k, v in sorted(res.items(), key=lambda item: len(item[1]), reverse=True)}
    return res

def instances_per_category(annotations):
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

parser = argparse.ArgumentParser(description='User args')
parser.add_argument('train', help='Path to train annotations')
parser.add_argument('val', help='Path to validation annotations')
parser.add_argument('test',  help='Path to test annotations')

args = parser.parse_args()

with open(args.train, 'r') as f:
    train = json.load(f)
with open(args.val, 'r') as f:
    val = json.load(f)
with open(args.test, 'r') as f:
    test = json.load(f)

classes = {
    0: {'name': 'Aluminium foil', 'supercategory': 'Aluminium foil', 'image_count': 43, 'instance_count': 62}, 1: {'name': 'Battery', 'supercategory': 'Battery', 'image_count': 2, 'instance_count': 2}, 2: {'name': 'Aluminium blister pack', 'supercategory': 'Blister pack', 'image_count': 6, 'instance_count': 6}, 3: {'name': 'Carded blister pack', 'supercategory': 'Blister pack', 'image_count': 1, 'instance_count': 1}, 4: {'name': 'Other plastic bottle', 'supercategory': 'Bottle', 'image_count': 45, 'instance_count': 50}, 5: {'name': 'Clear plastic bottle', 'supercategory': 'Bottle', 'image_count': 225, 'instance_count': 285}, 6: {'name': 'Glass bottle', 'supercategory': 'Bottle', 'image_count': 74, 'instance_count': 104}, 7: {'name': 'Plastic bottle cap', 'supercategory': 'Bottle cap', 'image_count': 185, 'instance_count': 209}, 8: {'name': 'Metal bottle cap', 'supercategory': 'Bottle cap', 'image_count': 55, 'instance_count': 80}, 9: {'name': 'Broken glass', 'supercategory': 'Broken glass', 'image_count': 15, 'instance_count': 138}, 10: {'name': 'Food Can', 'supercategory': 'Can', 'image_count': 20, 'instance_count': 34}, 11: {'name': 'Aerosol', 'supercategory': 'Can', 'image_count': 10, 'instance_count': 10}, 12: {'name': 'Drink can', 'supercategory': 'Can', 'image_count': 151, 'instance_count': 229}, 13: {'name': 'Toilet tube', 'supercategory': 'Carton', 'image_count': 3, 'instance_count': 5}, 14: {'name': 'Other carton', 'supercategory': 'Carton', 'image_count': 79, 'instance_count': 93}, 15: {'name': 'Egg carton', 'supercategory': 'Carton', 'image_count': 9, 'instance_count': 11}, 16: {'name': 'Drink carton', 'supercategory': 'Carton', 'image_count': 41, 'instance_count': 45}, 17: {'name': 'Corrugated carton', 'supercategory': 'Carton', 'image_count': 41, 'instance_count': 64}, 18: {'name': 'Meal carton', 'supercategory': 'Carton', 'image_count': 27, 'instance_count': 30}, 19: {'name': 'Pizza box', 'supercategory': 'Carton', 'image_count': 3, 'instance_count': 3}, 20: {'name': 'Paper cup', 'supercategory': 'Cup', 'image_count': 62, 'instance_count': 67}, 21: {'name': 'Disposable plastic cup', 'supercategory': 'Cup', 'image_count': 91, 'instance_count': 104}, 22: {'name': 'Foam cup', 'supercategory': 'Cup', 'image_count': 11, 'instance_count': 13}, 23: {'name': 'Glass cup', 'supercategory': 'Cup', 'image_count': 4, 'instance_count': 6}, 24: {'name': 'Other plastic cup', 'supercategory': 'Cup', 'image_count': 2, 'instance_count': 2}, 25: {'name': 'Food waste', 'supercategory': 'Food waste', 'image_count': 7, 'instance_count': 8}, 26: {'name': 'Glass jar', 'supercategory': 'Glass jar', 'image_count': 4, 'instance_count': 6}, 27: {'name': 'Plastic lid', 'supercategory': 'Lid', 'image_count': 69, 'instance_count': 77}, 28: {'name': 'Metal lid', 'supercategory': 'Lid', 'image_count': 6, 'instance_count': 10}, 29: {'name': 'Other plastic', 'supercategory': 'Other plastic', 'image_count': 171, 'instance_count': 273}, 30: {'name': 'Magazine paper', 'supercategory': 'Paper', 'image_count': 5, 'instance_count': 12}, 31: {'name': 'Tissues', 'supercategory': 'Paper', 'image_count': 36, 'instance_count': 42}, 32: {'name': 'Wrapping paper', 'supercategory': 'Paper', 'image_count': 11, 'instance_count': 12}, 33: {'name': 'Normal paper', 'supercategory': 'Paper', 'image_count': 68, 'instance_count': 82}, 34: {'name': 'Paper bag', 'supercategory': 'Paper bag', 'image_count': 23, 'instance_count': 27}, 35: {'name': 'Plastified paper bag', 'supercategory': 'Paper bag', 'image_count': 0, 'instance_count': 0}, 36: {'name': 'Plastic film', 'supercategory': 'Plastic bag & wrapper', 'image_count': 310, 'instance_count': 451}, 37: {'name': 'Six pack rings', 'supercategory': 'Plastic bag & wrapper', 'image_count': 4, 'instance_count': 5}, 38: {'name': 'Garbage bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 20, 'instance_count': 31}, 39: {'name': 'Other plastic wrapper', 'supercategory': 'Plastic bag & wrapper', 'image_count': 184, 'instance_count': 260}, 40: {'name': 'Single-use carrier bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 49, 'instance_count': 61}, 41: {'name': 'Polypropylene bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 3, 'instance_count': 3}, 42: {'name': 'Crisp packet', 'supercategory': 'Plastic bag & wrapper', 'image_count': 35, 'instance_count': 39}, 43: {'name': 'Spread tub', 'supercategory': 'Plastic container', 'image_count': 9, 'instance_count': 9}, 44: {'name': 'Tupperware', 'supercategory': 'Plastic container', 'image_count': 4, 'instance_count': 4}, 45: {'name': 'Disposable food container', 'supercategory': 'Plastic container', 'image_count': 37, 'instance_count': 38}, 46: {'name': 'Foam food container', 'supercategory': 'Plastic container', 'image_count': 13, 'instance_count': 15}, 47: {'name': 'Other plastic container', 'supercategory': 'Plastic container', 'image_count': 6, 'instance_count': 6}, 48: {'name': 'Plastic glooves', 'supercategory': 'Plastic glooves', 'image_count': 4, 'instance_count': 4}, 49: {'name': 'Plastic utensils', 'supercategory': 'Plastic utensils', 'image_count': 29, 'instance_count': 37}, 50: {'name': 'Pop tab', 'supercategory': 'Pop tab', 'image_count': 71, 'instance_count': 99}, 51: {'name': 'Rope & strings', 'supercategory': 'Rope & strings', 'image_count': 28, 'instance_count': 29}, 52: {'name': 'Scrap metal', 'supercategory': 'Scrap metal', 'image_count': 12, 'instance_count': 20}, 53: {'name': 'Shoe', 'supercategory': 'Shoe', 'image_count': 6, 'instance_count': 7}, 54: {'name': 'Squeezable tube', 'supercategory': 'Squeezable tube', 'image_count': 6, 'instance_count': 7}, 55: {'name': 'Plastic straw', 'supercategory': 'Straw', 'image_count': 110, 'instance_count': 157}, 56: {'name': 'Paper straw', 'supercategory': 'Straw', 'image_count': 4, 'instance_count': 4}, 57: {'name': 'Styrofoam piece', 'supercategory': 'Styrofoam piece', 'image_count': 78, 'instance_count': 112}, 58: {'name': 'Unlabeled litter', 'supercategory': 'Unlabeled litter', 'image_count': 269, 'instance_count': 517}, 59: {'name': 'Cigarette', 'supercategory': 'Cigarette', 'image_count': 227, 'instance_count': 667}}

#cats = {x['id']: x for x in classes}
cat_ids = list(classes.keys())

train_imgs = images_per_category(train['annotations'])
train_inst = instances_per_category(train['annotations'])
val_imgs = images_per_category(val['annotations'])
val_inst = instances_per_category(val['annotations'])
test_imgs = images_per_category(test['annotations'])
test_inst = instances_per_category(test['annotations'])

def get_image_count(imgs):
    res = set()
    for v in imgs.values():
        res.update(v)
    return len(res)

print(f"Train count: {get_image_count(train_imgs)} images, {sum(train_inst.values())} annotations")
print(f"Val count: {get_image_count(val_imgs)} images, {sum(val_inst.values())} annotations")
print(f"Test count: {get_image_count(test_imgs)} images, {sum(test_inst.values())} annotations")

def print_missing(data, dataset_name):
    print(f"Missing from {dataset_name}:")
    for i, name in data:
        print("\t" + name)

train_missing = [(i, classes[i]["name"]) for i in classes if i not in train_imgs]
val_missing = [(i, classes[i]["name"]) for i in classes if i not in val_imgs]
test_missing = [(i, classes[i]["name"]) for i in classes if i not in test_imgs]
print_missing(train_missing, "train")
print_missing(val_missing, "val")
print_missing(test_missing, "test")


plt.style.use("seaborn-darkgrid")

plt.figure()
#plt.subplot(211)
plt.bar(cat_ids, [len(train_imgs.get(x, [])) for x in cat_ids], label='train: images per category', color="b")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("train_imgs.jpg", bbox_inches='tight')
#plt.show()

plt.figure()
plt.bar(cat_ids, [train_inst.get(x, 0) for x in cat_ids], label='train: instances per category', color="b")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("train_inst.jpg", bbox_inches='tight')
#plt.show()

plt.figure()
plt.bar(cat_ids, [len(val_imgs.get(x, [])) for x in cat_ids], label='val: images per category', color="r")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("val_imgs.jpg", bbox_inches='tight')
#plt.show()

plt.figure()
plt.bar(cat_ids, [val_inst.get(x, 0) for x in cat_ids], label='val: instances per category', color="r")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("val_inst.jpg", bbox_inches='tight')
#plt.show()

plt.figure()
plt.bar(cat_ids, [len(test_imgs.get(x, [])) for x in cat_ids], label='test: images per category', color="y")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("test_imgs.jpg", bbox_inches='tight')
#plt.show()

plt.figure()
plt.bar(cat_ids, [test_inst.get(x, 0) for x in cat_ids], label='test: instances per category', color="y")
plt.ylabel('Quantity')
plt.xlabel('Category ID')
plt.legend()
plt.savefig("test_inst.jpg", bbox_inches='tight')
#plt.show()


#plt.subplot(212)
