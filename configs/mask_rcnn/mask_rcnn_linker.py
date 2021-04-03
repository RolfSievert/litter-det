_base_ = [
    # model config
    './mask_rcnn_r50_fpn.py',
    # dataset settings and pipeline
    '../taco_instance.py',
    # default scheduler and runtime
    '../schedule_100e.py', '../default_runtime.py'
]
