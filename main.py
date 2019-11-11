from FileSystemProcessor import walk
from Scaler import scale_image
import os
import docx

def loadImagesToOutDir(dir):
    dirIn = os.path.join(dir, "in/")
    dirOut = os.path.join(dir, "out/")
    if not os.path.exists(dirOut):
        os.mkdir(dirOut)
    for name in os.listdir(dirIn):
        scale_image(os.path.join(dirIn, name), os.path.join(dirOut, name), 800, 600)

if __name__ == '__main__':
    dir = "C:/Users/Oleg/PycharmProjects/ImageProcessing/ivan_automatizator/"
    loadImagesToOutDir(dir)
    
