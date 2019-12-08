# Evaluation of Bird-ROI-Detection-
Dice coefficient is used as evaluaion metric to measure the segmentation accuracy of bird ROI detection.

Dice coefficient = (area of intersection between original ROI and detected ROI)/sum of area of original+detected ROIs.
The value of dice coef varies from 0 to 1.

=========================
BOUNDING BOXES:
=========================

Each image contains a single bounding box label.  

boundingbox_gt.txt contain groundtruth bounding box labels and boundingbox_pred.txt contain the detected boundingbox labels, with each line corresponding to one image in the format: 

        <image_id> <x> <y> <width> <height>

    where <image_id> corresponds to the ID of each image, and <x>, <y>, <width>, and <height> are all measured in pixels

"Blue" - groundtruth bounding box

"green" - detected bounding box

"red" - ROI intersection of groundtruth and detected bounding box

# Description

    /dice_coef_eval_codes - codes and files for dice coefficient evalaution
    /bounding_box_samples - examples for groundtruth ROIs
    /dice_coef_eval_example - different cases of dice coefficient estimation
    /multiple_bird_detection- examples of multiple bird detection cases


