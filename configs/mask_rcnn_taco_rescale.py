_base_ = [
    # model config
    './mask_rcnn/mask_rcnn_r50_fpn.py',
    # dataset settings and pipeline
    './taco_instance_rescale.py',
    # default scheduler and runtime
    './schedule_200e.py', './default_runtime.py'
]
