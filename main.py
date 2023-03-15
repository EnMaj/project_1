
day = int(input())

mil_1=16637000000 #миль
v=38241 #миль в час

mil_2= mil_1-day*24*v

km_2=mil_2*1.609

ae=km_2/149597870.7

print(mil_2)
print(km_2)
print(ae)