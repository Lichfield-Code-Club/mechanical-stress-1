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
        return int(hs)

    #A function to calculate the stress using t-w approx
    # Equation 6
    def hoop_stress_tw_approx(self,r):
        h1 = p * ((ro + r)/2)
        t = ro - r
        hs = h1/t
        return int(hs)

    #A function to calculate the percentage error
    #hst = hoop stress thick wall calculation
    #rit = inner radius for thick wall calculation
    #hstw = hoop stress thin wall approx
    #inner radius for thin wall approx omitted as it equals rit
    def hoop_error_percent(self,hst,hstw):
        error = abs((hst - hstw)/hst) * 100
        return int(error)

    #A function to check whether % error < 1% -> if so = true
    def error_size_check(self,error):
        if error < 1:
            return True
        else:
            return False

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

    for r in range(1,ro):
        thick = pipeInput.hoop_stress(r)
        thin = pipeInput.hoop_stress_tw_approx(r)
        error = pipeInput.hoop_error_percent(thick,thin)
        isZero = pipeInput.error_size_check(error)
        if isZero:
            print(f"Radius [{r}]: thick=[{thick}], thin=[{thin}], error=[{error}], is zero=[{isZero}]")
    