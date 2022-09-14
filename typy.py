# szkolenie python dzień pierwszy 14.09.2022
# komentarze
# TYPY DANYCH:
#   1.int    - liczby całkowite:  2, 34, -54, 1345
#   2.float - liczby zmiennoprzecinkowe: 5.5    zamiast przecinka zawsze kropka
#   3.complex - liczby zespolone: 3+2j -4.4j
#   4.bool - wartość logiczna False=0, True=1
# METODA=FUNKCJA
# metoda drukowania na ekranie - print
# funkcje wbudowane mają kolor fioletowy - przykłądem jest print

print("print w pythonie")
# po poprawnym uruchomieniu RUN (prawy klawisz myszy wbieramy Run... jest 0 to jest ok,
# nie ma błędów w kodzie "Process finished with exit code 0"

# SKRÓTY
# CTRL+ALT+L - formatowanie kodu
# CTRL+D     - powiela linie
# CTRL+Z     - usuwa linie
# CTRL+?     - komentuje linie, ponowne użycie odkomentuje linie


print(5 / 2) # dzielenie
print(5 // 2) # dzielenie bez reszty
print(5 * 2) # mnożenie
print(5 ** 2) #potęgowanie
print(5*2+(4*5)-43)
print(5.5*2) #wynik int*float zawsze będzie floatem
print(' * '*10)   # mnożenie tekstu
print("Hej, jestem 'Python'")  #codzysłów moze być taki w takim " lub takim ' ma znaczenie jeśli używamy "" w srodku tekstu
# 5.LISTA - [] przechowuje wszystko co chcemy, python nie ma tablic (array służy do czegoś innego),
# lista jest ulotna działa tylko w trakcie działania programu
print(['jeden','dwa','trzy','cztery',5,7.7])
# do listy dostajemy się za pomocą indeksacji od zera
#ZMIENNE - wydzielony kawałek kodu, gdzie przechowujemy wartość, zmienną zawsze z małej litery bez polskich znaków
imie = "Tomek" # w python nie ma deklaracji typów zmiennych
imie1 = 5
print(type(imie))  #pokazuje jakim typem jest zmienna
print(type(imie1))
#rzutowanie  - jak wstawić aby zmienna była takiego typu jaki chcemy rzeczywiście, mimo braku deklaracji zmiennych
imie2 = int("5") #zamienia 5 jako tekst na intigera
print(type(imie2))
# STAŁE - nie ma tego w pythonie. przy Krotkach wróci ten temat, z dużymi literami.
# Po co duże litery? żeby tego nie zmieniać, to info dla innych programistów
WIEK = 39
print(WIEK)

lista = ['jeden','dwa','trzy','cztery',[5,7.7],8,9]
print(type(lista))
#Indeksowanie listy i  wycinek listy - slajsowanie (wycinanie)
print(lista[4]) # wyswietla piaty element listy
print(lista[4][1]) # lista w liście - wielowymiarowa pokazuje drugą wartość podlisty
print(lista[0:3])  #  slajsowanie, tnie element który wskazujemy jako brzegowy po lewej stronie
print(lista[0], lista[5])    # pobieranie dwóch elementów z listy nie po sąsiedzku
print(lista[-1])   #przy sortowaniu listy najnowszy element na końcu, pobieramy oststnie wartości z listy. LIczy od tyłu
print(lista[-3:-1])
lista [0] = 1             #podmiana elementów w liście
print(lista)
#METODY NA LIŚCIE
#lista.    #metody standardowe mają tylko nazwę z __ to metody wbudowane na etapie zaawansowanym
lista.append('Tomek') #dodaje na końcu listy wartosć
print(lista)
lista.insert(2, 'Artur')  #dodaje Artura na drugim miejscu na liście
print(lista)
# lista.remove('dwa')
# print(lista)
# lista.pop(1)  usuwa po indeksie
#print(lista.count('Tomek'))  #liczy ile występuje Tomków w liście
#lista.clear() # czyści listę
print(lista)
lista.index('dwa',1,2)
print(lista)
print(len(lista))
#sortowanie listy
#listę można rzutować identycznie jak zmienną
liczby =[4,6,8,100,39,24]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
print(min(liczby))
print(max(liczby))
#nie tylko listy działają jak listy, łąńcuchy znaków też są listami, dokleimy fragment ale nie zmienimy tego co jest w "napis"
napis = "Krzysztof Kowalski"
print(napis.count("K"))
print(napis[0:5])
print(napis.capitalize())
print(napis.upper())
print(napis, 'wita', 4, 'razy') #print zmienia wszsytko na stringa - również int jakim jest 4
print(napis+'wita'+4+'razy') #print zmienia wszsytko na stringa - również int jakim jest 4 więc z + bedzie błąd
print(napis + ' wita ' + ' razy ') #print zmienia wszsytko na stringa - również int jakim jest 4 więc z + bedzie błąd









