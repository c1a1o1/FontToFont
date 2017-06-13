import tkinter as tk
import os
import cv2
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import numpy as np
import matplotlib as plt
plt.use('TkAgg')


Image_width = 512
Image_height = 256

input_filename_list = []
input_list = []
Image_index = 0
input_dir = None

img_TK_Input = None
img_Input = None

img_TK_Processed = None
img_Processed = None


root = tk.Tk()
root.geometry('1100x800')
root.title('Gravity center processing')

var_filelist = tk.StringVar(value=input_filename_list)

var_label = tk.StringVar()

btn_Open = tk.Button(root, text="Open", command=lambda: open(canvas_original))
btn_Process = tk.Button(root, text="Process", command=lambda: process(canvas_processed))

lbox = tk.Listbox(root, listvariable=var_filelist, height=10)

label_gc = tk.Label(root, textvariable=var_label)

canvas_original = tk.Canvas(root, width=600, height=300, bg='black')
canvas_processed = tk.Canvas(root, width=600, height=300, bg='white')

btn_Open.grid(row=0, column=0, sticky=tk.N+tk.W+tk.E)
btn_Process.grid(row=0, column=0, sticky=tk.W+tk.E+tk.S)

lbox.grid(row=1, column=0, sticky=tk.W+tk.E)

canvas_original.grid(row=0, column=1, sticky=tk.W+tk.E)
canvas_processed.grid(row=1, column=1, sticky=tk.W+tk.E)

label_gc.grid(row=0, column=2, sticky=tk.W+tk.E)


def open(canvas_original):
    global input_list
    global input_filename_list
    global input_dir

    # clear
    input_list = []
    input_filename_list = []

    input_directory = askdirectory()
    if input_directory == '':
        return

    var_filelist.set(input_filename_list)

    input_dir = input_directory

    # input images
    files = os.listdir(input_directory)
    for fl in files:
        if '.jpg' in fl:
            input_list.append(os.path.join(input_directory, fl))
            input_filename_list.append(fl)
    var_filelist.set(input_filename_list)

    try:
        global Image_index
        input_img = input_list[Image_index]

        global img_TK_Input
        global img_Input

        # input image
        image = Image.open(input_img, mode='r')
        w, h = image.size
        img_Input = image
        img_TK_Input = ImageTk.PhotoImage(image)

        canvas_original.create_image(300, 150, image=img_TK_Input)
    except Exception as e:
        return


def process(canvas_processed):
    global img_Input
    global img_TK_Processed
    global img_Processed

    image = np.array(img_Input.getdata()).astype(np.uint8).reshape((img_Input.size[1], img_Input.size[0]))

    image_ = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    print(image_.shape)
    print("image_ shape:{}".format(image_.shape))

    src_ = image[:, 256:512]
    target_ = image[:, 0:256]
    #
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

    var_label.set('楷书: ({}, {}) \n\n 启功体: ({}, {})'.format((src_g_c_c - 256), src_g_c_r, tag_g_c_c, tag_g_c_r))

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

    try:
        image_ = Image.fromarray(image_, mode='RGB')
        img_TK_Processed = ImageTk.PhotoImage(image_)

        canvas_processed.create_image(300, 150, image=img_TK_Processed)
    except Exception as e:
        print(e)
        return


def update(event):
    widget = event.widget
    selection = widget.curselection()
    select_item = widget.get(selection[0])
    input_img = os.path.join(input_dir, select_item)

    try:
        global Image_index

        index = 0
        for i in input_filename_list:
            if select_item in i:
                break
            index += 1

        Image_index = index

        global img_TK_Input
        global img_Input

        # input image
        image = Image.open(input_img, mode='r')
        w, h = image.size
        img_Input = image
        img_TK_Input = ImageTk.PhotoImage(image)

        canvas_original.create_image(300, 150, image=img_TK_Input)
    except Exception as e:
        return

lbox.bind("<Double-Button-1>", func=update)

while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass