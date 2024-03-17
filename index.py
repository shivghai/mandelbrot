from PIL import Image
from viewport import Viewport
from mandelbrot_set import MandelbrotSet
import matplotlib.cm as colormap

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        c = complex(pixel)
        stability =  mandelbrot_set.stability(c, smooth=smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        paletteList = palette[index % len(palette)]
        pixel.color = (paletteList[0], paletteList[1], paletteList[2])

def denormalize_color_palette(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

if __name__ == "__main__":
    mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)
    width, height = 512, 512
    scale = 0.0075
    RGB = "RGB"
    image = Image.new(mode=RGB, size=(width, height))

    palette = denormalize_color_palette(colormap.get_cmap("twilight_shifted").colors)
    
    paint(mandelbrot_set=mandelbrot_set, viewport=Viewport(image, center=-0.7435 + 0.1314j, width=0.002), palette=palette, smooth=True)
    image.show()