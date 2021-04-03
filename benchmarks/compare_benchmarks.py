#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 znap <znap@asusmanjaro>
#
# Distributed under terms of the MIT license.

"""
Prints two test benchmarks in latex table format.
"""

import argparse
import json

parser = argparse.ArgumentParser(description='text files of test terminal output')
parser.add_argument('pathone', type=str)
parser.add_argument('pathtwo', type=str)

args = parser.parse_args()

with open(args.pathone, 'r') as f:
    t1 = f.readlines()
with open(args.pathtwo, 'r') as f:
    t2 = f.readlines()

t1_bbox = []
t1_segm = []
t2_bbox = []
t2_segm = []

def find_line_containing(txt, match):
    for i, l in enumerate(txt):
        if match in l:
            return i
    print(f"{match} not found")
    exit(1)

searches = ["Evaluating proposal...", "Evaluating bbox...", "Evaluating segm..."]

for s in searches:
    print(s)
    i1 = find_line_containing(t1, s)
    i2 = find_line_containing(t2, s)

    start_cut = 10

    grep = {
        0: ["mAP", "all"],
        1: ["mAP$_{0.5}$", "all"],
        2: ["mAP$_{0.75}$", "all"],
        3: ["mAP", "small"],
        4: ["mAP", "medium"],
        5: ["mAP", "large"],
        6: ["mAR", "all"],
        9: ["mAR", "small"],
        10: ["mAR", "medium"],
        11: ["mAR", "large"],
    }

    i1+=start_cut
    i2+=start_cut
    for i, [score, area] in grep.items():
        val1 = float(t1[i1+i].split()[-1])
        val2 = float(t2[i2+i].split()[-1])
        diff = val2 - val1
        sign = '' if val1 > val2 else '+'
        print(f"\t{score} & {area} & {val1:.3f} & {val2:.3f} & {sign}{diff:.3f} \\\\")
