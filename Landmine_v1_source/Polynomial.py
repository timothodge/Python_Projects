'''
Created on Apr 24, 2014

@author: Tim
'''
import Monomial
class Poly(object):
    '''
    classdocs
    Printpoly prints the corresponding polynomial using the printer for monomials.
    '''
    def Printpoly(self):
        #print(self.Poly_Array)
        return_string = self.Poly_Array[0].printmonomial()
        for i in range(1,len(self.Poly_Array)):
            # print(self.Poly_Array[i].printmonomial())
            return_string += ' + '
            return_string += self.Poly_Array[i].printmonomial()
        return return_string
    
    '''
    Evalpoly runs through monomials evaluating them and adding it all together.
    '''
    def Evalpoly(self,Pt):
        return_value = 0
        for i in range(len(self.Poly_Array)):
            return_value += self.Poly_Array[i].Evalmonomial(Pt)
            
        return return_value
    
    
            
            

    def __init__(self, Poly_String):
        '''
        Constructor:
        Split the polynomial up into the corresponding monomials, convert them to monomials and make a Poly_Array
        '''
        Tmp_Array = Poly_String.replace(' ','').split('+')
        #print(Tmp_Array)
        self.Poly_Array = []
        for i in range(len(Tmp_Array)):
            self.Poly_Array.append(Monomial.Mono(Tmp_Array[i]))
        #print(self.Poly_Array)
        #print(len(self.Poly_Array))
            
            
            