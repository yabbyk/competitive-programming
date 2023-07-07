m,n,a = map(int , input().split())
if m%a == 0:
    resA = m//a
else:
    resA = m//a+1
if n% a == 0:
    resB = n//a
else:
    resB = n//a+1
 
print(resA*resB)
