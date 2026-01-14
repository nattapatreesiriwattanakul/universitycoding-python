def pattern1(num_rows):
    print("Pattern 1")
    for i in range(0, num_rows + 1):
        print(" " * (num_rows - i), "* " * i)


def pattern2(num_rows):
    print("Pattern 2")
    for i in range(0, num_rows + 1):
        print("* " * i)


def pattern3(num_rows):
    print("Pattern 3")
    for i in range(0, num_rows + +1):
        print(" " * (num_rows - i), "* " * i)


def pattern4(num_rows):
    print("Pattern 4")
    for i in range(num_rows, 0, -1):
        print(" " * (num_rows - i), "* " * i)


def pattern5(num_rows):
    print("Pattern 5")
    for i in range(0, num_rows + 1):
        num = str(i) + " "
        print(num * i)


def main():
    num_rows = int(input("Enter the number of rows: "))
    pattern1(num_rows)
    pattern2(num_rows)
    pattern3(num_rows)
    pattern4(num_rows)
    pattern5(num_rows)


main()