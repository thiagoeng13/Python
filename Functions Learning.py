#while
x=0
while (x<5):
    print(x)
    x=x+1

#For
for x in range(5,10):
    print(x)

days=["mon","tue","wed","thu","fri","sat","sun"]

for d in days:
    if(d=="thu"):break
    print(d)

days=["mon","tue","wed","thu","fri","sat","sun"]

for d in days:
    if(d=="thu"):continue
    print(d)