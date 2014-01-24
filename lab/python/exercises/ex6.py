#Dette er en x verdi der %=10 personer.(%d for decimal)
x= "there are %d types of people." %10
#Verdier
binary = "binary"
do_not = "don't"
#bruker en verdi y der %=s er binary go (%s for string)
y = "Those who know %s and those who %s." % (binary, do_not)

#skriver ut verdi x og y
print x
print y

#skriver ut %r og %x
print "I said %r." % x
print "I also said: '%s'." %y


#Her setter man %r verdien til å hete "Hilarious"
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#Ganske forklarende i teksten
w = "This is the left side of..."
e = "a string with a right side."

print w + e