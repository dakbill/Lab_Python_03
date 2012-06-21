div_count=0;prime_count=0
inp=int(raw_input("Enter number:"))
for i in range(1,inp+1):
    if(inp%i==0):
        div_count+=1
    if(div_count==2):
        prime_num=inp
        prime_count+=1
        print "prime"
        

