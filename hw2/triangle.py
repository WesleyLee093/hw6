def classify_triangle(a: int, b: int, c: int) -> str:
    sides = (a, b, c)
    distinct_sides = set()
    for side in sides:
        if side <= 0:
            return "invalid"
        distinct_sides.add(side)
    shortest, middle, longest = sorted(sides)
    if shortest + middle <= longest:
        return "invalid"
    distinct_count = len(distinct_sides)
    if distinct_count == 1:
        return "equilateral"
    if distinct_count == 2:
        return "isosceles"
    return "scalene"
