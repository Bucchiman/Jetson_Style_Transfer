#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	live_record
# CreatedDate:  2021-10-17 16:22:30 +0900
# LastModified: 2021-10-29 04:00:39 +0900
#


import sys
import keras
from keras.preprocessing.image import img_to_array
import numpy as np
import cv2
import keras_contrib

import layers
from parser import get_live_parser, gstreamer_pipeline


def main():
#    if sys.argv:
#        del sys.argv[1:]
    args = get_live_parser()

    custom_objects = {
        'InstanceNormalization': keras_contrib.layers.InstanceNormalization,
        'DeprocessStylizedImage': layers.DeprocessStylizedImage
    }
    transfer_net = keras.models.load_model(
        args["model_path"],
        custom_objects=custom_objects
    )

    image_size = transfer_net.input_shape[1: 3]

    inputs = [transfer_net.input, keras.backend.learning_phase()]
    outputs = [transfer_net.output]

    transfer_style = keras.backend.function(inputs, outputs)

    cam = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

    while True:
        ret, original_img = cam.read()
        if ret is not True:
            break

        resized_img = cv2.resize(original_img, (image_size[0], image_size[1]))
        img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        img = img_to_array(img)
        img = np.array(img)[:, :, :3]
        img = np.expand_dims(img, axis=0)

        out_img = transfer_style([img, 1])[0]
        out_img = cv2.cvtColor(out_img[0], cv2.COLOR_RGB2BGR)

        if args["type"] == 'style_only':
            show_img = np.uint8(cv2.resize(out_img, (1280, 720)))

        else:
           show_original_img = cv2.cvtColor(cv2.resize(resized_img, (480, 640)), cv2.COLOR_RGB2BGR)
           show_out_img = cv2.resize(out_img, (480, 640))
           show_img = np.hstack((np.uint8(show_original_img), np.uint8(show_out_img)))


        cv2.imshow('stylize movie', show_img)

        key = cv2.waitKey(10)
        if key == 27:  # ESC
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
