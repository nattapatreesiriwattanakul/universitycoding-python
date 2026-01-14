def biggesst_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    elif num3 > num1 and num3 > num2:
        largest = num3
    return largest


def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    largest = biggesst_number(num1, num2, num3)
    print(f"The largest number is {largest}")


main()
