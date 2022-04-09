import pytesseract
import numpy
import cv2
import numpy as np

from PIL import Image


class TextExtractor:
    def __init__(self, path):
        print('[TextExtractor] init TextExtractor')
        pytesseract.pytesseract.tesseract_cmd = path
        print('[TextExtractor] available language : ', pytesseract.get_languages(config=''))

    # pos = (x,y)
    def load_image(self, fname):
        return cv2.imread(fname)

    def load_image_with_pos(self, fname, pos1, pos2):
        image = cv2.imread(fname)
        return image[pos1[1]:pos2[1], pos1[0]:pos2[0]]
        #return cv2.rectangle(image, (pos1[0], pos1[1]), (pos2[0], pos2[1]), (255, 0, 0), 3)

    def parse_image(self, image):
        print('[TextExtractor] parse_image')
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # make image gray
        # (thresh, img_bw) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY) # make image B&W

        print(pytesseract.image_to_string(img_gray, lang='kor'))
        cv2.imshow('image', img_gray)
        cv2.waitKey(0)
        cv2.destroyWindow()
        # print(pytesseract.image_to_string(Image.open(image), lang='kor'))

    def compare_image(self, image1, image2):
        diff = cv2.subtract(image1, image2)
        return not np.any(diff)
