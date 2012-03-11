# genetic algorithm to match an alphanumeric string
#
# FEATURES: works with all lengths of alphabetical strings, works with all numerical pool sizes, 
# mutations occur with a 1/10 chance when breeding, ability to step through program, kinda modular, 
# lightweightish, cycle and mutation counter, probably some other stuff
#
# Nate Baker 2012
import random
print "alphabetic string genetic algorithm by Nate Baker\n"
ideal=raw_input("Enter an alphabetical string to match: ") # get ideal string
pool=raw_input("Set the pool size (default=100): ") # get pool
pool=int(pool)
fitnesses=[]
totalmutations=0
count=0
mutated=False
def fit(x): # test // function that determines how fit a string is, compared to the ideal string
	global ideal
	result=0
	for i in range(len(x)):
		if x[i] == ideal[i]:
			result+=1
	return result
def populate(x,y): # length, size // function to populate a list of random strings
	str=""
	result=[]
	for i in range(y):
		for j in range(x):
			str+=random.choice('abcdefghijklmnopqrstuvwxyz')
		result.append(str)
		str=""
	return result
def breed(x): # population // function that breeds every string in a list
	global ideal,totalmutations,mutated
	t=x
	x=[]
	if mutated == False:
		r1=random.randint(1,10) # random number 1-10
		r2=random.randint(1,10) # random number 1-10
	for i in range(len(t)-1):
		str1=t[i]
		str2=t[i+1]
		half = len(ideal)/2
		if r1 == 1 and mutated == False: # MUTATION
			string1=list(str1)
			string1[random.randint(1,len(str1)/2)]=random.choice('abcdefghijklmnopqrstuvwxyz')
			str1="".join(string1)
			totalmutations+=1
			mutated=True
		if r2 == 1 and mutated == False: # MUTATION
			string2=list(str2)
			string2[random.randint(1,len(str2)/2)]=random.choice('abcdefghijklmnopqrstuvwxyz')
			str2="".join(string2)
			totalmutations+=1
			mutated=True
		str1_half1 = str1[:half]
		str2_half2 = str2[half:]
		x.append(str1_half1 + str2_half2)
	return x
def report(): # function to print population & fitness levels
	print "Population: \n",population,"\nFitnesses: \n",fitnesses,"\n-----"
	#raw_input("") # uncomment to step through program
def doSort(x,y): # fitnesses, population // sorts x and y; based on x
	global fitnesses,population
	pop=zip(fitnesses,population)
	pop=sorted(pop,reverse=True)
	fitnesses,population=zip(*pop)
def findElite(x): # list // function that finds the elite of a list (10%), dumps the rest
	t=x
	x=[]
	for i in range(len(t)/10):
		x.append(t[i])
	return x
def repopulate(x): # list // function to repopulate the list x
	global pool,ideal
	str=""
	while len(x) < pool:
		for i in range(len(ideal)):
			str+=random.choice('abcdefghijklmnopqrstuvwxyz')
		x.append(str)
		str=""
def recalcFit(x): # population // function to calculate fitness based on current population
	result=[]
	for i in range(len(x)):
		result.append(fit(population[i]))
	return result
population=populate(len(ideal),pool) # make population of 100 4 character strings
while True:
	count+=1
	fitnesses=recalcFit(population)
	#report() # uncomment to print population and fitnesses at every step
	doSort(fitnesses,population)
	#report() # uncomment to print population and fitnesses at every step
	population=findElite(population) # find the elite of population
	fitnesses=findElite(fitnesses) # find the elite of the fitnesses
	#report() # uncomment to print population and fitnesses at every step
	population=breed(population) # breed the elite
	mutated=False
	fitnesses=recalcFit(population)
	#report() # uncomment to print population and fitnesses at every step
	repopulate(population) # repopulate the population
	fitnesses=recalcFit(population)
	#report() # uncomment to print population and fitnesses at every step
	if ideal in population: # if we have ideal string in population
		fitnesses=recalcFit(population)
		doSort(fitnesses,population)
		report() # update
		print "Took",count,"cycles."
		print totalmutations,"total mutations."
		break