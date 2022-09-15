# # lista = []
# # print("podaj liczby które chcesz wrzucić dl listy")
# # print("Wpisz STOP aby zakończyć program")
# #
# # while True:         #wile działa Boolem - z True False
# #     wejscie = input("wprowadź liczbę:")
# #     if wejscie =='stop':
# #         break
# #     lista.append(int(wejscie))
# #
# # print("Twoja lista ->", lista)
#
#
#
# # pętla for - DLA  z góry określonych czynności, z góry musimy coś sprawdzić, konkretnie musi mieć pokaznae grdzie
# # ma grzebnąć i ile razy - iterator jest przydatny
#
#
# lista2 = [4,5,6]
# # iterator to litera i - to chwilowa zmienna tylko na potrzeby przejścia przez element np listę
# for i in lista2:
#     print("Element listy:", i)
#
# slownik = {"imie":"MArek", "nazwisko":"KOwalski"}
# for i  in slownik:
#     print(i)
#
# # items - pary      key, val - klucze i wartości
# #e numeracja - efekt wypakowania elemenów listy, wybiera elementy i dopasowuje je do indeksu
#
# lista3 = [4,5,6]
# # iterator to litera i - to chwilowa zmienna tylko na potrzeby przejścia przez element np listę
# for i,j in enumerate(lista3):
#     print("indeks",i, "element",j)

# czasami chcemy aby instrukcja for wykonałą się na pewnym zasięgu - do tego służy range. MOnna go ustawić na trzy wartości start i stop
# range daje nam kontrolę nad sekwencjami, potrafi pracować listami i za pomocą range dodaje do listy


#for i in range(5):  # lub
#for i in range(1,4):  # lub
# for i in range(1, 6, 2):     # xyz  xy wartości brzegowe, z krok, step co druga wartość, range potrafi biegać po liście.
#     print(i)

x=[1,3,-7,9,-4,4]
for i in range(len(x)):     #len - długość ciągu, range bez lena na liście nie zadziała bo traktuje listę jako obiekt a nie jako int.
    if x[i] < 0:
        print("znaleziono liczbę ujemną na pozycji", i)

print(list(range(3,7)))   #wynik - lista [3,4,5,6,7]

#comprehension (generatory)

y = [ i for i in range(3,7)]       # comprehensive - generujemy listę za pomocą range, bez pierwszego i nie zadziałą
print(y)

z = ["2","45","55","5"]
liczby = [int(i) for i in z]
print(liczby)
#liste przerabiamy na zbiór za pomocą comprehension
zbior = [1,2,3,4,5,6,6,6,]          # zbior {} to lista z niepowtarzającymi się wartościami
zbior2 = {i for i in zbior}       # i for i in.... - to w całości comprehensive, (składanie)  wszystko dzieje się w pierwszym i np int(i), i*2... ma się mieścic w jednej lini
print(zbior2)







