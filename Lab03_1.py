i=5;out="2,3,5,"
while True:
    i+=1
    if((i%2)!=0 and (i%3)!=0 and (i%5)!=0):
        #number=
        out+= str(i)+","
    else:
        continue
    if(i==500):
        break
print out
