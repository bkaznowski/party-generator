from PIL import Image
import numpy as np
import colorsys
import glob
from blend_modes import overlay, multiply
import itertools

colours = [
    '#ffd68c', '#8cff8c', '#8cffff', '#8cb5ff', '#d68cff', '#ff8cff',
]

def replace_color_with_transaprency(img, r, g, b):
    data = img.getdata()

    newData = []
    for item in data:
        if item[0] == r and item[1] == g and item[2] == b:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    return newData

def replace_alpha_with_white(img):
    data = img.getdata()

    newData = []
    for item in data:
        if item[3] == 0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)
    return newData


def make_party_gif(filename):
    print(f'Processing {filename}')
    im = Image.open(filename).convert('LA').convert('RGBA')

    basewidth = 100
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)

    im.putdata(replace_color_with_transaprency(im, 255, 255, 255))
    # im.putdata(replace_color_with_transaprency(im, 0, 0, 0))

    background_img = np.array(im)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.

    frames = []
    for c in colours:
        layer = Image.new('RGBA', im.size, c)
        foreground_img = np.array(layer)
        foreground_img_float = foreground_img.astype(float)

        # Blend images
        opacity = 0.8
        blended_img_float = overlay(background_img_float, foreground_img_float, opacity)
        blended_img_float = multiply(blended_img_float, foreground_img_float, opacity)

        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)
        blended_img_raw = Image.fromarray(blended_img)
        blended_img_raw.putdata(replace_alpha_with_white(blended_img_raw))
        frames.append(blended_img_raw)

    frames = frames + frames[::-1]

    # Save into a GIF file that loops forever
    print(f"Saving /output_data/{filename.split('/')[-1]}.gif")
    frames[0].save(
        f"/output_data/{filename.split('/')[-1]}.gif",
        format='GIF',
        append_images=frames[1:],
        save_all=True,
        duration=100,
        loop=0
    )

filetypes = [
    '*.jpg',
    '*.jpeg',
    '*.png',
]

print('Running')
for name in list(itertools.chain.from_iterable([glob.glob(f'/input_data/{f}') for f in filetypes])):
    make_party_gif(name)
