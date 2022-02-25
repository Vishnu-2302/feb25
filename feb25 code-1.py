l=[]
p=[]
n=[]
o=[]
r=int(input('enter the range : '))
for i in range(r):
	x=int(input('enter the value : '))
	l.append(x)
for i in range(r):
	if l[i]>=0:
		p.append(l[i])
p.sort()
for i in range(r):
	if l[i]<0:
		n.append(l[i])
n.sort(reverse=True)
p.extend(n)
o.extend(p)
print(o)