## Python'da switch-case yoktur

sayi = islem = kare = kup = 0

sayi = int(input("Bir sayı girin ="))

islem = int(input("Bir işlem seç (1-Kare 2-Küp) = "))

if islem == 1:
    kare = sayi * sayi
    print("{0} sayısının karesi= {1}".format(sayi,kare))
elif islem ==2:
    kup = sayi * sayi * sayi
    print("{0} sayısının küpü = {1}".format(sayi,kup))
else:
    print("Hatalı seçim")
    
    

