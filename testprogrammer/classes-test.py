class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

x.data  = 1
while x.data  < 10:
    x.data  = x.data  * 2
print(x.data )
del x.data