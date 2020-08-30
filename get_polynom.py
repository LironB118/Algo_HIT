from newtons import newton
import numpy as np
import sys

class GetPolynom:


    def main(self):
        try:
            lst=[]
            n = int(input("Please type your function number of items: "))
            for i in range(0,n): 
                c = int(input("enter the {} item coeffitient: ".format(i+1)))
                lst.append(c) # adding the element 
            max_iteration=int(input("Please type max iteration : "))
            initial_guess=float(input("Please type your initial guess: ")) 
            user_polynomial= np.poly1d(lst)
            print ("going to call newton's methos for this function \n{}".format(user_polynomial))
            newthon_algo= newton(max_iteration,initial_guess,lst)
            result=newthon_algo.newton()
            newthon_algo.plotting_function(result)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
        

                
c=GetPolynom()
c.main()