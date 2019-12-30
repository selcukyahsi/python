s1 = int(input("Birinci sayı="))
s2 = int(input("İkinci sayı="))

if s1>s2:
    print("{}>{}".format(s1,s2))
elif s1<s2:
    print("{}<{}".format(s1,s2))
else:
    print("{}={}".format(s1,s2))
