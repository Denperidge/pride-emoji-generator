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

def flag_from_svg(transparent_canvas, original_flag, mask_svg):
    # Copy that transparenty canvas and paste the svg into it, at the correct size & height
    shape = transparent_canvas.copy()
    shape.paste(svg_to_image(mask_svg, transparent_canvas.width, transparent_canvas.height))

    # Create a blank image the size of the flag, and paste the flag into it, but masked
    shape_flag = transparent_canvas.copy()
    shape_flag.paste(original_flag, mask=shape)
    return shape_flag

# This glob excludes flags starting with _ & -, but this can be easily modified by modifying the glob!
flags = glob("vendor/Zaimki/static/flags/[!_,-]*")

for flag_path in flags:
    flag_name = path.splitext(path.basename(flag_path))[0]
    flag = Image.open(flag_path)

    # Create a transparent canvas equal to the size of the flag for the masks to base themselves on
    # This isn't done in the function to save processing power!
    transparent = Image.new("RGBA", (flag.width, flag.height), (255, 255, 255, 0))

    
    heart_flag = flag_from_svg(transparent, flag, heart_svg)
    heart_flag.save(new_filename.format(flag_name, "heart"))
    
