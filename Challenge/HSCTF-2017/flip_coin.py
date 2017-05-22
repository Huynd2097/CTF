import re

flips = open('flip_coin.txt').read()

f0 = re.findall('0+', flips)
f1 = re.findall('1+', flips)

# sort 0 -> 0...0
f0.sort() 
f1.sort() 

run_max = max(len(f0[-1]), len(f1[-1]))
ret = [0]*(run_max + 1)

for run in f0:
	ret[len(run)] += 1
for run in f1:
	ret[len(run)] += 1

ret.pop(0)
print ', '.join(ret)