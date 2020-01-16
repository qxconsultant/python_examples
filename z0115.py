#!/usr/bin/env python

def is_pregenent(input):
    return_code = False
    if input == 'Y':
        return_code = True
    return return_code


def main():
    distance = float(input("how far from downtown (in km):"))
    print('distance: {}'.format(distance))
    if distance >= 20:
        print('{} km from downtown does not be evacuated'.format(distance))
    elif distance < 20:
        pregenent = input("whether pregenent? (Y or N):")
        print('pregenent? {}'.format(pregenent))
        if is_pregenent(pregenent):
            print('{} km from downtown and pregenent, you need be evacuated now'.format(distance))
        else:
            print('{} km from downtown does not be evacuated'.format(distance))


if __name__ == '__main__':
    main()
