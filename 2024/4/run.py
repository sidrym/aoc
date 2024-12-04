#lang python
file = 'input.txt'
f = open(file).readlines()
silver, gold = 0, 0

pairs = ["XMAS", "SAMX"]

# horizontal
for line in f:
	for i in range(len(line)):
		if line[i:i+4] in pairs:
			silver += 1

# vertical
for i in range(len(f)):
	for j in range(len(f)-3):
		if f[j][i] + f[j+1][i] + f[j+2][i] + f[j+3][i] in pairs:
			silver += 1

# diagonal
for i in range(len(f)-3):
	for j in range(len(f)-3):
		if f[j][i] + f[j+1][i+1] + f[j+2][i+2] + f[j+3][i+3] in pairs:
			silver += 1

# diagonal
for i in range(3, len(f)):
	for j in range(len(f)-3):
		if f[j][i] + f[j+1][i-1] + f[j+2][i-2] + f[j+3][i-3] in pairs:
			silver += 1
# gold x
for i in range(1, len(f)-1 ):
	for j in range(1, len(f)-1):
		if (f[j][i] == 'A' and
			f[j-1][i-1] + f[j+1][i-1] + f[j-1][i+1] + f[j+1][i+1] in 
			["MMSS", "SSMM", "MSMS", "SMSM"]
			):
			gold += 1

print("silver", silver)
print("gold", gold)

