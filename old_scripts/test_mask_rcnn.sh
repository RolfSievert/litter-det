cd mmdetection

O_PATH="../benchmarks/mask_test.txt"
EVAL=("segm" "bbox" "proposal")

# empty output
echo "" > $O_PATH

for e in "${EVAL[@]}"; do
    python tools/eval_metric.py  ../configs/mask_rcnn_linker.py  ../MaskRCNN_100.pkl --eval $e >> $O_PATH
done

cd -
