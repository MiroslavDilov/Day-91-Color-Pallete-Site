from colorthief import ColorThief


def pallete_finder(path):
    img = ColorThief(path)

    return img.get_palette()

