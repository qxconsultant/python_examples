"""
a simple python script to generate loto numbers
"""

from random import randint


def get_numbers(item_number, max_number):
    numbers = []
    while len(numbers) < item_number:
        number = randint(1, max_number)
        if number not in numbers:
            numbers.extend([number])
    return sorted(numbers)


def main():
    print('{}\n{}\n{}\n{}\n'.format('loto max:'.upper(), get_numbers(7, 50), get_numbers(7, 50), get_numbers(7, 50)))
    print('{}\n{}\n'.format('loto 649:'.upper(), get_numbers(6, 49)))
    print('{}\n{}\nbonus:\n{}'.format('loto grandvie:'.upper(), get_numbers(5, 49), randint(1, 7)))


if __name__ == '__main__':
    main()
