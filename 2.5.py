try:
    a = int(input("nhập số a: "))
    b = int(input("nhập vào số b: "))
    c = a/b
    print(c)

except ValueError:
    print(" phải nhập vào số nguyên")


except ZeroDivisionError:
    print("số b phải khác không !")