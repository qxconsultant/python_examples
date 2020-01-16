#!/usr/bin/env python

import re


def is_pregnant(input):
    return_code = False
    # use regex with case insensitive to handle [Yy][Es][Ss] answer
    if re.match(r'^y.*', input, re.IGNORECASE):
        return_code = True
    return return_code


def is_digit(input):
    return_code = False
    # use string isdigit() to verify input is digit or string
    if input.isdigit():
        print('Input "{}" is digit'.format(input))
        return_code = True
    else:
        print('Input "{}" is not digit'.format(input))
    return return_code


def main():
    distance = input("how far from downtown (in km):")
    # ensure is digit
    if not is_digit(distance):
        # exit script with error code 1
        exit(1)
    # casting to float
    distance = float(distance)
    # use string format to print, otherwise print("distance: " + str(distance))
    print('distance: {}'.format(distance))
    if distance >= 20:
        print('{} km from downtown does not be evacuated'.format(distance))
    elif distance < 20:
        pregnant = input("whether pregnant?:")
        if is_digit(pregnant):
            exit(1)
        print('pregnant? {}'.format(pregnant))
        if is_pregnant(pregnant):
            print('{} km from downtown and pregnant, you need be evacuated now'.format(distance))
        else:
            print('{} km from downtown does not be evacuated'.format(distance))


if __name__ == '__main__':
    main()
