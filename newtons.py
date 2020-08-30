import numpy as np
import matplotlib.pyplot as plt
import sys

class newton:


    def __init__(self,max_iter,x0,lst_coeff):
        self.epsilon = 0.0000001
        self.max_iteretion=max_iter
        self.function_coeff=lst_coeff
        self.initial_guess=x0
        self.user_polynomial=np.poly1d(self.function_coeff)
        
    def function(self,x):
        return self.user_polynomial(x)

    def derivative(self,x):
        p2 = np.polyder(self.user_polynomial)
        return p2(x)

    def plotting_function(self,sqrt):
        print("The approximate value of x is: "+str(sqrt))
        # Plotting configuration
        u = np.arange(sqrt-0.5, sqrt+0.5, 0.0001) # Setting up values for x in the plot
        w = self.user_polynomial(u)# Define the main function again

        plt.plot(u, w)
        plt.axhline(y=0.0, color='black', linestyle='-')
        plt.title('Newton-Raphson Graphics for \n {}'.format(self.user_polynomial))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.legend(['Xn'], loc='upper left')
        plt.show()


    def newton(self):
        try:
            x0=self.initial_guess
            x1 = 0

            if abs(x0-x1)<= self.epsilon and abs((x0-x1)/x0)<= self.epsilon:
                return x0

            print("k\t x0\t\t function(x0)")
            k = 1

            while k <= self.max_iteretion:
                x1 = x0 - (self.function(x0)/self.derivative(x0))
                print("x%d\t%e\t%e"%(k,x1,self.function(x1)))

                if abs(x0-x1)<= self.epsilon and abs((x0-x1)/x0)<= self.epsilon:
                    plt.plot(x0, self.function(x0), 'or')
                    return x1
                
                x0 = x1
                k = k + 1
                plt.plot(x0, self.function(x0), 'or')

                # Stops the method if it hits the number of maximum iterations
                if k > self.max_iteretion:
                    print("ERROR: Exceeded max number of iterations")

            return x1

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
        