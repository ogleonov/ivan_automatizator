from Scaler import scale_image
import os
from docx import Document
from initvars import dirIn
from initvars import dirOut
from initvars import dir
from initvars import docPath


def loadImagesToOutDir(dir):
    if not os.path.exists(dirOut):
        os.mkdir(dirOut)
    for name in os.listdir(dirIn):
        scale_image(os.path.join(dirIn, name), os.path.join(dirOut, name), 800, 600)


if __name__ == '__main__':
    loadImagesToOutDir(dir)
    document = Document()
    """for name in os.listdir(dirOut):
        document.add_picture(os.path.join(dirIn, name))"""

    tables = document.tables
    table = document.add_table(rows=len(os.listdir(dirOut))+1, cols=2)
    row_cells = table.add_row().cells
    i=0
    for name in os.listdir(dirOut):
        p = document.add_paragraph('Picture bullet section', 'List Bullet')
        p = p.insert_paragraph_before('')
        r = p.add_run()
        r.add_picture(os.path.join(dirOut, name))
        p = p.insert_paragraph_before('My picture title', 'Heading 1')
    document.save(docPath)
