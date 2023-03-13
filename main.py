import ru_local as ru

print(ru.initial_value)
volume = float(input())

liters = volume * 3.785412
print(ru.liters, round(liters, 2))
barrels = volume / 19.5
print(ru.barrels, round(barrels, 2))
co2 = volume * 20
print(ru.co2, round(co2, 2))
ethanol = volume * (115000 / 75700)
print(ru.ethanol, round(ethanol, 2))
cost = volume * 3
print(ru.cost, round(cost, 2))

#средний объём потребления нефтепродуктов в России 3699000 баррелей в сутки.
bar_1 = 3699000
gallon_1 = bar_1 * 19.5
litr_1 = gallon_1 * 3.785412
v_litrah_in_year = litr_1 * 365
print(ru.v_litrah_in_year,v_litrah_in_year)