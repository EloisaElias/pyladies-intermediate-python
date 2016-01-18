import pytest

# Exercise 1
# Use list comprehension to create a function that multiplies
# each element in a sequence of numbers by 2
# ================================
def double(sequence):
	# return [...]
	pass

def test_double():
    assert double(range(3)) == [0,2,4]


# Exercise 2
# Use list comprehension to create a function that finds
# the odd elements in a sequence of numbers
# ================================
def odd(sequence):
	# return [...]
	pass

def test_odd():
	assert odd(range(6)) == [1,3,5]


# Exercise 3
# Use list comprehension to create a function that finds
# the elements divisible by 5 in a sequence of numbers
# ================================
def by_five(sequence):
	# return [...]
	pass

def test_by_five():
	assert by_five(range(1,31)) == [5,10,15,20,25,30]


# Exercise 4
# Use list comprehension to create a function that finds
# words containing the letter 'e' in a list of words
# ================================
def e_present(words):
	# return [...]
	pass

def test_e_present():
	assert e_present(['dog', 'heron', 'turtle', 'aardvark', 'python', 'elephant']) == ['heron', 'turtle', 'elephant']


# Exercise 5
# Use list comprehension to display the index position in front of each element
# of a list.
# 
# Hint 1: write a function that accepts the index position and element of each item
# in the list, and formats the element into the form 'index: element'
# Hint 2: use enumerate() in the iterator of the list comprehension
# ================================

def treat(index, element):
	# return ...
	pass

def format_pair(sequence):
	# return [...]

def test_format_pair():
	assert format_pair(["zero", "one", "two"]) == ['0: zero', '1: one', '2: two']
