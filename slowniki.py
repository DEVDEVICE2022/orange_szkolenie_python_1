#słowniki lub inaczej mapy, trochę tablica mieszająca i SET-y
#jest to odpowiedznik json   składa się z dowolnego klucza i wartości
#słownik w pthon jest podstawową strukturą korzytania
#slownik1 = {}   deklaracja słownika, nie jest sortowalny a typy mogą być różne int,string, lista...
slownik1 = {1: "pierwszy",
            2: "drugi",
            3: "trzeci",
            "imie": "Tomek",
            "wiek": 39
            }
print(type(slownik1))       # typ dict
print(slownik1)
#slownik1.pop   zawsze usuwamy parę klucz i wartość, klucze nie mogą się powtarzać
print(slownik1.keys())
print(slownik1.values())
print(slownik1[2])
#ustawianie wartości klucza, a nowy wpis, klucz jest dodawany na końcu
slownik1["imie"]= "Krzysiek"
print(slownik1)
#SET - unikalność elementu w zbiorze (totolotek) tylko raz wypada liczba z 49, działa jak distinct
lotek = {1,3,1,4,5,9,5}
print(type(lotek))    #set jest jak distinct w sql
print(lotek)
print(5 in lotek) #sprawdza czy występuje w danym zbiorze, zwróci true albo false