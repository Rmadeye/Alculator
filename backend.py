# -*- coding: utf-8 -*-
"""
Script to perform calculations
"""

class Calculations:

    def calc_dil(vol,des,dendes,per,den):
        return ((vol*per*den)-(vol*des*dendes))/(des*dendes)
    def count_pure(vol,den,per):
        print(vol*(per/100)*den)
        return vol*(per/100)*den
    
    
        