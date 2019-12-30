a,b = 5,43
print("Sayıların başlangıç değeri, a = {0}, b = {1}".format(a,b))
yedek = a
a = b
b = yedek
print("Sayıların sonraki değeri, a = {0}, b = {1}".format(a,b))

## yada

a,b = b,a

print("Sayıların tekrar başlangıç değeri, a = {0}, b = {1}".format(a,b))
