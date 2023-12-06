def area_or_perimeter(l: int, w: int) -> int:
    return l * w if l == w else (l + w) * 2


print(area_or_perimeter(4, 4))
# 16
print(area_or_perimeter(6, 10))
# 32
