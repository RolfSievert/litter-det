#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 znap <znap@asusmanjaro>
#
# Distributed under terms of the MIT license.

"""

"""

import argparse
import json

parser = argparse.ArgumentParser(description='text files of test terminal output')
parser.add_argument('pathone', type=str)
parser.add_argument('pathtwo', type=str)
parser.add_argument('test_data', type=str)

args = parser.parse_args()

with open(args.test_data, 'r') as f:
    dataset = json.load(f)

# count all categories in dataset
cat_count = {}
for a in dataset['annotations']:
    cat = dataset["categories"][a['category_id']]['name']
    if cat not in cat_count:
        cat_count[cat] = 0
    cat_count[cat] += 1


with open(args.pathone, 'r') as f:
    t1 = f.readlines()
with open(args.pathtwo, 'r') as f:
    t2 = f.readlines()

t1_bbox = []
t1_segm = []
t2_bbox = []
t2_segm = []

start_cut = 26
end_cut = 46
for i, l in enumerate(t1):
    if "Evaluating segm..." in l:
        t1_segm = t1[i+start_cut:i+end_cut]
    elif "Evaluating bbox..." in l:
        t1_bbox = t1[i+start_cut:i+end_cut]
for i, l in enumerate(t2):
    if "Evaluating segm..." in l:
        t2_segm = t2[i+start_cut:i+end_cut]
    elif "Evaluating bbox..." in l:
        t2_bbox = t2[i+start_cut:i+end_cut]

t1 = {"segm": {}, "bbox": {}}
t2 = {"segm": {}, "bbox": {}}

for line in t1_bbox:
    x = [y.strip() for y in line.split('|')]
    for i in range(3):
        t1["bbox"][x[1+i*2]] = x[2+i*2]
for line in t1_segm:
    x = [y.strip() for y in line.split('|')]
    for i in range(3):
        t1["segm"][x[1+i*2]] = x[2+i*2]
for line in t2_bbox:
    x = [y.strip() for y in line.split('|')]
    for i in range(3):
        t2["bbox"][x[1+i*2]] = x[2+i*2]
for line in t2_segm:
    x = [y.strip() for y in line.split('|')]
    for i in range(3):
        t2["segm"][x[1+i*2]] = x[2+i*2]

cats = t1["bbox"].keys()


for x in ["bbox", "segm"]:
    print(f"\n{x} of {args.pathone} & {args.pathtwo}:\n")
    tmp = "\\&" # can't use backslash in f-expression
    for k in cats:
        if cat_count.get(k, 0):
            diff = float(t2[x][k]) - float(t1[x][k])
            print(f"{k.replace('&', tmp)} & {cat_count.get(k, 0)} & {t1[x][k]} & {t2[x][k]} & {'+' if diff > 0 else ''}{diff:.3f} \\\\", )
