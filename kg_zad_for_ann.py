a=int(input("Введите число: "))
if (a%10==2 or a%10==3 or a%10==4) and (a%100!=12 and a%100!=13 and a%100!=14):
    print(a, "килограмма")
elif a%10==1 and a%100!=11:
    print(a, "килограмм")
else:
    print(a, "килограммов")