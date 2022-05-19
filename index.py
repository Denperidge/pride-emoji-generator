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

flags = glob("vendor/Zaimki/static/flags/[!_]*")
for flag_path in flags:
    flag_name = path.basename(flag_path)
    flag = Image.open(flag_path)

    transparant = Image.new("RGBA", (flag.width, flag.height), (255, 255, 255, 0))


    heart_shape = transparant.copy()
    heart_shape.paste(svg_to_image(heart_svg, transparant.width, transparant.height))

    transparant.paste(flag, mask=heart_shape)



    transparant.save("test.png")

    #heart_flag = Image.composite(transparant, flag, heart_svg)


    #heart_flag.save(new_filename.format(flag_name, "heart"))
    


