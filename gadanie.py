#from google_speech import Speech    #import modułu z pypi.org   google-speech 1.1.0 musi być zaimportowany. Speech to klasa
                                    #
#pakiet random - generator liczb losowych
import random

# r = random.random() * 10
# print(int(r))

k6 = random.randrange(1,6)   # zasięg od 1 do 5
k6_2 = random.randint(1,6)   # zasięg od 1 do 6
k6_3 = random.randrange(100)
print(k6)
print(k6_2)
print(k6_3)

l = ['tomek','ania','karolina']

losowanie = random.choice(l)    #- choice losuje z listy, słownika, krotkę...
print(losowanie)
