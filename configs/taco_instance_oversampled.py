dataset_type = 'CocoDataset'
data_root = 'data/TACO/'
anns_root = '../anns/'


classes = {
    0: {'name': 'Aluminium foil', 'supercategory': 'Aluminium foil', 'image_count': 43, 'instance_count': 62}, 1: {'name': 'Battery', 'supercategory': 'Battery', 'image_count': 2, 'instance_count': 2}, 2: {'name': 'Aluminium blister pack', 'supercategory': 'Blister pack', 'image_count': 6, 'instance_count': 6}, 3: {'name': 'Carded blister pack', 'supercategory': 'Blister pack', 'image_count': 1, 'instance_count': 1}, 4: {'name': 'Other plastic bottle', 'supercategory': 'Bottle', 'image_count': 45, 'instance_count': 50}, 5: {'name': 'Clear plastic bottle', 'supercategory': 'Bottle', 'image_count': 225, 'instance_count': 285}, 6: {'name': 'Glass bottle', 'supercategory': 'Bottle', 'image_count': 74, 'instance_count': 104}, 7: {'name': 'Plastic bottle cap', 'supercategory': 'Bottle cap', 'image_count': 185, 'instance_count': 209}, 8: {'name': 'Metal bottle cap', 'supercategory': 'Bottle cap', 'image_count': 55, 'instance_count': 80}, 9: {'name': 'Broken glass', 'supercategory': 'Broken glass', 'image_count': 15, 'instance_count': 138}, 10: {'name': 'Food Can', 'supercategory': 'Can', 'image_count': 20, 'instance_count': 34}, 11: {'name': 'Aerosol', 'supercategory': 'Can', 'image_count': 10, 'instance_count': 10}, 12: {'name': 'Drink can', 'supercategory': 'Can', 'image_count': 151, 'instance_count': 229}, 13: {'name': 'Toilet tube', 'supercategory': 'Carton', 'image_count': 3, 'instance_count': 5}, 14: {'name': 'Other carton', 'supercategory': 'Carton', 'image_count': 79, 'instance_count': 93}, 15: {'name': 'Egg carton', 'supercategory': 'Carton', 'image_count': 9, 'instance_count': 11}, 16: {'name': 'Drink carton', 'supercategory': 'Carton', 'image_count': 41, 'instance_count': 45}, 17: {'name': 'Corrugated carton', 'supercategory': 'Carton', 'image_count': 41, 'instance_count': 64}, 18: {'name': 'Meal carton', 'supercategory': 'Carton', 'image_count': 27, 'instance_count': 30}, 19: {'name': 'Pizza box', 'supercategory': 'Carton', 'image_count': 3, 'instance_count': 3}, 20: {'name': 'Paper cup', 'supercategory': 'Cup', 'image_count': 62, 'instance_count': 67}, 21: {'name': 'Disposable plastic cup', 'supercategory': 'Cup', 'image_count': 91, 'instance_count': 104}, 22: {'name': 'Foam cup', 'supercategory': 'Cup', 'image_count': 11, 'instance_count': 13}, 23: {'name': 'Glass cup', 'supercategory': 'Cup', 'image_count': 4, 'instance_count': 6}, 24: {'name': 'Other plastic cup', 'supercategory': 'Cup', 'image_count': 2, 'instance_count': 2}, 25: {'name': 'Food waste', 'supercategory': 'Food waste', 'image_count': 7, 'instance_count': 8}, 26: {'name': 'Glass jar', 'supercategory': 'Glass jar', 'image_count': 4, 'instance_count': 6}, 27: {'name': 'Plastic lid', 'supercategory': 'Lid', 'image_count': 69, 'instance_count': 77}, 28: {'name': 'Metal lid', 'supercategory': 'Lid', 'image_count': 6, 'instance_count': 10}, 29: {'name': 'Other plastic', 'supercategory': 'Other plastic', 'image_count': 171, 'instance_count': 273}, 30: {'name': 'Magazine paper', 'supercategory': 'Paper', 'image_count': 5, 'instance_count': 12}, 31: {'name': 'Tissues', 'supercategory': 'Paper', 'image_count': 36, 'instance_count': 42}, 32: {'name': 'Wrapping paper', 'supercategory': 'Paper', 'image_count': 11, 'instance_count': 12}, 33: {'name': 'Normal paper', 'supercategory': 'Paper', 'image_count': 68, 'instance_count': 82}, 34: {'name': 'Paper bag', 'supercategory': 'Paper bag', 'image_count': 23, 'instance_count': 27}, 35: {'name': 'Plastified paper bag', 'supercategory': 'Paper bag', 'image_count': 0, 'instance_count': 0}, 36: {'name': 'Plastic film', 'supercategory': 'Plastic bag & wrapper', 'image_count': 310, 'instance_count': 451}, 37: {'name': 'Six pack rings', 'supercategory': 'Plastic bag & wrapper', 'image_count': 4, 'instance_count': 5}, 38: {'name': 'Garbage bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 20, 'instance_count': 31}, 39: {'name': 'Other plastic wrapper', 'supercategory': 'Plastic bag & wrapper', 'image_count': 184, 'instance_count': 260}, 40: {'name': 'Single-use carrier bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 49, 'instance_count': 61}, 41: {'name': 'Polypropylene bag', 'supercategory': 'Plastic bag & wrapper', 'image_count': 3, 'instance_count': 3}, 42: {'name': 'Crisp packet', 'supercategory': 'Plastic bag & wrapper', 'image_count': 35, 'instance_count': 39}, 43: {'name': 'Spread tub', 'supercategory': 'Plastic container', 'image_count': 9, 'instance_count': 9}, 44: {'name': 'Tupperware', 'supercategory': 'Plastic container', 'image_count': 4, 'instance_count': 4}, 45: {'name': 'Disposable food container', 'supercategory': 'Plastic container', 'image_count': 37, 'instance_count': 38}, 46: {'name': 'Foam food container', 'supercategory': 'Plastic container', 'image_count': 13, 'instance_count': 15}, 47: {'name': 'Other plastic container', 'supercategory': 'Plastic container', 'image_count': 6, 'instance_count': 6}, 48: {'name': 'Plastic glooves', 'supercategory': 'Plastic glooves', 'image_count': 4, 'instance_count': 4}, 49: {'name': 'Plastic utensils', 'supercategory': 'Plastic utensils', 'image_count': 29, 'instance_count': 37}, 50: {'name': 'Pop tab', 'supercategory': 'Pop tab', 'image_count': 71, 'instance_count': 99}, 51: {'name': 'Rope & strings', 'supercategory': 'Rope & strings', 'image_count': 28, 'instance_count': 29}, 52: {'name': 'Scrap metal', 'supercategory': 'Scrap metal', 'image_count': 12, 'instance_count': 20}, 53: {'name': 'Shoe', 'supercategory': 'Shoe', 'image_count': 6, 'instance_count': 7}, 54: {'name': 'Squeezable tube', 'supercategory': 'Squeezable tube', 'image_count': 6, 'instance_count': 7}, 55: {'name': 'Plastic straw', 'supercategory': 'Straw', 'image_count': 110, 'instance_count': 157}, 56: {'name': 'Paper straw', 'supercategory': 'Straw', 'image_count': 4, 'instance_count': 4}, 57: {'name': 'Styrofoam piece', 'supercategory': 'Styrofoam piece', 'image_count': 78, 'instance_count': 112}, 58: {'name': 'Unlabeled litter', 'supercategory': 'Unlabeled litter', 'image_count': 269, 'instance_count': 517}, 59: {'name': 'Cigarette', 'supercategory': 'Cigarette', 'image_count': 227, 'instance_count': 667}
}

