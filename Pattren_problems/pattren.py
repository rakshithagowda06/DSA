import sys

def square_pattren(n):
    for i in range(n-1):
        for j in range(n-1):
            print("*",end=" ")
        print()

# s=square_pattren(5)
# print(s)

def pattren2(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print()
    return " "

# s2 = pattren2(5)
# print(s2)


def pattren3(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    return " "

# s3 = pattren3(5)
# print(s3)


def pattren4(n):
    for i in range(n+1):
        for j in range(0,i):
            print(i,end=" ")
        print()
    return " "

# s3 = pattren4(5)
# print(s3)

def pattren5(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print()
    return " "

# s3 = pattren5(5)
# print(s3)

def pattren6(n):
    for i in range(n,0,-1):
        for j in range(n+1,i,-1):
            print(i,end=" ")
        print()
    return ""

# s3 = pattren6(5)
# print(s3)


def pattren7(n):
    for i in range(n):
        for j in range(n,i,-1):
            print(n-j+1,end=" ")
        print()
    return " "

# s4 = pattren7(5)
# print(s4)


def pattren8(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end=" ")
        for j in range(n-i-1):
            print(" ",end="")
        print()

    return  " "

# s4 = pattren8(5)
# print(s4)

def pattren9(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")

        for j in range(n*2-(2*i+1)):
            print("*",end=" ")

        for j in range(n-i-1):
            print(" ",end="")

        print()

    return " "

# s5 = pattren9(5)
# print(s5)

class double_pyramid:
    def erect_pyramid(self,n):
        for i in range(n):
            print(" " * (n - i - 1), end="")

            print("*" * (2 * i + 1), end="")

            print(" " * (n- i - 1))

    def inverted_pyramid(self,n):
        for i in range(n):
            print(" " * i, end="")
            print("*" * (2 * n - (2 * i + 1)), end="")
            print(" " * i)




s10 = double_pyramid()
s10.erect_pyramid(5)
s10.inverted_pyramid(5)




