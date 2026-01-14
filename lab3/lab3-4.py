def fibonacci(number):
    t1 = 0
    t2 = 1
    sum = 0
    print(t1, t2, end=" ")
    for i in range(number - 2):
        sum = t1 + t2 #
        t1 = t2 #
        t2 = sum #
        print(sum, end=" ")
        print()


def main():
    number = int(input("Enter the value of 'n': "))
    print("Fibonacci Series: ")    
    fibonacci(number)
main()
