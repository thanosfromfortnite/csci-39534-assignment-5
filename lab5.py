"""
    Jesse Han
    jesse.han53@myhunter.cuny.edu
    CSCI 39534 Lab 5
    Resource: None
"""
from PIL import Image

output_dir = "output/"

def bitplane_decomposition(image):
    img = image.convert('L')
    width = img.size[0]
    height = img.size[1]
    pxl = img.load()

    for k in range(7, -1, -1):
        out = Image.new(mode='L', size=(width, height))
        out_pxl = out.load()

        for i in range(width):
            for j in range(height):
                out_pxl[i,j] = 255 if pxl[i,j] >= (2 ** k) else 0
                pxl[i,j] = pxl[i,j] - (2 ** k) if pxl[i,j] >= (2 ** k) else pxl[i,j]

        out.save(f"{output_dir}{k}.png")

image = Image.open('dog.png')
bitplane_decomposition(image)
