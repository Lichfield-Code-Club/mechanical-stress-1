import math

v = 10 # metres per second
p = 1.225 # air density (rho) kg per cubic metre
a = 10 # attack angle (alpha) degrees
d = 0 # drag
q = 0.5 * ( p * (v**2))
c = 2 * math.pi * a # lift coefficient
l = q * c # lift per unit chord

print(f"The lift is {l:.3f}N")