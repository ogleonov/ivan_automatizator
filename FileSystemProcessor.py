from Scaler import scale_image
import os

def loadImagesToOutDir(dir):
    dirIn = os.path.join(dir, "in/")
    dirOut = os.path.join(dir, "out/")
    if not os.path.exists(dirOut):
        os.mkdir(dirOut)
    for name in os.listdir(dirIn):
        scale_image(os.path.join(dirIn, name), os.path.join(dirOut, name), 800, 600)