
print("1.TOPLAMA")
print("2.ÇIKARMA")
print("3.ÇARPMA")
print("4.BÖLME")
print("-------")

secim = int(input("İşlem tipinizi seçiniz (1-4):"))


if (secim == 1):
      
    print("********************************")
    print("* Seçilen işlem TOPLAMA işlemi *")
    print("********************************")
    sayi1 = int(input("1.Sayıyı giriniz:"))
    
    sayi2=int(input("2.Sayıyı giriniz:"))
    
    sonuc = sayi1 + sayi2
    print("Sonuç={0}".format(sonuc))

elif (secim == 2):

  
    print("********************************")
    print("* Seçilen işlem ÇIKARMA işlemi *")
    print("********************************")
    sayi1 = int(input("1.Sayıyı giriniz:"))
    
    sayi2=int(input("2.Sayıyı giriniz:"))
    
    sonuc = sayi1 - sayi2
    print("Sonuç={0}".format(sonuc))


elif (secim == 3):

   
    print("********************************")
    print("* Seçilen işlem ÇARPMA işlemi *")
    print("********************************")
    sayi1 = int(input("1.Sayıyı giriniz:"))
    
    sayi2=int(input("2.Sayıyı giriniz:"))
    
    sonuc = sayi1 * sayi2
    print("Sonuç={0}".format(sonuc))

elif (secim == 4):

  
    print("********************************")
    print("* Seçilen işlem BÖLME işlemi *")
    print("********************************")
    sayi1 = int(input("1.Sayıyı giriniz:"))
    
    sayi2=int(input("2.Sayıyı giriniz:"))
    
    
    
    if (sayi2 != 0):
            sonuc = sayi1 / sayi2
            print("Sonuç={0}".format(sonuc))
    
    else:
    
        print("!!! SIFIRA BÖLME HATASI !!!")
    

else:

    print("Yanlış seçim ! Lütfen 1-4 arası seçim yapınız")


