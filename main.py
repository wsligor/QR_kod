# This is a sample Python script.
import tkinter

import os

import fitz

from typing import Tuple
from PIL import Image as ImagePIL
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def block1(img: ImagePIL, tiled_img: ImagePIL):
    # 1.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 20))

    # 1.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 20))

    # 1.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 20))

    # 1.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 20))

    # 1.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 20))

    # 1.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 20))

    # 1.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 20))

    # 1.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 20))

    # 1.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 20))

    # 1.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 20))


def block2(img, tiled_img):
    # 2.1
    crop_img = img.crop((38, 804, 170, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 110))

    # 2.2
    crop_img = img.crop((248, 804, 380, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 110))

    # 2.3
    crop_img = img.crop((458, 804, 590, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 110))

    # 2.4
    crop_img = img.crop((668, 804, 796, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 110))

    # 2.5
    crop_img = img.crop((880, 804, 1010, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 110))

    # 2.6
    crop_img = img.crop((38, 1162, 170, 1264))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 110))

    # 2.7
    crop_img = img.crop((248, 1162, 380, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 110))

    # 2.8
    crop_img = img.crop((458, 1162, 590, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 110))

    # 2.9
    crop_img = img.crop((668, 1162, 796, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 110))

    # 2.10
    crop_img = img.crop((880, 1162, 1010, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 110))


def block3(img, tiled_img):
    # 3.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 203))

    # 3.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 203))

    # 3.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 203))

    # 3.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 203))

    # 3.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 203))

    # 3.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 203))

    # 3.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 203))

    # 3.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 203))

    # 3.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 203))

    # 3.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 203))


def block4(img, tiled_img):
    # 4.1
    crop_img = img.crop((38, 804, 170, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 296))

    # 4.2
    crop_img = img.crop((248, 804, 380, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 296))

    # 4.3
    crop_img = img.crop((458, 804, 590, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 296))

    # 4.4
    crop_img = img.crop((668, 804, 796, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 296))

    # 4.5
    crop_img = img.crop((880, 804, 1010, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 296))

    # 4.6
    crop_img = img.crop((38, 1162, 170, 1264))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 296))

    # 4.7
    crop_img = img.crop((248, 1162, 380, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 296))

    # 4.8
    crop_img = img.crop((458, 1162, 590, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 296))

    # 4.9
    crop_img = img.crop((668, 1162, 796, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 296))

    # 4.10
    crop_img = img.crop((880, 1162, 1010, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 296))


def block5(img, tiled_img):
    # 5.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 390))

    # 5.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 390))

    # 5.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 390))

    # 5.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 390))

    # 5.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 390))

    # 5.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 390))

    # 5.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 390))

    # 5.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 390))

    # 5.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 390))

    # 5.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 390))


def block6(img, tiled_img):
    # 6.1
    crop_img = img.crop((38, 804, 170, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 483))

    # 6.2
    crop_img = img.crop((248, 804, 380, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 483))

    # 6.3
    crop_img = img.crop((458, 804, 590, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 483))

    # 6.4
    crop_img = img.crop((668, 804, 796, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 483))

    # 6.5
    crop_img = img.crop((880, 804, 1010, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 483))

    # 6.6
    crop_img = img.crop((38, 1162, 170, 1264))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 483))

    # 6.7
    crop_img = img.crop((248, 1162, 380, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 483))

    # 6.8
    crop_img = img.crop((458, 1162, 590, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 483))

    # 6.9
    crop_img = img.crop((668, 1162, 796, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 483))

    # 6.10
    crop_img = img.crop((880, 1162, 1010, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 483))


def block7(img, tiled_img):
    # 7.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 576))

    # 7.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 576))

    # 7.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 576))

    # 7.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 576))

    # 7.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 576))

    # 7.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 576))

    # 7.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 576))

    # 7.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 576))

    # 7.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 576))

    # 7.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 576))


def block8(img, tiled_img):
    # 8.1
    crop_img = img.crop((38, 804, 170, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 669))

    # 8.2
    crop_img = img.crop((248, 804, 380, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 669))

    # 8.3
    crop_img = img.crop((458, 804, 590, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 669))

    # 8.4
    crop_img = img.crop((668, 804, 796, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 669))

    # 8.5
    crop_img = img.crop((880, 804, 1010, 936))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 669))

    # 8.6
    crop_img = img.crop((38, 1162, 170, 1264))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 669))

    # 8.7
    crop_img = img.crop((248, 1162, 380, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 669))

    # 8.8
    crop_img = img.crop((458, 1162, 590, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 669))

    # 8.9
    crop_img = img.crop((668, 1162, 796, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 669))

    # 8.10
    crop_img = img.crop((880, 1162, 1010, 1294))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 669))


def block9(img, tiled_img):
    # 9.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 762))

    # 9.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 762))

    # 9.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 762))

    # 9.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 762))

    # 9.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 762))

    # 9.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 762))

    # 9.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 762))

    # 9.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 762))

    # 9.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 762))

    # 9.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 762))


