pi = 3.14  # pi jest zmienną globaną, bo jest wyciągnięta poza definicje


#funkcje   #dogstring

# funkcja/metoda. funkcja żyje w kodzie jako oddzielna część. Metoda to rzecz która jest funkcją schowaną w klasie
#do konstrukcji funkcji używamy def

# : aby funkcja mogła działać, w innych języjach klamry
def rysunek():
    '''funkcja która rysuje menu wyświetla się  po najechaniu na funkcję '''
    print('''
                <----****----->
                <------------->
                    menu 1
                    menu 2         
    ''')      # dok string to jest to co jest między potrojnymi cudzysłowami

#moduł w python   new->python package
#funkcja może byc przechowywana w liście ale bez nawiasów okrągłych
#opisanie klasy/funkcji

def powitanie():
    imie = input("podaj swoje imie")
    print("Cześć", imie)



def powitanie2(imie='domyslny'):
    '''wita się z użytkownikem'''
    print("Cześć", imie)


def promien(r):    #return - zwraca funkcja zwykle z returnem
    pi = 3.15      #zmienna lokalna, kod najpierw szuka globalnie jak nie znajdzie to bierze lokalnie z funkcji
    return (pi*r*r)

def promien(r):
    global pi       #można też tak definiować monumentalną zmienną pi, przesłania wszytskie pi, niepolecane
    pi = 4.45
    return (pi*r*r)



