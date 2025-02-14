# Stitch Images

Given 2 images (left and right in that order), stitch the image to create a panorama image.

![Initial State](https://github.com/varun-suresh/imagestitch/blob/main/images/screenshots/1.png) |![Upload Images](https://github.com/varun-suresh/imagestitch/blob/main/images/screenshots/2.png) | ![Result](https://github.com/varun-suresh/imagestitch/blob/main/images/screenshots/3.png)

## Baseline approach

To stitch two images

1. Find the keypoints in the first and second image. In this case, I used [ORB](https://docs.opencv.org/4.x/d1/d89/tutorial_py_orb.html) from the CV2 library.
2. Find the keypoint matches between the two images and sort them by distance.
3. Estimate the homography matrix using the keypoint matches.
4. Using the homography matrix, project the second image in the reference frame of the first image.
5. Put the first image and the projected second image side by side.
