# Valid domain: integer x; y is one of 10, 20, 30.
# The output specification is defined in hw6/REPORT.md.
def F(x: int, y: int) -> int:
    scaled = y // 10
    if x < 0:
        weight = -1
    elif x == 1:
        weight = 0
    elif x == 1:
        weight = 1
    elif x == 2:
        weight = 2
    else:
        weight = 3
    result = weight * scaled
    return result
