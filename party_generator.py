from PIL import Image
import numpy as np
import colorsys
import glob
from blend_modes import overlay, multiply

colours = [
    '#ffd68c', '#8cff8c', '#8cffff', '#8cb5ff', '#d68cff', '#ff8cff',
]

def make_party_gif(filename):
    print(f'Processing {filename}')
    im = Image.open(filename).convert('RGBA')
    background_img = np.array(im)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.

    frames = []
    for c in colours:
        layer = Image.new('RGBA', im.size, c)
        foreground_img = np.array(layer)
        foreground_img_float = foreground_img.astype(float)

        # Blend images
        opacity = 0.7
        blended_img_float = overlay(background_img_float, foreground_img_float, opacity)
        blended_img_float = multiply(blended_img_float, foreground_img_float, opacity)

        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)
        blended_img_raw = Image.fromarray(blended_img)
        frames.append(blended_img_raw)

    frames = frames + frames[::-1]

    # Save into a GIF file that loops forever
    print(f"Saving /output_data/{filename.split('/')[-1]}.gif")
    frames[0].save(
        f"/output_data/{filename.split('/')[-1]}.gif",
        format='GIF',
        append_images=frames[1:],
        save_all=True,
        duration=200,
        loop=0
    )

print('Running')
for name in glob.glob('/input_data/*.jpg'):
    make_party_gif(name)
