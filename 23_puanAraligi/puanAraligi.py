
n1= int(input("Birinci sınav notunu giriniz:"))

n2 = int(input("İkinci sınav notunu giriniz:"))

n3 = int(input("Üçüncü sınav notunu giriniz:"))


ort = float((n1 + n2 + n3) / 3)
print(ort)
if (ort>=0 and ort<=49):
    print("Ortalama:{0} Puan:1 Durum:Geçmez".format(ort))
elif (ort >= 50 and ort <= 59):
    printLine("Ortalama:{0} Puan:2 Durum:Geçer".format(ort))
elif (ort >= 60 and ort <= 69):
    printLine("Ortalama:{0} Puan:3 Durum:Orta".format(ort))
elif (ort >= 70 and ort <= 84):
    printLine("Ortalama:{0} Puan:4 Durum:İyi".format(ort))
elif (ort >= 85 and ort <= 100):
    printLine("Ortalama:{0} Puan5 Durum:Pekiyi".format(ort))
else:
    print("Geçersiz Ortalama ! Sınav notları 0-100 aralığında olmalı")

