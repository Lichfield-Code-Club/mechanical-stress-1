#Create a program to calculate the percentage error of t-w approx
#pipe properties/conditions class
class Pipe:
    def init(self, p, ri, ro,):
        self.p = p #pressure difference [MPa]
        self.ri = ri #inner radius [mm]
        self.ro = ro #outer radius [mm]

pipeInput = Pipe(0,0,0)

#input function
pipeInput.p = int(input("Enter the pressure difference: \n ->"))
pipeInput.ro = int(input("Enter the outer radius: \n ->"))
pipeInput.ri= int(input("Enter the assumed inner Radius: \n ->"))

#A function to calculate the actual stress in the cylinder walls

def hoop_stress_radius_iter(Pipe,temp):
#    while Pipe.ri < Pipe.ro:
     hs = (Pipe.p(Pipe.ro2 + temp2))/(Pipe.ro2 - temp2)
#        print(hs)
     return hs


#A function to calculate the stress using t-w approx
def hoop_stress_tw_approx(Pipe,temp):
    hs = (Pipe.p(Pipe.ro + temp)/2)/(Pipe.ro-temp)
    return hs

#A function to calculate the percentage error
#hst = hoop stress thick wall calculation
#rit = inner radius for thick wall calculation
#hstw = hoop stress thin wall approx
#inner radius for thin wall approx omitted as it equals rit
def hoop_error_percent(hst,hstw):
    error = abs((hst - hstw)/hst) * 100
    return error
#A function to check whether % error < 1% -> if so = true
def error_size_check(error):
    if error < 1:
        return True
    else:
        return False

#main body
temp = pipeInput.ri
while temp < pipeInput.ro:
    error = hoop_error_percent(hoop_stress_radius_iter(pipeInput, temp),hoop_stress_tw_approx(pipeInput, temp))
    if error_size_check(error) == True:
        print(str(round(error,2)) + "% - inner radius: " + str(round(temp,2)))
        break
    else:
        temp = temp + 0.1