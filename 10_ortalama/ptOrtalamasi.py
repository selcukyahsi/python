print("Programlama Temelleri Dersi Ortalama Hesaplama")

not1 = int(input("1. not = "))
not2 = int(input("2. not = "))
not3 = int(input("3. not = "))

ort = (not1+not2+not3) /3
print("Ortalamanız = {0:.2f}".format(ort))
if ort >=50:
    print("Tebrikler")
else:
    print("Kaldınız")
    

