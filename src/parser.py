#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	parser
# CreatedDate:  2021-10-17 16:26:45 +0900
# LastModified: 2021-10-18 13:16:27 +0900
#


import os
import argparse


def get_live_parser():
    parser = argparse.ArgumentParser(
        description='Real-Time Style Transfer'
    )

    parser.add_argument('--model_path', type=str,
                        help='model path from trained models')

    return vars(parser.parse_args())


def get_record_parser():
    parser = argparse.ArgumentParser(
        description='Record Style Transfer'
    )

    parser.add_argument('--output_path', type=str, help='output about videos')
    parser.add_argument('--model_path', type=str)


    return vars(parser.parse_args())


def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=400,
    display_height=600,
    framerate=20,
    flip_method=0,
):
    return ("nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx !"
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (capture_width,
               capture_height,
               framerate,
               flip_method,
               display_width,
               display_height))
