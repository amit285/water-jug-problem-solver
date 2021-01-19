x=int(input("Enter the capacity of x")) #4
y=int(input("Enter the capacity of y")) #3
xg=int(input("Enter the goal amount in x")) #2
yg=int(input("Enter the goal amount in y")) #0

state_space={}
xc=0
yc=0
ol=[(0,0)]
cl=[]
'''Rules for the problem'''
while((xg,yg) not in cl or len(ol)!=0):
    xc,yc=ol.pop(0)
    if (xc,yc) not in cl:
        l=[]
        state_space[(xc,yc)]=l
        if(xc<x):
            l.append((x,yc))
            ol.append((x,yc))
        if(yc<y):
            l.append((xc,y))
            ol.append((xc,y))
        if(xc>0):
            l.append((0,yc))
            ol.append((0,yc))
        if(yc>0):
            l.append((xc,0))
            ol.append((xc,0))
        if(xc>0 and yc<y):
            if(xc+yc>y):
                l.append((xc+yc-y,y))
                ol.append((xc+yc-y,y))
            else:
                l.append((0,xc+yc))
                ol.append((0,xc+yc))
        if(xc<x and yc>0):
            if(xc+yc>x):
                l.append((x,xc+yc-x))
                ol.append((x,xc+yc-x))
            else:
                l.append((xc+yc,0))
                ol.append((xc+yc,0))
        cl.append((xc,yc))
for i,j in state_space.items():
    print("node is ",i, "Childs are ",j)
print(ol,cl)