def cal_bricks(area, l, h):
    l /= 12
    h /= 12
    return area // (l * h)


wall_area = 70 * 10 * 3 + 30 * 10 * 4
print("Area   :", wall_area)
bricks = cal_bricks(wall_area, 10, 4)  # feet², inch, inch
unit_price = 83
print("Bricks :", bricks)
print("Cost   :", bricks * unit_price)
