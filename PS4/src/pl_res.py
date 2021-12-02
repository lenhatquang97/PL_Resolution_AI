from algorithms import *
#Step 1: Read file
fileName = "input.txt"
file = open(fileName, "r")
lines = file.readlines()
values = list(map(lambda x: x.strip(), lines))

#Step 2: Read alpha clause, N clauses for KB, KB clauses
alpha = values[0]
N = int(values[1])
kbValues = values[2:]

#Call function to run
check = "YES" if plResolution(kbValues, alpha) else "NO" 
print(check)