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
        p = document.add_paragraph(name)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = p.insert_paragraph_before('')
        p.line_spacing_rule = WD_LINE_SPACING.SINGLE

        c = document.add_paragraph('[Comment]')
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER

        r = p.add_run()
        r.add_picture(os.path.join(dirOut, name))
        last_paragraph = document.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r.orientation = WD_ORIENT.PORTRAIT
        r.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p = p.insert_paragraph_before('')
     #   p = p.insert_paragraph_before(name, 'Heading 1')
    document.save(docPath)
