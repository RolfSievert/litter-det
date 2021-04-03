#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Uses matplotlib to visualize training loss and validation AP.
"""

import matplotlib.pyplot as plt
import os.path
import json
import argparse


parser = argparse.ArgumentParser(description='User args')
parser.add_argument('log', help='Path to json log file')
parser.add_argument('--loss_scores', nargs="+", default=["loss"], help='Which losses to plot of train')
parser.add_argument('--val_scores', nargs="+", default=["bbox_mAP", "segm_mAP"], help='Which validation scores to plot of val')

args = parser.parse_args()
loss_scores = args.loss_scores
val_scores = args.val_scores

with open(args.log, 'r') as f:
    log = [json.loads(line) for line in f]

losses = {k: [] for k in loss_scores}
val = {k: [] for k in val_scores}
max_val = {k: (-1, -1) for k in val_scores}

train_e = -1
val_e = -1
for l in log:
    e = l["epoch"]
    if l["mode"] == "train":
        # append next epoch
        if train_e != e:
            train_e = e
            for k in loss_scores:
                losses[k].append([])
        # add values
        for k in loss_scores:
            losses[k][e-1].append(l[k])

    if l["mode"] == "val":
        # add values
        for k in val_scores:
            val[k].append(l[k])

            # save maximum found value together with epoch
            if l[k] > max_val[k][1]:
                max_val[k] = (len(val[k]), l[k]) # epoch, value

loss_x_values = []

# loop through logs l from every epoch e
for e, l in enumerate(losses[loss_scores[0]]):
    # add horizontal values per epoch
    loss_x_values += [e + x/len(l) for x in range(len(l))]

dpi = 200

plt.style.use("seaborn-darkgrid")

plt.figure()
for score, v in val.items():
    plt.plot(range(1, len(v)+1), v, label=f'{score}')
#plt.show()
plt.xlabel("epoch")
plt.ylabel("mAP")
plt.legend()
plt.savefig(f"validation.jpg", dpi=dpi, bbox_inches='tight')

plt.figure()
for score, v in losses.items():
    plt.plot(loss_x_values, [x for epoch in v for x in epoch], label=f'{score}')
#plt.show()
plt.xlabel("epoch")
plt.ylabel("mAP")
plt.legend()
plt.savefig(f"train.jpg", dpi=dpi, bbox_inches='tight')

def print_val_of_epoch(validation, epoch):
    for k, v in validation.items():
        print(f"\t\t{k}: {v[epoch]}")

# print max values of validation
print("Max values of validation scores:")
for k, v in max_val.items():
    print(f"\tepoch {v[0]}: {v[1]} {k}")
    print_val_of_epoch(val, v[0]-1)

#plt.savefig("train_inst.jpg")
#plt.show()
