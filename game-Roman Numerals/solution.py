#!/usr/bin/env python

ROMAN = ['0','I','II','III','IV','V','VI','VII','VIII','IX','X']

print ("Iniciando solução para jogo de converter número inteiro para Romano")
number = input("Insira o numero")

if ( len(number) == 1 ):
    print (ROMAN[int(number)] )   
