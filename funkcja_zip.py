# pakujemy łaczenie dwóch obiektów w jeden, obiekty iterowalne
x= [1,2,3,4]
y = ['a','b','c']
z = x+y
print (z)
print (type(z))
#  efekt [1, 2, 3, 4, 'a', 'b', 'c']
# funkcja zip służy do dopasowania odpowiedników
x= [1,2,3,4]
y = ['a','b','c']
z = zip(x, y)
print (list(z))
print (type(z))
# efekt [(1, 'a'), (2, 'b'), (3, 'c')]  dopasowuje wg indeksu

x = 0
if 0 <  x < 10:     # lub taki zapis jest tożsamy  if 0 <  x and x < 10:
        print("....")






