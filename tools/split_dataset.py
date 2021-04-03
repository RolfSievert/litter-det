"""
Random data splitting is bad. Use stratified sampling, splits classes proportionally.
"""


import os.path
import json
import argparse
import numpy as np
import random
import datetime as dt
import copy
import numpy as np
from skmultilearn.model_selection import iterative_train_test_split
from skmultilearn.model_selection import IterativeStratification
#from skmultilearn.model_selection.iterative_stratification import iterative_train_test_split

parser = argparse.ArgumentParser(description='User args')
parser.add_argument('--dataset_dir', required=True, help='Path to dataset annotations')
parser.add_argument('--test_percentage', type=int, default=10, required=False, help='Percentage of images used for the testing set')
parser.add_argument('--val_percentage', type=int, default=10, required=False, help='Percentage of images used for the validation set')

args = parser.parse_args()

ann_input_path = args.dataset_dir + '/' + 'annotations.json'

# Load annotations
with open(ann_input_path, 'r') as f:
    dataset = json.loads(f.read())

anns = dataset['annotations']
scene_anns = dataset['scene_annotations']
imgs = dataset['images']
cats = dataset['categories']
nr_images = len(imgs)
print(f"Number of images: {nr_images}")

# Find all annotations below a specified quantity and mark them as unlabeled trash
ann_threshold = 3

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

def unlabel_annotations_by_threshold(annotations, threshold):
    """
    Marks all categories below image count @threshold as 'unlabeled_litter'
    """
    # id of unlabeled litter
    unlabeled_id = 58
    category_count = category_counter(annotations)

    category_removes = [k for k, v in category_count.items() if v < threshold]
    for cat in category_removes:
        print(f"Unlabeling id: {cat}, \tcount: {category_count[cat]}, \tname: {cats[cat]['name']}")
    for a in annotations:
        if a['category_id'] in category_removes:
            a['category_id'] = unlabeled_id

    return annotations

def get_image_instance_quantities(annotations):
    """
    Return dict containing how many images that contain 1 instance, 2 instances, etc.
    """
    per_image_count = {}
    for a in annotations:
        if a['image_id'] not in per_image_count:
            per_image_count[a['image_id']] = 0
        per_image_count[a['image_id']] += 1

    res = {}
    for k, v in per_image_count.items():
        if v not in res:
            res[v] = 0
        res[v] += 1
    res = {k: v for k, v in sorted(res.items(), key=lambda item: item[0], reverse=True)}
    return res

def category_instances(annotations):
    """
    Build a list of pairs (categories, and all images containing that category).
    """
    res = {}
    for a in annotations:
        if not a['id'] in res:
            res[a['id']] = []
        if a['image_id'] not in res[a['id']]:
            res[a['id']].append(a['image_id'])
    # sort on number of images containing category
    res = [(k, v) for k,v in sorted(res.items(), key=lambda item: len(item[1]), reverse=True)]
    return res

def get_train_val_test(image_ids, image_categories, train_size=0.8, val_size=0.1, test_size=0.1):
    """
    Uses IterativeStratification from scikit multilabel learn package to split data into train, validation, and test sets.
    """
    X = np.array(image_ids)
    y = np.array(image_categories)

    stratifier1 = IterativeStratification(n_splits=2, order=2, sample_distribution_per_fold=[val_size+test_size, 1.0-(test_size+val_size)])
    stratifier2 = IterativeStratification(n_splits=2, order=2, sample_distribution_per_fold=[val_size/(val_size+test_size), test_size/(val_size+test_size)])
    # get train data
    train_indexes, val_test_indexes = next(stratifier1.split(X, y))
    train = [X[x] for x in train_indexes]

    # get val and test data
    X = X[val_test_indexes]
    y = y[val_test_indexes, :]
    val_indexes, test_indexes = next(stratifier2.split(X, y))
    val = [X[x] for x in val_indexes]
    test = [X[x] for x in test_indexes]

    def intersects(lst1, lst2):
        return len(list(set(lst1) & set(lst2))) != 0

    # assert non-overlap of datasets
    assert intersects(train, val) == False
    assert intersects(train, test) == False
    assert intersects(test, val) == False

    return train, val, test

