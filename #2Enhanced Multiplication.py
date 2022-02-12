def mu(a,b):
    for i in range(1,b+1):
        r=a*i
        print ("{0}x{1}={2}".format(a,i,r))
if __name__=="__main__":
    a=input("inter number:")
    b=int(input("genertor:"))
    a=float(a)
    mu(a,b)
                
                
