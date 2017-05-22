import math
import random

def distance(p1, p2):
	tmp = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
	return math.sqrt(tmp)

def arceage_tri(a,b,c):
	AB = distance(a,b)
	AC = distance(a,c)
	CB = distance(c,b)
	p = (AB + AC + CB) / 2
	return math.sqrt(p*(p-AB)*(p-AC)*(p-CB))

def get_points_outof_triangle(a,b,c, points):
	arceage_triangle = arceage_tri(a,b,c)
	ret = [a,b,c]
	for p in points:
		abp = arceage_tri(a,b,p)
		acp = arceage_tri(a,c,p)
		cbp = arceage_tri(c,b,p)

		if arceage_triangle <= (abp + acp + cbp):
			ret.append(p)
	return ret 

# read + config
points = open('keith_march.txt').read().splitlines()
for i in xrange(len(points)-1, -1, -1):
	p = points[i].split(' ')
	p[0] = int(p[0])
	p[1] = int(p[1])
	# not config also sovle but slower
	# after config,  len(points) = 188
	# if math.fabs(p[0]) < 450 and math.fabs(p[1]) < 450:
	# 	# print p[0], p[1]
	# 	points.pop(i)
	# else:
	points[i] = p

# See in pts: angle ~ 25
while len(points) > 25:
	a = points.pop(random.randint(0,len(points)-1))
	b = points.pop(random.randint(0,len(points)-1))
	c = points.pop(random.randint(0,len(points)-1))
	points = get_points_outof_triangle(a,b,c,points)

# 2300 = 25C3
for i in xrange(2300):
	a = points.pop(random.randint(0,len(points)-1))
	b = points.pop(random.randint(0,len(points)-1))
	c = points.pop(random.randint(0,len(points)-1))
	points = get_points_outof_triangle(a,b,c,points)

mul = 1
for p in points:
	mul *= p[0] * p[1]
print mul % (10**9 + 7)
# print len(points)
# print points



# print ','.join(points)
