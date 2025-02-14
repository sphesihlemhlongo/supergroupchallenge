def is_magical_potion(power):
    cube_root = round(power ** (1/3))
    return "YES" if cube_root ** 3 == power else "NO"

# Test Cases
print(is_magical_potion(27))  # YES
print(is_magical_potion(30))  # NO
print(is_magical_potion(1))   # YES
print(is_magical_potion(132651201231))  # ?
