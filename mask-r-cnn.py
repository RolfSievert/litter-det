#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Rolf Sievert
#
# Distributed under terms of the MIT license.

"""

"""
from mmdet.apis import init_detector, inference_detector
import mmcv

# Get path to mmdet
import os
SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
MMDET_FOLDER = os.path.join(script_folder, "mmdetection/")


config_file = os.path.join(MMDET_FOLDER, 'configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_poly_1x_coco_v1.py')
checkpoint_file = os.path.join(SCRIPT_FOLDER, 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth')

# build the model from a config file and a checkpoint file
device = 'cpu' # 'cuda:0'
model = init_detector(config_file, checkpoint_file, device=device)

# test a single image and show the results
img = 'test.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# visualize the results in a new window
model.show_result(img, result)
# or save the visualization results to image files
model.show_result(img, result, out_file='result.jpg')

# test a video and show the results
video = mmcv.VideoReader('video.mp4')
for frame in video:
    result = inference_detector(model, frame)
    model.show_result(frame, result, wait_time=1)
