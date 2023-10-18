def A(n,x):
    a = ((x**2 + x + 1)**n) + ((x**2 - x + 1)**n)
    print("gia trị của biểu thức là: ",a)
n = int(input("nhập giá trị n: "))
x = int(input("nhập giá trị x: "))
A(n,x)