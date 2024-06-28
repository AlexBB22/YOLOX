#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "/kaggle/input/d/alexandrubobe2/safety2017"
        self.train_ann = "/kaggle/input/d/alexandrubobe2/safety2017/train2017/_annotations.coco.json"
        self.val_ann = "/kaggle/input/d/alexandrubobe2/safety2017/val2017/_annotations.coco.json"

        self.num_classes = 5

        self.max_epoch = 300
        # self.data_num_workers = 4
        self.eval_interval = 1
        self.basic_lr_per_img = 0.005 / 64.0
