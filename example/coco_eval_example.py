import os.path as osp

from pycocotools.coco import COCO
from caption_metrics import COCOEvaluation

DIR = osp.abspath(osp.join(__file__, '..'))
annotation_file = osp.join(DIR, 'captions_val2014.json')
results_file = osp.join(DIR, 'captions_val2014_fakecap_results.json')

# create coco object and coco_result object
coco = COCO(annotation_file)
coco_result = coco.loadRes(results_file)

# create coco_eval object by taking coco and coco_result
coco_eval = COCOEvaluation(coco, silent=True)

# evaluate results
# SPICE will take a few minutes the first time, but speeds up due to caching
coco_eval.evaluate(coco_result)

# print output evaluation scores
for metric, score in coco_eval.eval.items():
    print(f'{metric}: {score:.3f}')
