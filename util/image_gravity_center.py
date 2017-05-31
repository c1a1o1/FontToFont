import cv2
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser(description='ImageCenter')
parser.add_argument('--dir', dest='dir', required=True,
                    help='data directory')
parser.add_argument('--target', dest='target', required=True,
                    help='target directory')
args = parser.parse_args()


def main():
    print("Begin to process images")
    img_list = os.listdir(args.dir)
    for img in img_list:
        img_path = os.path.join(args.dir, img)
        if 'jpg' not in img:
            continue

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
        src_g_c_c = int(np.mean(COLS)) + 256
        print("src c:{} r:{}".format(src_g_c_c, src_g_c_r))

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

        # draw the axis on the image

        cv2.line(image_, (src_g_c_c+4, src_g_c_r+4), (src_g_c_c-4, src_g_c_r-4), (0, 255, 0), 1)
        cv2.line(image_, (src_g_c_c-4, src_g_c_r+4), (src_g_c_c+4, src_g_c_r-4), (0, 255, 0), 1)
        cv2.line(image_, (tag_g_c_c+4, tag_g_c_r+4), (tag_g_c_c-4, tag_g_c_r-4), (0, 255, 0), 1)
        cv2.line(image_, (tag_g_c_c-4, tag_g_c_r+4), (tag_g_c_c+4, tag_g_c_r-4), (0, 255, 0), 1)

        cv2.imwrite(os.path.join(args.target, img), image_)


if __name__ == '__main__':
    main()





