'''
Created on Apr 24, 2014

@author: Tim
Point class used for plugging in monomial and polynomial class

'''

class Pt(object):
    '''
    Only functions are to return the x,y,z, and t components
    '''
    def getXcomp(self):
        return self.xcomponent
    def getYcomp(self):
        return self.ycomponent
    def getZcomp(self):
        return self.zcomponent
    def getTcomp(self):
        return self.tcomponent
    
    def PrintPt(self):
        return_string = '('
        return_string += str(self.xcomponent,',')
        return_string += str(self.ycomponent,',')
        return_string += str(self.zcomponent,',')
        return_string += str(self.tcomponent)


    def __init__(self, component_array):
        '''
        Constructor
        From array assign x,y,z,t
        '''
        self.xcomponent = component_array[0]
        self.ycomponent = component_array[1]
        self.zcomponent = component_array[2]
        self.tcomponent = component_array[3]
        