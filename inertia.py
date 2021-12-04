import math

m = 0.5 # mass, kg
d = 0.14 # distance from pivot point, metres
g = 9.81 # acceleration due to gravity, metres per second squared

# Rearranging the equation
# Divide each side by 2pi
# Square each side to remove square root
# Multiply each side by mgd
# Subtract md squared from each side
# i = (((t / 2pi)**2) * mgd) - (m * (d**2))
oscillations = [11,12,11,12,9] # time for 10 swings, seconds
total_duration = sum(oscillations)
num_oscillations = len(oscillations) * 10
t = total_duration/num_oscillations

twopi = math.pi * 2
tsq = (t / twopi) ** 2
mgd = m * g * d
dsq = d ** 2
mdsq = m * dsq

I = (tsq * mgd) - mdsq # moment of inertia, kg per square metre

print(f'I = {I:.3e} kg/m\N{SUPERSCRIPT TWO}') # https://unicode.org/Public/UNIDATA/NamesList.txt