import random
rastgele = random.randint(0,100)
print(rastgele)
hak=0

while True:
    tahmin = int(input("Sayıyı yazın=")) 
    hak = hak + 1
    if hak == 5:
        print("Kaybettiniz")
        break
    else:
        if tahmin == rastgele:
            print("Tebrikler",hak ,"defada bildiniz ")
            break
        elif tahmin >  rastgele:
            print("Aşağı")
        
        else:
            print("Yukarı")
      
    
