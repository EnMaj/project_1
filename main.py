import ru_local as ru

day = int(input(ru.DAY))

mil_1 = 16637000000 #миль
v = 38241 #миль в час

mil_2 = mil_1-day*24*v
km_2 = mil_2*1.609
ae = km_2/149597870.7
delay_comm = ((km_2*1000/299792458)/60)/60

print(ru.DISTANCE)
print(mil_2, ru.MIL)
print(km_2, ru.KM)
print(ae, ru.AE)
print(ru.DELAY,delay_comm,ru.HOUR)