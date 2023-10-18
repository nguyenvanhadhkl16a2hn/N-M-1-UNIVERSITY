# tính chỉ số BMi của cơ thể
def BMI(x,y):
    bmi = x/y**2
    print("kết quả bmi của bạn là: ",bmi)
    if bmi <18.5:
        print(" và bạn đang quá gầy")
    elif bmi <24.99:
        print(" oke good bình thường")
    else:
        print(" bạn đang quá péo")
x = int(input("nhập cân nặng: "))
y = float(input("nhập chiều cao: "))
BMI(x,y)