#Lab03_2a
out=""
for i in range(1,7):
    for j in range(1,i+1):
        out+=str(j)
    out+="\n"
print out
#Lab03_2b
out=""
for i in range(6,-1,-1):
    for j in range(1,i+1):
        out+=str(j)
    out+="\n"
print out
#Lab03_2c
out=""
for i in range(1,8):
    for j in range(6,0,-1):
          if(j>i-1):
              out+=" "
          else:
              out+=str(j)
    out+="\n"
out+="\n"
print out
#Lab03_2d
for i in range(7,0,-1):
    for j in range(1,7):
          out+=str(j)
              
          
    out+="\n"
out+="\n"
print out

#Lab03_2e
