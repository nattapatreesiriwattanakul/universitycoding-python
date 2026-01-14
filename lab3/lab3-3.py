def perfect_number(number):
    sum_digit = 0
    for i in range(1, number):
        if (number % i) == 0:
            sum_digit += i

    if sum_digit == number: #
        print(f"{sum_digit} Number is Perfect Number.")
    else:
        print(f"{sum_digit} Number is Not a Perfect Number.")
  
def main():
    number = int(input("Please Enter any Number: "))
    perfect_number(number)

main()