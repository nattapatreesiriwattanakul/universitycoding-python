def pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    for i in range(n):
        print(" " * (n - i - 1), end="")
        for num in triangle[i]:
            print(num , end=" ")  
        print()  

def main():
    number = int(input("Enter the rows: "))
    pascal_triangle(number)
main()