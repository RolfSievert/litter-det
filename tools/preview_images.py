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
import random

parser = argparse.ArgumentParser(description='List Creative Commons images from dataset.')
parser.add_argument('anns', help='json annotation file')
parser.add_argument('data_root', help='json annotation file')

args = parser.parse_args()

with open(args.anns, 'r') as f:
    anns = json.load(f)

images = anns["images"]
random.shuffle(images)

licenses = ['CC', "ODBL (c) OpenLitterMap & Contributors"]

for i in images:
    if i["license"] in licenses:
        print(args.data_root + i["file_name"], end=' ')
