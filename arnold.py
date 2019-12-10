import numpy as np
from PIL import Image

class Arnold:

    def __init__(self, a:int, b:int, rounds:int):
        # Parameters
        self.__a = a
        self.__b = b
        self.__rounds = rounds

    def mapping(self, s:np.shape):
        x, y = np.meshgrid(range(s[0]), range(s[0]), indexing="ij")
        xmap = (self.__a*self.__b*x + x + self.__a*y) % s[0]
        ymap = (self.__b*x + y) % s[0]
        return xmap, ymap

    def inverseMapping(self, s:np.shape):
        x, y = np.meshgrid(range(s[0]), range(s[0]), indexing="ij")
        xmap = (x - self.__a*y) % s[0]
        ymap = (-self.__b*x + self.__a*self.__b*y + y) % s[0]
        return xmap, ymap

    def applyTransformTo(self, image:np.ndarray):
        xm, ym = self.mapping(image.shape)
        img = image
        for r in range(self.__rounds):
            img = img[xm, ym]
        return img

    def applyInverseTransformTo(self, image:np.ndarray):
        xm, ym = self.inverseMapping(image.shape)
        img = image
        for r in range(self.__rounds):
            img = img[xm, ym]
        return img