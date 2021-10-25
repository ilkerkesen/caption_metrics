Evaluation Metrics for Image Captioning
===================
This package is a fork of Python 3 compatible [pycocoevalcaps](https://github.com/salaniz/pycocoevalcap) package. There are several differences,
- Better repo structure for development.
- Modular `COCOEvalCap` implementation (renamed as `COCOEvaluation`).
- Increased PEP8 compatibility.

You can find the original repository in [here](https://github.com/tylin/coco-caption) which is not Python 3 compatible.

## Requirements ##
- Java 1.8.0
- Python 3

## Installation ##
To install caption_metrics along with the dependencies, run:
```
git clone https://github.com/ilkerkesen/caption_metrics
cd caption_metrics
pip install -e .
```

## Usage ##
See the example script: [example/coco_eval_example.py](example/coco_eval_example.py)
