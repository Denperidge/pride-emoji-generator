from glob import glob
from io import BytesIO
from PIL import Image
from os import path
#from svglib.svglib import svg2rlg
from cairosvg import svg2png

def svg_shape_import(path):
    with open(path, "r") as svg:
        png
        shape = Image.open(BytesIO(svg2png(svg.read()))) # https://stackoverflow.com/a/62345450

    return shape

heart_shape = svg_shape_import("vendor/heart.svg")

new_filename = "export/{0}_{1}.png"

flags = glob("vendor/Zaimki/static/flags/[!_]*")
for flag_path in flags:
    flag_name = path.basename(flag_path)
    flag = Image.open(flag_path)

    heart_flag = Image.composite(flag, flag, heart_shape)


    heart_flag.save(new_filename.format(flag_name, "heart"))
    


