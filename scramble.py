#!/usr/bin/env python3

import numpy as np
import math, time, sys
from PIL import Image
from arnold import Arnold

def main(argv):
    image_name = "lena_grayscale_8bit.gif"
    image_path = "images/" + image_name

    # Arnold Transform Parameters
    a = 6
    b = 40
    rounds = 33

    # Open the images
    lena = np.array(Image.open(image_path).convert("L"))

    print(" ~~~~~~  * PARAMETERS *  ~~~~~~ ")
    arnold = Arnold(a, b, rounds)
    print("\ta:\t", a)
    print("\tb:\t", b)
    print("\trounds:\t", rounds)

    print("\n ~~~~~~  *  RESULTS   *  ~~~~~~ ")
    
    start_time = time.time()
    scrambled = arnold.applyTransformTo(lena)
    exec_time = time.time() - start_time
    print("Transform  execution time: %.6f " % exec_time, "sec")
    im = Image.fromarray(scrambled).convert("L")
    im.save("scrambled.tif", format="TIFF")

    start_time = time.time()
    reconstructed = arnold.applyInverseTransformTo(scrambled)
    exec_time = time.time() - start_time
    print("Inverse T. execution time: %.6f " % exec_time, "sec")
    im = Image.fromarray(reconstructed).convert("L")
    im.save("reconstructed.tif", format="TIFF")

    counter = 0
    for i in range(scrambled.shape[0]):
        for j in range(scrambled.shape[0]):
            if(lena[i, j] != reconstructed[i, j]):
                print(lena[i, j], " != ", reconstructed[i, j])
                counter += 1
    print("\nDIFFERENT PIXELS\n\toriginal  VS reconstructed:\t\t", counter)


if __name__ == "__main__":
    main(sys.argv[1:])