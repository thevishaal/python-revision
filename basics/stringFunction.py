#Day - 01

n = 'this Is PytHon'
print(n)
print(n.upper())    #all words capital
print(n.lower())    #all words small
print(n.title())    #1st letter capital of every word
print(n.capitalize())  #1st letter of sentece capital
print(n.swapcase())   #reverse small to capital , capital to small


# index function 
name = 'Raj kumar'
print(name.index('u'))
print(name.find('m'))

#count function
line = 'this is my code'
print(line.count('i'))

word = 'Python code Python test'
print(word.count('Python'))

#Day - 02

n = 'A12b'
print(n.isalnum())

r = 'Abc'
print(r.isalpha())

w = '123'
print(w.isdigit())

m = 'ASF'
print(m.isupper())
print(m.islower())
