from glob import glob
from io import BytesIO
from PIL import Image, ImageDraw
from os import path
#from svglib.svglib import svg2rlg
from cairosvg import svg2png

def svg_shape_import(path):
    with open(path, "r") as svg:
        shape = svg.read()

    return shape

def svg_to_image(data, width, height):
    return Image.open(BytesIO(svg2png(data, output_width=width, output_height=height))) # https://stackoverflow.com/a/62345450

heart_svg = svg_shape_import("vendor/heart.svg")

new_filename = "export/{0}_{1}.png"

#def flag_from_svg(mask_svg, original_flag, transparent_canvas):
    
flags = glob("vendor/Zaimki/static/flags/[!_]*")
for flag_path in flags:
    flag_name = path.basename(flag_path)
    flag = Image.open(flag_path)

    # Create a transparent canvas equal to the size of the flag for the masks to base themselves on
    transparent = Image.new("RGBA", (flag.width, flag.height), (255, 255, 255, 0))

    # Copy that transparenty canvas and paste the heart svg into it, at the correct size & height
    heart_shape = transparent.copy()
    heart_shape.paste(svg_to_image(heart_svg, transparent.width, transparent.height))

    heart_flag = transparent.copy()
    heart_flag.paste(flag, mask=heart_shape)
    heart_flag.save(new_filename.format(flag_name, "heart"))
    