def block10(img, tiled_img):
    # 10.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 856))

    # 10.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 856))

    # 10.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 856))

    # 10.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 856))

    # 10.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 856))

    # 10.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 856))

    # 10.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 856))

    # 10.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 856))

    # 10.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 856))

    # 10.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 856))


def block11(img, tiled_img):
    # 11.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 949))

    # 11.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 949))

    # 11.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 949))

    # 11.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 949))

    # 11.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 949))

    # 11.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 949))

    # 11.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 949))

    # 11.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 949))

    # 11.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 949))

    # 11.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 949))


def block12(img, tiled_img):
    # 12.1
    crop_img = img.crop((38, 88, 170, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (10, 1042))

    # 12.2
    crop_img = img.crop((248, 88, 380, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (90, 1042))

    # 12.3
    crop_img = img.crop((458, 88, 590, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (170, 1042))

    # 12.4
    crop_img = img.crop((668, 88, 798, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (250, 1042))

    # 12.5
    crop_img = img.crop((880, 88, 1010, 220))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (330, 1042))

    # 12.6
    crop_img = img.crop((38, 446, 170, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (410, 1042))

    # 12.7
    crop_img = img.crop((248, 446, 380, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (490, 1042))

    # 12.8
    crop_img = img.crop((458, 446, 590, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (570, 1042))

    # 12.9
    crop_img = img.crop((668, 446, 800, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (650, 1042))

    # 12.10
    crop_img = img.crop((880, 446, 1010, 576))
    new_crop_img = crop_img.resize((60, 60))
    tiled_img.paste(new_crop_img, (730, 1042))


def convert_pdf2img(input_file: str, pages: Tuple = None):
    """Преобразует PDF в изображение и создает файл за страницей"""
    # Open the document

    pdf_in = fitz.open(input_file)
    output_files = []
    i = 0
    # Полистаем страницы
    for page in pdf_in:
        i += 1
        if str(pages) != str(None):
            if str(page) not in str(pages):
                continue
        # Выберем страницу
        # rotate = int(0)
        # PDF Страница конвертируется в целое изображение 1056 * 816, а затем для каждого изображения делается снимок экрана.
        # zoom = 1.33333333 -----> Размер изображения = 1056 * 816
        # zoom = 2 ---> 2 * Разрешение по умолчанию (текст четкий, текст изображения плохо читается) = маленький размер файла/размер изображения = 1584 * 1224
        # zoom = 4 ---> 4 * Разрешение по умолчанию (текст четкий, текст изображения плохо читается) = большой размер файла
        # zoom = 8 ---> 8 * Разрешение по умолчанию (текст четкий, текст изображения читается) = большой размер файла
        zoom_x = 2.08
        zoom_y = 2.08
        # Коэффициент масштабирования равен 2, чтобы текст был четким
        # Pre-rotate - это вращение при необходимости.
        mat = fitz.Matrix(zoom_x, zoom_y)  # .preRotate(rotate)
        # pix = page.getPixmap(matrix=mat, alpha=False)
        output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}{i}.jpg"
        pix = page.get_pixmap(matrix=mat)
        # pix.writePNG(output_file)
        pix.save(output_file)
        output_files.append(output_file)
    pdf_in.close()
    # summary = {
    #    "Исходный файл": input_file, "Страниц": str(pages), "Выходной файл(ы)": str(output_files)
    # }
    # Printing Summary
    # print("#### Отчет ########################################################")
    # print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    # print("###################################################################")
    return output_files


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    tiled_size = (800, 1120)
    tiled_img = ImagePIL.new('RGB', tiled_size, (250, 250, 250))

    filename = 'order1.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block1(img, tiled_img)
    block2(img, tiled_img)

    img.close()

    filename = 'order2.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block3(img, tiled_img)
    block4(img, tiled_img)

    img.close()

    filename = 'order3.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block5(img, tiled_img)
    block6(img, tiled_img)

    img.close()

    filename = 'order4.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block7(img, tiled_img)
    block8(img, tiled_img)

    img.close()

    filename = 'order5.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block9(img, tiled_img)
    block10(img, tiled_img)

    img.close()

    filename = 'order6.jpg'
    img = ImagePIL.open(filename)
    img.load()

    block11(img, tiled_img)
    block12(img, tiled_img)

    img.close()

    tiled_img.save('tiled_img.png', 'PNG')
    tiled_img.close()

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.title = "QR kod"
    file = filedialog.askopenfilename(filetypes=(('PDF', '*.pdf'), ('PDF', '*.pdf')))
    convert_pdf2img('order.pdf')
    print_hi('PyCharm')
    canvas = tkinter.Canvas(window, height=600, width=800)
    image = ImagePIL.open('tiled_img.png')
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.grid(row=1, column=1)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
