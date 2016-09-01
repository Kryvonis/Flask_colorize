from PIL import Image, ImageChops


def image_overlay(src, color):
    hair = Image.open(src)
    color = [int(x) for x in color.split(',')]
    color = Image.new("RGBA", hair.size, (*color, 255))
    white = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res_mul = ImageChops.multiply(hair, color)
    res_scr = ImageChops.screen(res_mul, res_mul)
    res = Image.composite(res_scr, white, hair)
    return res


def image_color(src, color):
    hair = Image.open(src)
    color = [int(x) for x in color.split(',')]
    color = Image.new("RGBA", hair.size, (*color, 255))
    white_col = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res = Image.blend(hair, color, alpha=0.6)
    res = Image.composite(res, white_col, hair)
    return res


def image_multiply(src, color):
    hair = Image.open(src)
    color = [int(x) for x in color.split(',')]
    color = Image.new("RGBA", hair.size, (*color, 255))
    white_col = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res = ImageChops.multiply(hair, color)
    res = Image.composite(res, white_col, hair)
    return res
