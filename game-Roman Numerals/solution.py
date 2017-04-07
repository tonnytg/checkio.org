#!/usr/bin/env python
#ROMAN = ['0','I','II','III','IV','V','VI','VII','VIII','IX']
#ROMANBig = [ 'X','L','C','D','M' ]
#number = input("Insert a number: ")
#if ( len(number) == 1 ):
#    print (ROMAN[int(number)] )
#elif ( len(number) == 2 ):
#    if ( int(number[1:2]) == 0 ):
#        print ('X')
#    else:
#        print('X' + ROMAN[int(number[1:2])]  )
R1 = { 0:0,1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX' }
R2 = { 10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC' }
R3 = { 100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM' }
R4 = { 1000:'M',2000:'MM',3000:'MMM',4000:'MMMM' }

number = input ("Insert: ")
print( R1[int(number)] )