class_names = [v['name'] for k, v in classes.items()]

### default pipeline
# taco norm std
#img_norm_cfg = dict(
    #mean=[124.20980350548206, 119.07613691050055, 106.64417264260621],
    #std=[63.75104021539383, 60.982119813841386, 61.72956009487551],
    #to_rgb=False)

# norm of taco train data
img_norm_cfg = dict(
    mean=[124.88084477474031, 119.0808394214224, 106.7341802522661],
    std=[63.685021163851864, 61.00485803391499, 61.29027463037255],
    to_rgb=False)
image_res = (1074, 942) # old was 1333 800
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='Resize', img_scale=image_res, keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=image_res,
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

oversampled_train = dict(
        type='ClassBalancedDataset',
        oversample_thr=0.1,
        dataset=dict(  # This is the original config of Dataset_A
            type=dataset_type,
            classes=class_names,
            ann_file=anns_root + "annotations_train.json",
            img_prefix=data_root,
            pipeline=train_pipeline,
        )
    )

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=oversampled_train,
    val=dict(
        type=dataset_type,
        classes=class_names,
        ann_file=anns_root + "annotations_val.json",
        img_prefix=data_root,
        pipeline=test_pipeline,
             ),
    test=dict(
        type=dataset_type,
        classes=class_names,
        ann_file=anns_root + "annotations_test.json",
        img_prefix=data_root,
        pipeline=test_pipeline,
    ))

# add cls?
evaluation = dict(metric=['bbox', 'segm'])
