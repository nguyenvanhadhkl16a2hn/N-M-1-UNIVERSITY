can = ["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỉ"]
chi = ["Thân",'Dậu',"Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
def lich_can_chi(x):
    a = x%10
    b = x%12
    return print("đây là năm",can[a],chi[b])
x = int(input("nhập năm: "))
lich_can_chi(x)
