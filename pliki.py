#obsługa plików - open,   hendler - zmienna, uchwyt
# open działa z hendlerem
# uchwyt go łapie i nie puszcza dopóki go nie puścimy
# ścieżka - wystarczy nazwa pliku

# uchwyt1 = open('C:\Users\Surmapi1\notatki\plik.txt')  # litera r informuje aby python brał ścieżkę a nie znaki specjalne
# uchwyt2 = open(r'C:\Users\Surmapi1\notatki\plik.txt')  # litera r informuje aby python brał ścieżkę a nie znaki specjalne
# uchwyt3 = open('C:\Users\Surmapi1\\notatki\plik.txt')  # lub podwójne slashe
# trzeba też podać modyfikator   r-odczyt(read) a-dopisz (append), w-zapisz(write)-zapisuje plik od nowa
# uchwyt = open('plik.txt','r')
# n coding  -strona kodowa

uchwyt = open('plik.txt','r',encoding='utf-8')
dane = uchwyt.read()
print(dane)
uchwyt.close()    #uwalnianie uchwytu, musimy to zrobić
# duze pliki powinny być otwierane pandasem


lista = ['Tomek','Marcin', 'Krzysiek','Żaneta']
uchwyt = open('plik.txt','r',encoding='utf-8')
# for i in lista:
#     uchwyt.write(i)
#     uchwyt.write("\n")
#     print(i)
print(dane)

uchwyt.close()    #uwalnianie uchwytu, musimy to zrobić
# duze pliki powinny być otwierane np pandasem

#with open ('plik.txt','r',encoding='utf-8') as odczyt:   # with open nei ma closa, zamykany jest po operacji with
    # for i in odczyt:
    #     print(i)

# otwieranie pliku to tez sprawdzenie  ilości słów

#tworzenie pliku txt
with open ('plik2.txt','w',encoding='utf-8') as zapis:
    zapis.write("Tutaj nowe informacje")

