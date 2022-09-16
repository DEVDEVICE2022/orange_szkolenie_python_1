# nie jest konieczna do podstaw z python
# funkcja wykonywana ad hoc tu i teraz zar w programie np do przekształcenia st kelwin na celsjusz
# lambda jest po to by nie pisać funkcji prostych

# lambda <parametry> : <wyrażenie>     - składnia lambdy, tylko w jednej linii

dodawanie = lambda a, b: a + b
print(dodawanie(2, 3))


temp={'FnaK': lambda st_f:273.15+ (st_f-32) * 5/9, "CnaK": lambda st_c: 237.15 +st_c}
print(temp["FnaK"](32))
print(temp["CnaK"](32))