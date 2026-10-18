#imagine counting toys and putting them in a basket
#pattern = "" is the empty basket, for i in range(1, n + 1). pattern += str(i) + "" each time you count a number you leave a gap
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."
    pattern = " "
    for i in range(1, n + 1):
        pattern += str(i) + " "
    return pattern.strip()
print(number_pattern(4))