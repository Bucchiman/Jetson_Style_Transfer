#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	record
# CreatedDate:  2021-10-17 23:16:50 +0900
# LastModified: 2021-10-30 03:40:45 +0900
#


import os
import cv2

from parser import gstreamer_pipeline, get_record_parser
from video2image import Video2Image
from stylize_video import Stylize_Video


def main():
    args = get_record_parser()
    if not os.path.exists(args["output_path"]):
        os.makedirs(args["output_path"])

    cam = cv2.VideoCapture(gstreamer_pipeline(display_width=400, display_height=600), cv2.CAP_GSTREAMER)

    fps = cam.get(cv2.CAP_PROP_FPS)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(height, width)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    out = cv2.VideoWriter(os.path.join(args["output_path"], "original.mp4"),
                          int(fourcc), fps, (int(width), int(height)))

    while True:
        ret, img = cam.read()
        if ret is not True:
            break

        cv2.imshow("Original_Image", img)
        out.write(img)

        key = cv2.waitKey(30)
        if key == 27:
            break

    out.release()
    cam.release()
    cv2.destroyAllWindows()

    Video2Image(args["output_path"])
    Stylize_Video(args["output_path"], args["model_path"])


if __name__ == "__main__":
    main()
