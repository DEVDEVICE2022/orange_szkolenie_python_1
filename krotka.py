#krotka jest niezbędna, musi mieś jeden minimanie, zawiera dowolne elementy, krotkę można użyc jako stałą,
#zbiór do przechowywania różnych wartości

krotka = (1,4,55,56,33)
krotka2 = ()
#krotka3 = (4) # to bład jako typ pojawi się typ int zamiast tuple
krotka3 = (4,) #aby była poprawnie rozpoznawana musi być przecinek
print (type(krotka))
print (type(krotka2))
print (type(krotka3))
print(krotka[1])  #z każdej krotki pobierzemy po indeksie można też min max oraz inne porównywawcze LEN, operatory (+,*...) nigdy nie można zmienić zawartości krotki
#można zmodyfikować krotkę poprzez rzutowanie np na listę
x = list(krotka2)  #rzutowanie na listę
x.append(35)   #lista na krotkę
print(x)
krotka4 = tuple(x) # kopia krotki 2
print(krotka4)

