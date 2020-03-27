import os
from os import path

import cv2


class FrameDir:
    root: str

    def __init__(self, root: str):
        self.root = root

    def len(self):
        return sum(1 for f in os.listdir(self.root) if path.splitext(f)[1] == 'jpg')

    # load a scaled, color_bgr image using the naming convention
    def load(self, frame: int):
        im = cv2.imread(path.join(self.root, f'{frame:04}.jpg'))
        # INTER_AREA: recommended for decimation
        dim = (2560 // 2, 1920 // 2)
        im = cv2.resize(im, dim, im, interpolation=cv2.INTER_AREA)
        return im
