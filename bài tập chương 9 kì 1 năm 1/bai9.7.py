# chương tình trả về phần nguyên của phép chia 2 số nguyên
import math as neo
def chia_lay_nguyen(x,y):
    z = x/y
    z1 = neo.floor(z)
    return z1
x = float(input("nhập số x: "))
y = float(input("nhập số y: "))
print(chia_lay_nguyen(x,y))
