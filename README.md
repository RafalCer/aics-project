# There is Noise on Your Face, but there is no Nose: An Exploration of Data Augmentation Methods for Captioning Facial Features

## Viktorija Buzaitė, Eva Elžbieta Sventickaitė, Rafal Černiavski

### Final project for the Artificial Intelligence: Cognitive Systems course at Gothenburg University 

This repository contains the code, report, results, and other supplementary materials for our final project. We uploaded all the code we produced or adapted in the form of Jupyter notebooks for convenience. 

The structure of the repository is as follows:

```bash
│   README.md
│   Report.pdf
│
├───notebooks
│   │   AI Preprocessing.ipynb
│   │
│   ├───captioning_and_evaluation
│   │   │   feature_evaluation.ipynb
│   │   │   meteor.ipynb
│   │   │   preprocess.ipynb
│   │   │   test.ipynb
│   │   │
│   │   ├───a-PyTorch-Tutorial-to-Image-Captioning
│   │   │
│   │   └───pymeteor
│   │
│   ├───image_and_caption_augmentation
│   │   │   Face2Sketch.ipynb
│   │   │   textual_augmenter_ant.ipynb
│   │   │
│   │   ├───ca-gan
│   │   │
│   │   └───pytorch-CycleGAN-and-pix2pix
│   │
│   └───linear_feature_recognition
│           Linear_models .ipynb
│
├───notes
│       2022-01-04-meeting-notes.md
│       Project proposal LaTeX.pdf
│       Project proposal Markdown.md
│
└───results
    │   feature_eval_results.txt
    │   meteor_results.json
    │
    ├───caption_augmentation
    │       caption_augmentation_demo.png
    │
    ├───caption_augmentation_results
    ├───caption_predictions
    │       predictions_celeb_small_res_m10_trained_on_all_antons.json
    │       predictions_celeb_small_res_m3_trained_on_celeb_small_res.json
    │       predictions_celeb_small_res_m5_trained_on_sketches.json
    │       predictions_celeb_small_res_m6_trained_on_freakshow.json
    │       predictions_celeb_small_res_m7_trained_on_b_sketches.json
    │       predictions_celeb_small_res_m8_trained_on_mixed.json
    │       predictions_celeb_small_res_m9_trained_on_antons.json
    │       predictions_freakshow_m10_trained_on_all_antons.json
    │       predictions_freakshow_m3_trained_on_celeb_small_res.json
    │       predictions_freakshow_m5_trained_on_sketches.json
    │       predictions_freakshow_m6_trained_on_freakshow.json
    │       predictions_freakshow_m7_trained_on_b_sketches.json
    │       predictions_freakshow_m8_trained_on_mixed.json
    │       predictions_freakshow_m9_trained_on_antons.json
    │       predictions_sketches_m10_trained_on_all_antons.json
    │       predictions_sketches_m3_trained_on_celeb_small_res.json
    │       predictions_sketches_m5_trained_on_sketches.json
    │       predictions_sketches_m6_trained_on_freakshow.json
    │       predictions_sketches_m7_trained_on_b_sketches.json
    │       predictions_sketches_m8_trained_on_mixed.json
    │       predictions_sketches_m9_trained_on_antons.json
    │
    ├───image_augmentation_results
    │       datasets_demo.png
    │
    └───linear_feature_prediction_results
            knn_macro.png
            knn_micro.png
            linear_feature_prediction_scores.txt
            random_forest_macro.png
            random_forest_micro.png
```
