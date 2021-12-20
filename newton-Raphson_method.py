#write a program to find roots of function using
#Newton - Raphson method

import numpy as np #used for error check

class function_x:
    fx = 0     #variable to keep track of function output
    deriv = 0  #variable to keep track of function derivative output
    coeff = 1  #function coefficient, redundant in this case, added for potential future changes
    power = 2  #power to which input is rased in the f(x)
    def __init__(self,N, guess, error,maxiter):
        #self.coeff = coeff
        #self.power = power
        self.N = N              #N - input number - value of which we want to find a root
        self.guess = guess      #initial guess for the N-R method
        self.error = error      #certainty to which we want our approx. to be
        self.maxiter = maxiter  #maximum number of iteration we want to perform (in case the program does something funky)
        #self.__deriv = deriv
        #self.__fx = fx
        
    def deriv_x(self,guess):    #calculates the value of the f'(x) at x = guess
        self.deriv = ((guess**(self.power-1))*self.coeff*self.power)
        return self.deriv
    def func_x(self, guess):    #calculates f(x) at x = guess
        self.fx = (self.coeff*(guess**self.power) - self.N)
        return self.fx
    def findStep(self, guess):  #finds next guess for the N-R method
        self.guess = guess -(self.func_x(guess)/self.deriv_x(guess))
        
x = function_x(15, 10, 0.0001,100)

i = 0                           #keeps count of iterations performed
for n in range(0,x.maxiter):    #loop to iterate through the N-R 
    
    x.findStep(x.guess)         #calls the find next step function
    i = i+1
    if np.abs(x.guess) - np.sqrt(x.N) < x.error:    #check if the error between our value and the actual root is less then our desired error
        break


print ("Square root of {} : {}".format (x.N,"%5.3f" % x.guess))
print ("Number of iterations: {}".format(i))
