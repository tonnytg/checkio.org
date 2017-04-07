#!/usr/bin/env python

ROMAN = ['0','I','II','III','IV','V','VI','VII','VIII','IX','X']
number = input("Insert a number: ")

if ( len(number) == 1 ):
    print (ROMAN[int(number)] )   
