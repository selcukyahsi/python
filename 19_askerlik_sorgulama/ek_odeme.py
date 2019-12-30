medeni = str(input("Evli-Bekar ?(e,b) ="))
if medeni == "e":
    cocuk = int(input("Çocuk sayısı = "))
    if cocuk >0:
        ekOdeme = 220 + (cocuk * 50)
        print("Evli ve {0} çocuklu ek ödemesi = {1}".format(cocuk,ekOdeme))
    else:
        print("Evli ve çocuksuz ek ödemesi = 220")
else:
    print("Bekar ek ödemesi = 200 ")
    
    
        
