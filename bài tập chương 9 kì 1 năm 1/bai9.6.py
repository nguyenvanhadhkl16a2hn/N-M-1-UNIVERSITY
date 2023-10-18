def kiem_tra_so_nguyen_to(n):
    a = 1
    if (n <2):
        a = 0
        return a  

    for p in range(2, n):
        if n % p == 0:
            a = 0
            break 
    return a

n = int(input("nhap so tu nhien: "))
b = kiem_tra_so_nguyen_to(n)

if b == 1:
    print(n," la so nguyen to")
else:
    print(n,"khong phai so nguyen to")

