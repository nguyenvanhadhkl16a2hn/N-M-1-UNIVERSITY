def kiem_tra_so_hoan_hao(x):
    a = 0
    for i in range(1,x+1):
        if x%i == 0:
            a +=i
            if a == x:
                print("đây là số hoàn hảo")
                break
    else:
        print("đây không phải số hoàn hảo")
x = int(input("nhập số bạn muốn kiểm tra: "))
kiem_tra_so_hoan_hao(x)