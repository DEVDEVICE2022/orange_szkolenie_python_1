rzecz = "pythona"
tekst = "Lubię %s" % rzecz    #%s - spodziewana zmienna jako string
print(tekst)
godzina = 14.56
dzien = "środę"
tekst2  = "Jest teraz godzina: %.2f, a dziś mamy %s" %(godzina, dzien)    #%s - spodziewana zmienna jako intiger
#%.2f spodziewany float dwa miejsca po przecinku
print(tekst2)
# częćciej wykorzytywany sposób, formatowania, wyświetlania stringów - litera f i beczka{}
print(f"Lubię {rzecz} ")   #skorzystamy z beczki{} wstawiając f
tekst3  = (f"Jest teraz godzina:{godzina}, a dziś mamy{dzien} ")
print(tekst3)


