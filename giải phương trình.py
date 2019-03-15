print("nhap a")
a = float(input())
print("nhap b")
b = float(input())
print("nhap c")
c = float(input())
if a == 0:
    if b != 0:
        if c == 0:
            print("phuong trinh vo nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -b / a
        print("phuong trinh co nghiem la: " + str(x))
else:
    d = b ** 2 - 4 * a * c
    if d >= 0:
        if d == 0:
            x = -b / (2 * a)
            print("phuong trinh co nghiem la: " + str(x))
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print("phuong trinh co nghiem la:" + str(x1))
            print("phuong trinh co nghiem la: " + str(x2))
    else:
        print("phuong trinh vo nghiem")
