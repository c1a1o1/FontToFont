# -*- coding: utf-8 -*-

import cv2
import argparse
import os
import numpy as np
import re

parser = argparse.ArgumentParser(description='ImageCenter')
parser.add_argument('--dir', dest='dir', required=True,
                    help='data directory')
parser.add_argument('--target', dest='target', required=True,
                    help='target directory')
args = parser.parse_args()


def main():
    print("Begin to process images")
    img_list = os.listdir(args.dir)
    with open("gravity_center_statistics.txt", mode="w") as out:
        for img in img_list:
            img_path = os.path.join(args.dir, img)
            if 'jpg' not in img:
                continue

            re_words = re.compile(u"[\u4e00-\u9fa5]+")
            m = re_words.search(img, 0)
            print(m.group())

            image = cv2.imread(img_path)
            image_ = image

            # RGB to Grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_image = np.array(gray_image)

            src_ = gray_image[:, 256:512]
            target_ = gray_image[:, 0:256]

            #  source image -- kai
            ROWS = []
            COLS = []

            for r in range(256):
                for c in range(256):
                    if src_[r][c] <= 80:
                        ROWS.append(r)
                        COLS.append(c)

            src_g_c_r = int(np.mean(ROWS))
            src_g_c_c = int(np.mean(COLS))
            print("src c:{} r:{}".format(src_g_c_c, src_g_c_r))
            src_g_c_c += 256

            # target image - qigong
            ROWS = []
            COLS = []

            for r in range(256):
                for c in range(256):
                    if target_[r][c] <= 80:
                        ROWS.append(r)
                        COLS.append(c)

            tag_g_c_r = int(np.mean(ROWS))
            tag_g_c_c = int(np.mean(COLS))
            print("tag c:{} r:{}".format(tag_g_c_c, tag_g_c_r))

            # draw edges
            cv2.line(image_, (0, 0), (511, 0), (0, 0, 0), 2)
            cv2.line(image_, (0, 0), (0, 255), (0, 0, 0), 2)
            cv2.line(image_, (255, 0), (255, 255), (0, 0, 0), 2)
            cv2.line(image_, (511, 0), (511, 255), (0, 0, 0), 2)
            cv2.line(image_, (0, 255), (511, 255), (0, 0, 0), 2)

            # draw intersected lines

            cv2.line(image_, (0, 0), (255, 255), (0, 0, 255), 1)
            cv2.line(image_, (255, 0), (0, 255), (0, 0, 255), 1)

            cv2.line(image_, (127, 0), (127, 255), (0, 0, 255), 1)
            cv2.line(image_, (0, 127), (255, 127), (0, 0, 255), 1)

            cv2.line(image_, (0, 0), (255, 255), (0, 0, 255), 1)
            cv2.line(image_, (255, 0), (0, 255), (0, 0, 255), 1)

            cv2.line(image_, (256, 0), (511, 255), (0, 0, 255), 1)
            cv2.line(image_, (256, 256), (511, 0), (0, 0, 255), 1)

            cv2.line(image_, (384, 0), (384, 255), (0, 0, 255), 1)
            cv2.line(image_, (256, 127), (511, 127), (0, 0, 255), 1)

            # draw sudoku lines
            cv2.line(image_, (0, 85), (511, 85), (166, 235, 246), 1)
            cv2.line(image_, (0, 171), (511, 171), (166, 235, 246), 1)

            cv2.line(image_, (85, 0), (85, 255), (166, 235, 246), 1)
            cv2.line(image_, (171, 0), (171, 255), (166, 235, 246), 1)
            cv2.line(image_, (341, 0), (341, 255), (166, 235, 246), 1)
            cv2.line(image_, (426, 0), (426, 255), (166, 235, 246), 1)

            # draw the axis on the image

            cv2.line(image_, (src_g_c_c + 4, src_g_c_r + 4), (src_g_c_c - 4, src_g_c_r - 4), (0, 255, 0), 2)
            cv2.line(image_, (src_g_c_c - 4, src_g_c_r + 4), (src_g_c_c + 4, src_g_c_r - 4), (0, 255, 0), 2)
            cv2.line(image_, (tag_g_c_c + 4, tag_g_c_r + 4), (tag_g_c_c - 4, tag_g_c_r - 4), (0, 255, 0), 2)
            cv2.line(image_, (tag_g_c_c - 4, tag_g_c_r + 4), (tag_g_c_c + 4, tag_g_c_r - 4), (0, 255, 0), 2)

            # cv2.imwrite(os.path.join(args.target, img), image_)

            out.write("{},{},{},{},{}\n".format(m.group(), (src_g_c_c-256), src_g_c_r, tag_g_c_c, tag_g_c_r))

            # break


if __name__ == '__main__':
    main()





