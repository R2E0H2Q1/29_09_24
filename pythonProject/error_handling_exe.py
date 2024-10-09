#write a loop that input a float height
#kep on input-ing until the float(input(..)) suceed and height is between 1.4 - 3.0

height: float = 0
while True:
    try:
        height = float(input('Please enter your height: '))
        if not 1.4 <= height <= 3.0:
            continue
        break
    except:
        print(f'The number is out of range!')

print(f'A correct height is: {height}')


