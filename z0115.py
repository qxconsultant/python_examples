#!/usr/bin/env python

import re


def is_pregenent(input):
    return_code = False
    if re.match(r'^y.*', input, re.IGNORECASE):
        return_code = True
    print(return_code)
    return return_code


def is_digit(input):
    return_code = False
    if input.isdigit():
        print('Input "{}" is digit'.format(input))
        return_code = True
    else:
        print('Input "{}" is not digit'.format(input))
    return return_code


def main():
    distance = input("how far from downtown (in km):")
    if not is_digit(distance):
        exit(1)
    distance = float(distance)
    print('distance: {}'.format(distance))
    if distance >= 20:
        print('{} km from downtown does not be evacuated'.format(distance))
    elif distance < 20:
        pregenent = input("whether pregenent?:")
        if is_digit(pregenent):
            exit(1)
        print('pregenent? {}'.format(pregenent))
        if is_pregenent(pregenent):
            print('{} km from downtown and pregenent, you need be evacuated now'.format(distance))
        else:
            print('{} km from downtown does not be evacuated'.format(distance))


if __name__ == '__main__':
    main()
