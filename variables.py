"""variable rules
- variable names are case sensitive name and NAME are different variables
- must start with a letter or underscore _
- may have numbers but cant start withone
"""
x = 1 #int
y = 2.5 # float
name = 'Brad' # string
is_cool = True # bool

#Multiple assignments
x, y, name, is_cool = (1,2.5,'Brad',True)
print(x)
print(y)
print(name)
print(is_cool)
print(x, y, name, is_cool)

#math
a = x + y
print(a)

print(type(a))
b = str(a)
print(type(b))


#string
name = 'Vijay'
print ('Hello '+ name + ' How are you?')
#Arguments by position
print ('{0}, {1}, {2}'.format('this_goes_1st', 'this_second', 'this_third'))
print ('{1}, {2}, {0}'.format('this_goes_1st', 'this_second', 'this_third'))
#Arguments by name
print ('{name}, {place}, {age}'.format(name = 'Vijay', place = 'Bdvt',  age = '34'))
#F strings only in 3.6+
#name = 'Vijay'
#place = 'Shmg'
#print(f'My name is {name} & I am from {place})
#String Methods
s = 'hello guys we are here'
print(s.capitalize())
print(s.upper())
print(s.replace('guys','all'))
print(len(s))

#List is an array(java) . It is a collection which is ordered and changable. Allows duplicate members
number_list = [1,2,3,4,5]
print(type(number_list))

fruits = ['Apples','Orange','Banana']
print(len(fruits))
fruits.append('Mango')
print(fruits)
fruits.remove('Orange')
print(fruits)
#insert into position
fruits.insert(1,'BLue Berry')
print(fruits)
#remove from position
fruits.pop(1)
print(fruits)
fruits.sort(reverse = True)
print(fruits)
#.sort.reverse inplace

#TUple ordered collection  is unchangable(immutable). Allows duplicate memebers
fruits_tup = ('Apples','Orange','Banana')
print(len(fruits_tup))
print(fruits_tup[2])

#set IS A COLLECTION WHIch is unordered and unindexed . Cannot have duplicates. Is mutable
fruit_set = {'Apple','Orange', 'Banana', 'SOmeBerry'}
#check if in set
print('Orange' in fruit_set)
fruit_set.add('GRapes')
print(fruit_set)
fruit_set.remove('GRapes')
print(fruit_set)
fruit_set.clear()
print(fruit_set)
del fruit_set
#print(fruit_set)


#Dictionay, unordered ,changable & indexed. No Duplicates
person = {'name' : 'vijay', 'age':33, 'place' : 'bdvt'}
print(person['place'])
print(person.get('name'))
# add key values
person['phone'] = 3345553
print(person)
print(person.keys())
print(person.values())
#make a copy, so that you can add ned elements to copy
person2 = person.copy()
print(person2)
del(person2['age']) #person.pop('age')
print(person2)
person2.clear() #empty
# list pf dicts
people = [{'name' : 'vijay', 'age':33, 'place' : 'bdvt'},
{'name' : 'sujay', 'age':34, 'place' : 'shmg'}]
print(people[1]['name'])

#Functions
def sayHello(x):
    print('Hello ' + x )
sayHello('Vijay')

def getSum(x,y):
    z = x + y
    return z
print(getSum(2,5))
#lambda, just one expression, no need to explicit return
getSumLambda = lambda num1, num2 : num1 + num2
print(getSumLambda(5,5))

#conditionals ==, !=, >, <, >=, <=
#logical operator and, or, not
#membership operators not, not in
x, y = 5, 5
if x == y :
    print('both equal')
