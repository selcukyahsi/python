import random
toplam = 0

for i in range(5):
    rastgele = random.randint(1,100)
    print(i+1,".üretilen sayı =",rastgele)
    toplam = toplam + rastgele
print("Sayıların toplamı = ",toplam)
