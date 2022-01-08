import random
jed=0
dwa=0
trz=0
czt=0
pie=0
sze=0
sie=0
osi=0
dzi=0
x=int(input("Podaj liczbę: "))
count=0
list=[]
while x !=1:
    if x % 2 == 0:
        x=x/2
    else:
        x=3*x+1
    print(int(x))
    count=count+1
    for i in str(x):
        if i == "." or i == "0":
            True
        else:    
            list.append(i)
print("Przeskoków: ",count)
for o in list:
    o=int(o)
    if o == 1:
        jed=jed+1
    if o == 2:
        dwa=dwa+1    
    if o == 3:
        trz=trz+1
    if o == 4:
        czt=czt+1   
    if o == 5:
        pie=pie+1
    if o == 6:
        sze=sze+1    
    if o == 7:
        sie=sie+1
    if o == 8:
        osi=osi+1
    if o == 9:
        dzi=dzi+1
print("1: ",jed)
print("2: ",dwa)
print("3: ",trz)
print("4: ",czt)
print("5: ",pie)
print("6: ",sze)
print("7: ",sie)
print("8: ",osi)
print("9: ",dzi)      