def get_image_histograms(annotations, n_categories):
    """
    Build a histogram of categories for each image.
    """
    image_hist = {}
    for a in annotations:
        image_id = a['image_id']
        a_cat = a['category_id']
        # create histogram if non-existent
        if image_id not in image_hist:
            image_hist[image_id] = [0 for _ in range(n_categories)]
        image_hist[image_id][a_cat] += 1
    return image_hist

def images_per_category(annotations):
    res = {}
    for a in annotations:
        img_id = a['image_id']
        cat_id = a['category_id']
        if cat_id not in res:
            res[cat_id] = []
        if img_id not in res[cat_id]:
            res[cat_id].append(img_id)
    res = {k: v for k, v in sorted(res.items(), key=lambda item: len(item[1]), reverse=True)}
    for cat, imgs in res.items():
        print(cat, len(imgs))



anns = unlabel_annotations_by_threshold(anns, ann_threshold)

quant = get_image_instance_quantities(anns)
# print("Images with number of instances:")
inst_count = 0
for k, v in quant.items():
    print(f"\t{k}: {v}")
    inst_count += k*v
print("Average no instances per image:", inst_count/nr_images)
print("Number of instances:", inst_count)

images_per_category(anns)

for k, v in category_counter(anns).items():
    print(k, "-", v)

# get label histograms of images
image_hists = get_image_histograms(anns, len(cats))
# randomize order
image_hists = list(image_hists.items())
random.shuffle(image_hists)
image_ids = [item[0] for item in image_hists]
image_cats = [item[1] for item in image_hists]

# create annotation templates
dataset_base = {
    'info': None,
    'images': [],
    'annotations': [],
    'scene_annotations': [],
    'licenses': [],
    'categories': [],
    'scene_categories': [],
}
dataset_base['info'] =  dataset['info']
dataset_base['categories'] = dataset['categories']
dataset_base['scene_categories'] = dataset['scene_categories']

train_set = copy.deepcopy(dataset_base)
val_set = copy.deepcopy(dataset_base)
test_set = copy.deepcopy(dataset_base)

# iterative stratifier split
train_imgs, val_imgs, test_imgs = get_train_val_test(image_ids, image_cats)
print("train, val, test size:", len(train_imgs), len(val_imgs), len(test_imgs))

# add images to datasets
for i in imgs:
    if i['id'] in train_imgs:
        train_set['images'].append(i)
    elif i['id'] in val_imgs:
        val_set['images'].append(i)
    elif i['id'] in test_imgs:
        test_set['images'].append(i)

def get_annotations_from_images(annotations, images):
    res = []
    for a in annotations:
        if a['image_id'] in images:
            res.append(a)
    return res

train_set['annotations'] = get_annotations_from_images(anns, train_imgs)
val_set['annotations'] = get_annotations_from_images(anns, val_imgs)
test_set['annotations'] = get_annotations_from_images(anns, test_imgs)


# Write dataset splits
ann_train_out_path = args.dataset_dir + '/' + 'annotations' +'_train.json'
ann_val_out_path   = args.dataset_dir + '/' + 'annotations' + '_val.json'
ann_test_out_path  = args.dataset_dir + '/' + 'annotations'  + '_test.json'

with open(ann_train_out_path, 'w') as f:
    json.dump(train_set, f)

with open(ann_val_out_path, 'w+') as f:
    json.dump(val_set, f)

with open(ann_test_out_path, 'w+') as f:
    json.dump(test_set, f)

exit()





test_count = category_counter(test_set['annotations'])
val_count = category_counter(val_set['annotations'])
train_count = category_counter(train_set['annotations'])

category_count = category_counter(anns)
category_count = {k: v for k, v in sorted(category_count.items(), key=lambda item: item[1], reverse=True)}
for cat in category_count:
    test_c = test_count[cat] if cat in test_count else 0
    val_c = val_count[cat] if cat in val_count else 0
    train_c = train_count[cat] if cat in train_count else 0
    print(f"ID: {cat} - ({train_c}, {val_c}, {test_c})")



