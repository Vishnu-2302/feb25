l=[]
t=[]
c=0
n=int(input('enter the range : '))
for i in range(n):
	x=int(input('enter the value : '))
	l.append(x)
l.sort()
for i in range(n):
	if l[i]>0:
		t.append(l[i])
		c=c+1
print(t)
print(f'total count of numbers : {c}')