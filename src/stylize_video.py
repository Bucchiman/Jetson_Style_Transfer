#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	stylize_movie
# CreatedDate:  2021-10-10 23:44:01 +0900
# LastModified: 2021-10-18 03:17:44 +0900
#


import os
import cv2
import tensorflow as tf
import numpy as np
import keras
from keras.preprocessing.image import img_to_array
import keras_contrib

import layers



def Stylize_Video(output_path, model_path):
    tmp_dir = os.path.join(output_path, "tmp")
    custom_objects = {
        'InstanceNormalization': keras_contrib.layers.InstanceNormalization,
        'DeprocessStylizedImage': layers.DeprocessStylizedImage
    }
    transfer_net = keras.models.load_model(
        model_path,
        custom_objects=custom_objects
    )

    image_size = transfer_net.input_shape[1: 3]

    inputs = [transfer_net.input, keras.backend.learning_phase()]
    outputs = [transfer_net.output]

    transfer_style = keras.backend.function(inputs, outputs)


    for img_name in os.listdir(tmp_dir):

        img = cv2.imread(os.path.join(tmp_dir, img_name))
        img = cv2.resize(img, (image_size[0], image_size[1]))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img_to_array(img)
        img = np.array(img)[:, :, :3]
        img = np.expand_dims(img, axis=0)

        out_img = transfer_style([img, 1])[0]

        out_img = cv2.cvtColor(out_img[0], cv2.COLOR_RGB2BGR)
        out_img = cv2.resize(out_img, (640, 480))
#        cv2.imshow('stylize movie', np.uint8(out_img))
        cv2.imwrite(os.path.join(tmp_dir, img_name), np.uint8(out_img))


