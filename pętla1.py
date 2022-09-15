# najczęściej while - dopóki
#while (dopóki) warunek:
#ciało pętli
#else:
#kod który, gdy warunek nie jest spęłniony

#w kodzie wszsytko dzieje się na wcięćiach. Pycharm poprawia sam

licznik = 0
while licznik < 3:  #wcięcie ustawia się po :    while się zawsze uruchomi, chociaż raz aby sprawdizć warunek if czeka na spełnienie warunku
    print(licznik, "mniejszy od 5")
    licznik = licznik + 1
    #licznik += 1   skrócona wersja tego co powyżej
print("Poza pętlą")
print(licznik)
# break -  hamuje działanie pętli, uciekamy jakąś instrukcję warunkową

#jedyna pętla to if w 3.10 pojawia się keys oprócz if
if licznik == 5:   # jeśli licznik jest równe 5 to wyświetl licznik + równe 5
    print(licznik, "równe 5")
    #ELIF   = else if   jeżeli nie. Elifów może być nieskończenie dużo
elif licznik> 6:   # jesłi licznik jest większe od 6 to zrób poniższy warunek i wyświetl licznik +komunikat większe od 6
    print(licznik, "większe od 6")
elif licznik<4:
    print(licznik, "mniejsz od 4")
else:   # jeśli żaden z powyższych warunków nie jest spełniony, to warunek na resztę, nie występuje samodzielnie
    print("Ja tu sobie jestem else...")



