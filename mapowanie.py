lista = [1,3,5,7]   #lamdba mnoży każdy element z listy * 2 (mapuje) x to elementy listy
print(f"Zastosowanie map z lambda:{list(map(lambda x : x * 2, lista))} ")    # f - to format w klamrach
print(f"Zastosowanie filter z lambda:{list(filter(lambda x : x > 3, lista))} ")


#funkcja wyższego rzędu  (funkcja w funkcji)

def funkcja (f, liczba):
    return f(liczba)

def dodaj_jeden(x):
    return x+1

def kwadrat(parametr):
    return parametr * parametr



print(funkcja(dodaj_jeden, 7 ))



