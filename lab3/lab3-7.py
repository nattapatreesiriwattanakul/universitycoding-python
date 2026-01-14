def pattern1():
    print("Pattern 1:")
    char = ""
    for i in range(65, 70):
        char += chr(i)
        print(char)


def pattern2():

    print("Pattern 2:")
    for i in range(65, 70):
        for j in range(i, i + (i - 64)):
            print(chr(j), end="")
        print()


def pattern3():
    print("Pattern 3:")
    name = input("Enter your name: ")
    char = ""
    for i in name:
        char += i
        print(char)


def pattern4():
    print("Pattern 4:")
    num_rows = int(input("Enter the row: "))
    for i in range(num_rows, 0, -1):
        space = " " * (num_rows - i)
        print(space, end="")
        for j in range(65, 65 + (2 * i - 1)):
            print(chr(j), end="")
        print()


def pattern5():
    print("Pattern 5:")
    n = 5
    for i in range(0, n):
        space = " " * (n - i)
        print(space, end="")
        for j in range(65, 65 + (2 * i - 1)):
            print(chr(j), end="")
        print()

    for i in range(n, 0, -1):
        space = " " * (n - i)
        print(space, end="")
        for j in range(65, 65 + (2 * i - 1)):
            print(chr(j), end="")
        print()


def main():
    pattern1()
    pattern2()
    pattern3()
    pattern4()
    pattern5()


main()