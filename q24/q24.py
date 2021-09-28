from typing import ForwardRef, List


print("fefe")

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def permutation(number: int):
    total_number: int = 1
    while number > 0:
        total_number = number * total_number
        number = number - 1

    return total_number


max_limit = 1000000
base_numbers: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
magic_number = 9
number_text: str = ""

while True:
    if len(base_numbers) == 0:
        break

    for base_number in base_numbers:
        founded = False
        max_number = permutation(magic_number)
        if max_limit > max_number:
            max_limit -= max_number
        else:
            founded = True
            break

    if founded:
        magic_number -= 1
        number_text += str(base_number)
        base_numbers.remove(base_number)

print(number_text)


# 012345678 1!
# 01234567 2!
# 0123456 3!
# 012345 4!
# 01234 5!
# 0123 6!
# 012 7!
# 01 8!
# 0 9!
# x10
