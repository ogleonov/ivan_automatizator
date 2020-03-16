import os

homeDir = "C:\\Users\\Oleg\\PycharmProjects\\ImageProcessing\\ivan_automatizator"
docPath = os.path.join(homeDir, "docs\\document.docx")
dirIn = os.path.join(homeDir,"in\\")
dirOut = os.path.join(homeDir, "out\\")

hcm = 12.67   #12.67; 7.69; BK - 30.0
wcm = 9.5 #9.5; 10.27; BK - 12.0

pix = 37.89

height = hcm*pix
widht = wcm*pix

angle = 90
