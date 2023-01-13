from createbeds import Bed

beds = []

while True:
    name = input('What is the bed name? Enter "done" if finished:')
    if name == 'done':
        break
    try:
        length = int(input('What is the length of the bed? (in feet): '))
        width = int(input('What is the width of the bed? (in feet): '))
        depth = int(input('What is the depth of the bed? (in inches): '))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue
    sun = input('Does the bed have shade, partial, or full sun?: ')
    drainage = input
