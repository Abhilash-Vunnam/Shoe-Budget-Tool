#!/bin/python3

from SHOES import Shoes

low = Shoes("And ls", 30)
medium = Shoes("Air Force ls", 120)
high = Shoes("off whites",400)

try:
	shoe_budget = float(input('What is your budget? ')) 
except ValueError:
	exit("Please enter a number")
	
for shoes in (high, medium, low):
	shoes.buy(shoe_budget)
