# positive = True
# x
# |___(grid_x, grid_y)
# |  /|
# |/  |
# 0-------y
#
#
# positive = False
# x
# |___(grid_x, grid_y)
# |\  |
# |  \|
# 0-------y
#
# Quad always bind to grid
#
#   Upper triangle
#      |
#      v
#  ___________________
# |                  /|
# |                /  |
# |              /    |
# |            /      |
# |          /        |
# |        /          |
# |      /            | <-- Lower triangle
# |    /              |
# |  /                |
# |/                  |
# ---------------------

def is_in_upper(grid_x: float, grid_y: float, x: float, y: float, positive: bool) -> bool:
    x = (x % grid_x) / grid_x
    y = (y % grid_y) / grid_y
    if not positive:
        x = 1 - x
    return y > x

grid_x = float(input("Grid X: "))
grid_y = float(input("Grid Y: "))
x = float(input("X: "))
y = float(input("Y: "))
pos = bool(int(input("Is quad 'positive'? (0 or 1):")))

res = is_in_upper(grid_x, grid_y, x, y, pos)
print(f"In upper triangle: {res}")
