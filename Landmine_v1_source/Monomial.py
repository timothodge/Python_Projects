'''
Created on Apr 24, 2014

@author: Tim
'''

class Mono(object):
    '''
    Functions:
        Get Coefficient, or any of the exponents of the monomial
        Printer for printing the monomial
        Evaluater of the monomial (must be given a point)
    '''
    def getCoef(self):
        return self.coef
    
    def getXpower(self):
        return self.xpower
    
    def getYpower(self):
        return self.ypower
    
    def getZpower(self):
        return self.zpower
    def getTpower(self):
        return self.tpower
    
    def printmonomial(self):
        return_string = str(self.coef)
        if(self.xpower != '0'):
            return_string+='x'
            return_string+=str(self.xpower)
        if(self.ypower != '0'):
            return_string+='y'
            return_string+=str(self.ypower)
        if(self.zpower != '0'):
            return_string+='z'
            return_string+=str(self.zpower)
        if(self.tpower != '0'):
            return_string+='t'
            return_string+=str(self.tpower)
        return return_string
    
    def Evalmonomial(self,Pt):
        #print(self.coef*Pt.getXcomp()**int(self.xpower))
        return self.coef*Pt.getXcomp()**int(self.xpower)*Pt.getYcomp()**int(self.ypower)*Pt.getZcomp()**int(self.zpower)*Pt.getTcomp()**int(self.tpower)
    
    
        


    def __init__(self, monomial_String):
        '''
        Constructor
        Given a string rip off corresponding coefficient and corresponding exponents.
        '''
        
        exp_array = [monomial_String.find('x'),monomial_String.find('y'),monomial_String.find('z'),monomial_String.find('t')]
        # print('Exp_array is ', exp_array)
        #monomial_arr.append(float(monomial[0:min(arr)]
        
        # Try to assign the coefficient this will fail if there is no constant or if all variables are missing
        try:
            self.coef = float(monomial_String[0:min(filter(lambda x:x>0,exp_array))])
        except:
            #Assuming there is only a constant then this will convert it to a float.
            try:
                self.coef = float(monomial_String)
                #All else fails the coeff must be a 1
            except:
                self.coef = 1
  
    #Grabbing x exponent
    #Check if the exponent if x is at the end of string with no exponent
        if(exp_array[0]+1 >= len(monomial_String)):            
            self.xpower = 1    
        #Check to see if there is no x in the monomial -1 is error for .find function
        elif(exp_array[0] != -1):
            #Checking to see if where the exponent should be is a character
            if(type(monomial_String[exp_array[0]+1]) == type('')):
                
                #This will try to append where the exponent would be (if it exists)
                try:
                    self.xpower = monomial_String[exp_array[0]+1:exp_array[1]] 
                    #All else fails the power must be one and was left out.
                except:
                        self.xpower = 1
        else:     
            self.xpower = 0
        #All other exponents grabbbing happens this way.
        
    #Grabbing y exponent    
        if(exp_array[1]+1 >= len(monomial_String)):
            self.ypower = 1      
        elif(exp_array[1] != -1):  
            if(type(monomial_String[exp_array[1]+1]) == type('')):
                try:
                    self.ypower = monomial_String[exp_array[1]+1:exp_array[2]] 
                except:
                        self.ypower = 1 
        else: 
            self.ypower = 0 
    
    #Grabbing z exponent    
        if(exp_array[2]+1 >= len(monomial_String)):
            self.zpower = 1        
        elif(exp_array[2] != -1):
            if(type(monomial_String[exp_array[2]+1]) == type('')):
                try:
                    self.zpower = monomial_String[exp_array[2]+1:exp_array[3]] 
                except:
                        self.zpower = 1
        else: 
            self.zpower = 0   
       
       
       
    #Grabbing t exponent    
        if(exp_array[3]+1 >= len(monomial_String)):
            self.tpower = 1    
        elif(exp_array[3] != -1):
                try:
                    self.tpower = monomial_String[exp_array[3]+1:len(monomial_String)] 
                except:
                        self.tpower = 1
        else: 
            self.tpower = 0   
            
            
            
            
            