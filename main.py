import os

from docx import Document

from Scaler import scale_image
from initvars import dir
from initvars import dirIn
from initvars import dirOut
from initvars import docPath
from initvars import height
from initvars import widht


def loadImagesToOutDir(dir):
    if not os.path.exists(dirOut):
        os.mkdir(dirOut)
    for name in os.listdir(dirIn):
        scale_image(os.path.join(dirIn, name), os.path.join(dirOut, name), widht, height)


if __name__ == '__main__':
    loadImagesToOutDir(dir)
    document = Document()

    for name in os.listdir(dirOut):
        p = document.add_paragraph(name, 'List Bullet')
        p = p.insert_paragraph_before('')
        r = p.add_run()
        r.add_picture(os.path.join(dirOut, name))
        p = p.insert_paragraph_before(name, 'Heading 1')
    document.save(docPath)
