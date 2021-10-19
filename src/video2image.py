#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	video2image
# CreatedDate:  2021-10-18 00:00:50 +0900
# LastModified: 2021-10-18 03:44:04 +0900
#


import os
import cv2


def getFrame(vidcap, sec, tmp_dir, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("{}/image_{}.jpg".format(tmp_dir,
                                             str(count).zfill(5)),
                                             image)
    return hasFrames


def Video2Image(output_path):
    tmp_dir = os.path.join(output_path, "tmp")
    os.makedirs(tmp_dir)
    vidcap = cv2.VideoCapture('{}/original.mp4'.format(output_path))
    sec = 0
    frameRate = 0.05  # it will capture image in each 0.5 second
    count = 1
    success = getFrame(vidcap, sec, tmp_dir, count)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(vidcap, sec, tmp_dir, count)
