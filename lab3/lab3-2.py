def sum_digit(number):
    total = 0
    while number > 0:
        num = number % 10
        total += num
        number //= 10
    return total


def main():
    number = int(input("Enter a number: "))
    total = sum_digit(number)
    print(f"The total sum of digits is: {total}")


main()
