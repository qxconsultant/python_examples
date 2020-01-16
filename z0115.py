distance = float(input("how far from downtown (in km):"))
print('distance: {}'.format(distance))
pregenent = input("whether pregenent? (Y or N):")
print('pregenent? {}'.format(pregenent))

if distance <= 20:
    print('{} km from downtown does not be evacuated'.format(distance))
elif distance > 20 and distance <= 40:
    if pregenent == 'Y':
        print('{} km from downtown and pregenent need be evacuated now'.format(distance))
    else:
        print('{} km from downtown does not be evacuated'.format(distance))

