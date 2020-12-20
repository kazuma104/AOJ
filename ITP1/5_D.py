for i in range(1,int(input())+1):
    if i%3==0:
        print(" ",i,sep="",end="")
    else:
        for j in range(len(str(i))):
            if (i//10**j)%10==3:
                print(" ",i,sep="",end="")
                break
print()