'''
Created on Apr 22, 2014

@author: Tim
'''

import numpy as np #Have version 1.6.2 as of 4/28/14

import Polynomial
import Monomial
import Point
def main():
    print("This is the main for version 1")

    M = Monomial.Mono('-3x2y4z3t0')
    #M2 = Monomial.Mono('0x0y0z0t0')
  
    #P2 = Point.Pt([2,3,4,5])
    #print(M.printmonomial())
    #print(M2.printmonomial())
    #print(M2.evalmonomial(P2))
    #print(M2.printmonomial())
    #print(M3.printmonomial())
    #print(M4.printmonomial())
    Poly_S = 'x2y0z0t0 + x0y2z0t0 + x0y0z2t0 + -1x0y0z0t0'
    Poly = Polynomial.Poly(Poly_S)
    
    print(Poly.Printpoly())
    P = Point.Pt([1,3.21,5.6,0])
    print(Poly.Evalpoly(P))
    
    
    
#     Re = np.linspace(0,1,num = 11)
#     Im = np.linspace(-1,1,num = 11)
#     
#     x,y = np.meshgrid(Re,Im)
    
    #z = x + 1j*y # 1j is I for imaginary numbers this is the complex grid
    #print("Re is ",Re)
    #print("Im is ", Im)
    #print("Complex Grid is ", z)
    
    ###### Midpt grid work######
    
    Re_arr = [.05]
    Re_add = .1
    Im_pos_arr = [.05]
    Im_neg_arr = [-.05]
    for i in range(1,10):
        Re_arr.append(Re_arr[i-1]+Re_add)
        Im_pos_arr.append(Im_pos_arr[i-1]+ Re_add)
        Im_neg_arr.append(Im_neg_arr[i-1]-Re_add)
        
    #print("Real array is ",Re_arr)
    Im_arr = Im_pos_arr + Im_neg_arr
    Im_arr.sort()
    #print(Im_arr)    
    
    
    x,y = np.meshgrid(Re_arr,Im_arr)
    Midpt_grid = x + 1j*y
    
    print("Midpt_grid is ",Midpt_grid)
    print(type(Midpt_grid))

if __name__ == '__main__':
    main()