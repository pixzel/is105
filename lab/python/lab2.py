# -*- coding: latin-1 -*-

#
#  IS-105 LAB2
#
#  lab2.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Jens Holm', \
			'student2': 'Sondre Lind', \
            
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
print """
#
oppgave 1
#
"""
def ascii_fugl():
	print """
	       \/_
	  \,   /( ,/
	   \\\' ///
	    \_ /_/
	    (./
	     '` 
	"""
	
ascii_fugl()

# 
#  Oppgave 2
#    'return 2' - 2 skal erstattes med en korrekt returverdi, 2 er kun en stedsholder
#    bitAnd - x&y
#    Eksempel: bitAnd(6, 5) = 4
#
print """
#
oppgave 2
#
"""
#bitAnd sammenligner med bruk av tegnet &
def bitAnd(x, y):
	return x & y
     
    #Her skrives funksjonen med 5 og 6 som parameter
    # 5 = 0101^2, 6 = 0110^2 her sammenlignes det og blir = 0100 = 4
print bitAnd(5, 6)
#
#  Oppgave 4
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
print """
# 
oppgave 4
#
"""
#Her ser Xor etter forskjell
def bitXor(x, y):
  return x^y

# 3 = 0011^2, 5 = 0101 alle ulike tells = 0110 = 6
print bitXor(3,5)

#
#  Oppgave 5
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
print """
#
oppgave 5
#
"""
def bitOr(x, y):
  return x|y
  

print bitOr(5,6)

#
#  Oppgave 6
#    ascii8Bin - ta et tegn som argument og returnerer ascii-verdien som 8 bits streng binært
#    Eksempel: ascii8('A) = 01000001
#
#  Tips:
#    For å finne desimalverdien til et tegn bruk funksjonen ord, for eksempel
#      ord('A) , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
print """
#
oppgave 6
#
"""
def ascii8Bin(bokstav):
	snus = ord(bokstav)
	return '{0:08b}'.format(snus) 
	


print ascii8Bin('b') 
#  Oppgave 7
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#
print """
#
oppgave 7
#
"""
def transferBin(fest):
	l = list(fest)
	for c in l:
		print ascii8Bin(c)

transferBin("hei")

		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)

#
#  Oppgave 8
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#  
print """
#
oppgave 8
#
"""

def ascii2hex(hi):
	hexa = ord(hi)
	return '{0:08x}'.format(hexa)
		

def heksa(hexa):
	liste = list(hexa)
	for c in liste:
		print ascii2hex(c)


ascii2hex("h")
heksa("Lind")




		
