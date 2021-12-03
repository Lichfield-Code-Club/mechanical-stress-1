import math

m = 0.5 # mass, kg
d = 0.14 # distance from pivot point, metres
i = 0 # moment of inertia, kg per square metre
g = 9.81 # acceleration due to gravity, metres per second squared

# Rearranging the equation
# i = (((t / 2pi)**2) * mgd) - (m * (d**2))
oscillations = [11,12,11,12,9] # time for 10 swings, seconds
total_duration = sum(oscillations)
num_oscillations = len(oscillations) * 10
t = total_duration/num_oscillations
i = (((t / (2*math.pi)**2)*(m*g*d)- (m*(d**2))))

print(f'I = {i:.3e} kg/m\N{SUPERSCRIPT TWO}') # https://unicode.org/Public/UNIDATA/NamesList.txt