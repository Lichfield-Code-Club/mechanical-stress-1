#Create a program to calculate the percentage error of t-w approx
#pipe properties/conditions class
class Pipe:
    def __init__(self,p, ri, ro,):
        self.p  = p  #pressure difference [MPa]
        self.ri = ri #inner radius [mm]
        self.ro = ro #outer radius [mm]

    # Equation 4
    def hoop_stress(self,r):
#        print(f"hoop stress: p=[{p}], ri=[{ri}], ro=[{ro}]")
        h1 = (p * (ri**2)) * ((ro**2) + (r**2))
        h2 = (r**2) * ((ro**2) - (r**2))
        hs = h1/h2
        return int(hs)

    # Equation 5
    def hoop_stress_max(self):
        print(f"hoop stress max: p=[{p}], ri=[{ri}], ro=[{ro}]")
        h1 = p * (ro**2) + (ri**2)
        h2 = (ro**2) - (ri**2)
        hs = h1/h2
        return hs

    #A function to calculate the stress using t-w approx
    # I'm not sure of the role of temp here, so I might get this wrong
    def hoop_stress_tw_approx(temp):
        print(f"hoop stress: p=[{p}], ri=[{ri}], ro=[{ro}]", temp=[{temp}])
        h1 = p * ((ro + temp)/2)
        h2 = (ro + temp) - (ro-temp)
        hs = h1/h2
        return int(hs)

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

    #A function to calculate the actual stress in the cylinder walls
    def hoop_stress_radius_iter(temp):
    #    while Pipe.ri < Pipe.ro:
        hs = (Pipe.p(Pipe.ro2 + temp))/(Pipe.ro2 - temp)
    #        print(hs)
        return hs

#main body
if __name__ == '__main__':
    #input function
   # p  = int(input("Enter the pressure difference: \n ->"))
   # ro = int(input("Enter the outer radius: \n ->"))
   # ri = int(input("Enter the assumed inner Radius: \n ->"))
    
    p  = 20  # Pressure difference 20MPa
    ro = 100 # Outer radius 100mm
    ri = 90  # Inner radius 90.5mm

    pipeInput = Pipe(p,ro,ri)

    hsMax = pipeInput.hoop_stress_max() # Equation 5
    print(f"Max  Stress [{hsMax}]")

    for r in range(1,ro):
        stress = pipeInput.hoop_stress(r)
        print(f"Stress at radius [{r}]=[{stress}]")
    
#    temp = pipeInput.ri
#    while temp < pipeInput.ro:
#        error = hoop_error_percent(hoop_stress_radius_iter(pipeInput, temp),hoop_stress_tw_approx(pipeInput, temp))
#        if error_size_check(error) == True:
#            print(str(round(error,2)) + "% - inner radius: " + str(round(temp,2)))
#            break
#        else:
#            temp = temp + 0.1