import colorgram

colors = colorgram.extract('hirst_painting.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    combination = (r, g, b)
    rgb_colors.append(combination)

print(rgb_colors)