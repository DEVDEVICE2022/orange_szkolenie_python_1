imie1 = "Mirek"
imie2 = "Marek"

if imie1 == imie2:
    print("jest ok")
elif imie1 != imie2:
    print("nie jest ok")


start = 1
for i in range(1,101):
    print(i+start)


licznik = 0
while licznik < 100:  #wcięcie ustawia się po :    while się zawsze uruchomi, chociaż raz aby sprawdizć warunek if czeka na spełnienie warunku
     licz = licznik + 1
     print(licz)