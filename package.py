# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

import argparse
import glob
import os
import pickle
import random
import cv2


def pickle_examples(paths, train_path, val_path, train_val_split=0.1):
    """
    Compile a list of examples into pickled format, so during
    the training, all io will happen in memory
    """
    with open(train_path, 'wb') as ft:
        with open(val_path, 'wb') as fv:
            for p in paths:
                img = cv2.imread(p)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                print(img.shape)

                shape = img.shape
                for c in range(shape[0]):
                    for r in range(shape[1]):
                        if img[c][r] < 128:
                            img[c][r] = 0
                        else:
                            img[c][r] = 255

                r = random.random()
                if r < train_val_split:
                    pickle.dump(img, fv)
                else:
                    pickle.dump(img, ft)


parser = argparse.ArgumentParser(description='Compile list of images into a pickled object for training')
parser.add_argument('--dir', dest='dir', required=True, help='path of examples')
parser.add_argument('--save_dir', dest='save_dir', required=True, help='path to save pickled files')
parser.add_argument('--split_ratio', type=float, default=0.1, dest='split_ratio',
                    help='split ratio between train and val')
args = parser.parse_args()

if __name__ == "__main__":
    train_path = os.path.join(args.save_dir, "train.obj")
    val_path = os.path.join(args.save_dir, "val.obj")
    pickle_examples(glob.glob(os.path.join(args.dir, "*.jpg")), train_path=train_path, val_path=val_path,
                    train_val_split=args.split_ratio)
