
# Instance Segmentation of Litter - Thesis Project

![video of DetectoRS](demo/detectors_demo.gif)

This project explored using [Mask R-CNN](https://arxiv.org/pdf/1703.06870.pdf) and [DetectoRS](https://arxiv.org/pdf/2006.02334.pdf) to do instance segmentation of litter.
A comparison of Mask R-CNN with and without oversampling was also tested.
Metrics are presented in the [COCO format](https://cocodataset.org/#detection-eval).

This project was realized with [TACO](https://github.com/pedropro/TACO) and [MMDetection](https://github.com/open-mmlab/mmdetection).

Data is split using second order iterative stratification from the [scikit-multilearn](http://scikit.ml/api/skmultilearn.model_selection.iterative_stratification.html) python package.

## Installation

* Install PyTorch
* Install mmcv with correct version and cuda version according to MMDetection and pytorch installment respectively
* Install MMDetection
* Download TACO dataset
* Link TACO data folder to `mmdetection/data/TACO`
* Install `pip install scikit-multilearn` to split dataset with iterative stratification

## Scripts

The folder `tools/` contains some small helper scripts,

* `category_count.py` -- plots and prints category quantities
* `class_count.py` -- prints quantities of each category in order of annotation ID
* `create_demo_anns.py` -- creates a new annotation file from images defined in the script to be used with running tests to generate demos
* `data_distribution_visualizer.py` -- plots category quantity and the number of images per category of train, validation, and test sets
* `plot_train_logs.py` -- prints training loss and validation scores using information from training log
* `preview_images.py` -- lists all images with specified licenses from annotations. To display images, use with feh: `feh $(python preview_images.py anns/annotations_test.json data/TACO/)`
* `split_dataset` -- take annotations and split into train, validation, and test using second order iterative stratification

## Configurations

Model configurations lie within folder `configs/`, which originate from MMDetection's model zoo, and are adapted to work with the used hardware of this project and the dataset.
