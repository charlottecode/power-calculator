base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (non-negative integer): "))

if exponent < 0:
    print("Error: Exponent must be non-negative.")
elif exponent == 0:
    print(1)  # base**0 is always 1
else:
    result = 1
    for _ in range(exponent):
        result *= base
    print(result)