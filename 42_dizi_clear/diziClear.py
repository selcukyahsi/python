isimler = ["Ali","Ahmet","Mehmet","Aslı","Ayşe"]
print("""Dizinin temizlenmeden önceki hali
-----------------------------------""")
for i in range(len(isimler)):
    print("{0}- {1}".format(i,isimler[i]))

isimler.pop(4)
isimler.pop(3)
isimler.pop(2)

print("""Dizinin temizlendikten sonraki hali
-----------------------------------""")
for i in range(len(isimler)):
    print("{0}- {1}".format(i,isimler[i]))
