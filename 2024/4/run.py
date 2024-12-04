#lang python
file = 'input.txt'
f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

pairs = ["XMAS", "SAMX"]

# horizontal
for j in range(len(f)):
	for i in range(len(f[0])):
		# horizontal
		if f[j][i:i+4] in pairs:
			silver += 1

		# vertical
		if j in range(len(f)-3) and f[j][i] + f[j+1][i] + f[j+2][i] + f[j+3][i] in pairs:
			silver += 1

		# diagonal
		if i < len(f)-3 and j < len(f)-3 and f[j][i] + f[j+1][i+1] + f[j+2][i+2] + f[j+3][i+3] in pairs:
			silver += 1

		# reverse diagonal
		if i >= 3 and j < len(f)-3 and f[j][i] + f[j+1][i-1] + f[j+2][i-2] + f[j+3][i-3] in pairs:
			silver += 1

		if (0 < i < len(f)-1 and 0 < j < len(f)-1 and
			f[j][i] == 'A' and f[j-1][i-1] + f[j+1][i-1] + f[j-1][i+1] + f[j+1][i+1] in 
			["MMSS", "SSMM", "MSMS", "SMSM"]):
				gold += 1

print("silver", silver)
print("gold", gold)

