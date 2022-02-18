# logic control the flow of the program.
#python cheatsheet

a = 5
b = 7

a >= b #false
a <= b #false

c = a > b #false
d = a < b #true

e = a is b #false (==)
f = a is not b #true (!=)

g = not e #oposite of e, so true

h = e and f #False T&F=F (+ - = -) (If one option is false then the whole thing is false)

j = e or f #true (only one option has to be true)

if e:
    print('e is true')

#3elif g: #else if checks if with the rest
    print('this one will always print')

else:
    print('e lied!')

