lista = []
print("podaj liczby które chcesz wrzucić dl listy")
print("Wpisz STOP aby zakończyć program")

while True:         #hile działa Boolem - z True False
    wejscie = input("wprowadź liczbę:")
    if wejscie =='stop':
        break
    lista.append(int(wejscie))

print("Twoja lista ->", lista)


