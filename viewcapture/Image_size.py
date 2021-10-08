
from minecart.content import Shape
from PIL import Image

pdffile = open(r"C:\Users\ericsonm\Documents\GitHub\mcericson.github.io\Movie Maker\Oriented_Ellipse_tori_019.pdf", encoding="Latin-1")
doc = minecart.Document(pdffile)

page = doc.get_page(1)
for shape in page.shapes.iter_in_bbox(0,0,1000,1000):
    print("yes")
