"""
    Jesse Han
    jesse.han53@myhunter.cuny.edu
    CSCI 39534 Lab 5
    Resource: None
"""
from PIL import Image

def bitplane_decomposition(image):
    img = image.convert('L')
    width = img.size[0]
    height = img.size[1]
    pxl = img.load()
    bitplanes = [Image.new(mode='L', size=(width, height))] * 8

    for i in range(width):
        for j in range(height):
            pixel = pxl[i,j]
            for k in range(7, -1, -1):
                bitplanes[k] = 1 if pixel >= (2 ** k) else 0
                pixel = pixel - (2 ** k) if pixel >= (2 ** k) else pixel
    print(bitplanes)

fake_img = Image.new(mode='L', size=(1,1))
fake_img.load()[0,0] = 4
bitplane_decomposition(fake_img)
