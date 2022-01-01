# Build a weight converter that asks for input on how much you weigh then convert it to either pounds or kgs
# Next, the program will ask whether this number is specified in pounds (L) or kilograms (K)
# Weight: 72
# (L)bs or (K)g: k
# You are 160.0 pounds

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper == "L":
    converted = weight * 0.45
    print(f"you are {converted} kgs")
else:
    converted = weight / 0.45
    print(f"You are {converted} lbs")