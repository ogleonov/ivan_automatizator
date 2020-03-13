import os

dir = "C:/Users/ivan.vasilyev/Documents/Python/python_projects/automation/"
docPath = os.path.join(dir, "docs/document.docx")
dirIn = os.path.join(dir,"in/")
dirOut = os.path.join(dir, "out/")

hcm = 12.67   #12.67; 7.69; BK - 30.0
wcm = 9.5 #9.5; 10.27; BK - 12.0

pix = 37.89

height = hcm*pix
widht = wcm*pix

angle = 90
