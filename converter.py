def rgb_to_hex(rgb_list):
    new_array = []

    for rgb in rgb_list:
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        print(('{:X}{:X}{:X}').format(r, g, b))