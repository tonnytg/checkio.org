#!/usr/bin/env python

ROMAN = ['0','I','II','III','IV','V','VI','VII','VIII','IX']
ROMANBig = [ 'X','L','C','D','M' ]

number = input("Insert a number: ")

if ( len(number) == 1 ):
    print (ROMAN[int(number)] )
elif ( len(number) == 2 ):
    if ( int(number[1:2]) == 0 ):
        print ('X')
    else:
        print('X' + ROMAN[int(number[1:2])]  )
