from glob import glob
from io import BytesIO
from PIL import Image
from os import path
from cairosvg import svg2png


def svg_to_image(data, width, height):
    return Image.open(BytesIO(svg2png(data, output_width=width, output_height=height))) # https://stackoverflow.com/a/62345450

def filename_no_ext(original_path):
    return path.splitext(path.basename(original_path))[0]

# Import all svgs
shape_paths = glob("shapes/*.svg")
shapes = dict()
for shape_path in shape_paths:
    shape_name = filename_no_ext(shape_path)

    with open(shape_path, "r") as shape_svg_data:
        shapes[shape_name] = shape_svg_data.read()
    


def flag_from_svg(transparent_canvas, original_flag, mask_svg, mask_name):
    # Copy that transparenty canvas and paste the svg into it, at the correct size & height
    shape = transparent_canvas.copy()
    shape.paste(svg_to_image(mask_svg, transparent_canvas.width, transparent_canvas.height))

    # Create a blank image the size of the flag, and paste the flag into it, but masked
    shape_flag = transparent_canvas.copy()
    shape_flag.paste(original_flag, mask=shape)

    shape_flag.save("export/{0}_{1}.png".format(flag_name, mask_name))

# This glob excludes flags starting with _ & -, but this can be easily modified by modifying the glob!
flags = glob("vendor/Zaimki/static/flags/[!_,-]*")

for flag_path in flags:
    flag_name = filename_no_ext(flag_path)
    flag = Image.open(flag_path)

    # Create a transparent canvas equal to the size of the flag for the masks to base themselves on
    # This isn't done in the function to save processing power!
    transparent = Image.new("RGBA", (flag.width, flag.height), (255, 255, 255, 0))

    for shape_name in shapes:
        flag_from_svg(transparent, flag, shapes[shape_name], shape_name)

    
