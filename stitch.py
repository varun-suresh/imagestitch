"""
Define all the functions needed to stitch multiple images
"""
from typing import List
import numpy as np
import cv2
from matplotlib import pyplot as plt

class Stitcher:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
        self.N = 50
    
    def stitch(self):
        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(self.img1, None)
        kp2, des2 = orb.detectAndCompute(self.img2, None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)

        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        dstPoints = np.array([ kp1[matches[i].queryIdx].pt for i in range(self.N)])
        srcPoints = np.array([ kp2[matches[i].trainIdx].pt for i in range(self.N)])
        M, mask = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC,5.0)
        print("Homography matrix: ", M)
        warpedImage = cv2.warpPerspective(self.img2, M, (self.img1.shape[0]+self.img2.shape[0],self.img1.shape[0]))
        warpedImage[0:self.img1.shape[0], 0:self.img1.shape[1]] = self.img1
        return warpedImage

if __name__ == "__main__":
    img1 = cv2.imread('images/hill/1.jpg')
    img2 = cv2.imread('images/hill/2.jpg')
    stitcher = Stitcher(img1, img2)
    stitched_image = stitcher.stitch()
    print(stitched_image.shape)

