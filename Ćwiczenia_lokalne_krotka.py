bool(())
krotka = (1, True, 2.0, 'String', [])


print(len(krotka))

print(krotka.index('String'))

print(krotka[2])

print(krotka[1:3])

print(krotka[0:-1:2])

print(krotka[::-1])

krotka_liczb = (13,9,27,14,15)

print(max(krotka_liczb))

print(min(krotka_liczb))

print(sum(krotka_liczb))

print(krotka_liczb)
print(sorted(krotka_liczb))



krotka_stringow =  ('c', 'd', 'b', 'e', 'a')

print(max(krotka_stringow))

print(min(krotka_stringow))


print(krotka_stringow)
print(sorted(krotka_stringow))


for string in krotka_stringow: print(string)
for i in range(len(krotka_stringow)): print(krotka_stringow[i])



