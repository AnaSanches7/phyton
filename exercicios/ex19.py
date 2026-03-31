catop = float(input("cateto oposto"))
catad = float (input(" cateto adjacente"))
hi = (catop**2+catad**2)**0.5
print (" A hipotenusa vai medir{}".format(hi))

from math import hypot 
catop = float (input("cateto oposto:"))
catad = float (input("cateto adjacente: "))
hi = hypot(catop,catad)
print( " A hipotenuda vai medie {}".format(hi))