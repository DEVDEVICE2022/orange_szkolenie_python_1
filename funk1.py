def duzo_rzeczy(data, *args,**kwarks):   #funkca guma może ale nie musi przyjąc jakiś argument, przydaje się jeśl nie wiemy ile bezie argumentów
    print(data)
    print(args)   #argumenty bez nazwy        ()
    print(kwarks)     #argumenty z kluczem   {}

duzo_rzeczy(4,55,7.55,'Tomek',wiek=39)



def maximum(*liczba):  # ta liczba to argument zastepujący args kwarks...to argument który musi być ale nie musi,
    if len(liczba) ==0:   # jeeli dł mojej liczby równa się ) to nic nei zwracaj
        return None
    else:
        liczba_max = liczba[0]
        for n in liczba[1:]:
            if n>liczba_max:
                liczba_max = n
        return liczba_max

w = maximum()
print(w)
w1 = maximum(3,2,8,-2,45,9,89)
print(w1)

def fun1(xy, **inne):   # a to argument z kluczem
    print('x:{0},y:{1},klucze w zmiennej inne:{2}'.format(x,y,list(inne.keys())))
    inne_razem = 0
    for k in inne.keys():
        inne_razem=inne_razem+inne[k]
        print('Łącznie w zmiennej inne jest wartosc {0}'.format(inne_razem))
fun1(2,"1",liczb=34)
