#iteratory to for while...
#Yeld działa jak stoper, robi swoje i pamięta poprzedni stan, można go zatrzymać porobić i zrobić kolejny krok


def cztery():
    x = 0
    while x < 4:
        print("W generatorze x =", x)
        yield x
        x += 1

for i in cztery():
    print(1)
