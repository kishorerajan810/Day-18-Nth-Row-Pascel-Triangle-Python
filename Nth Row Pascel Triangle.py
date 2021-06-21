def NthRowPascelTriangle(n): 
    a= 1
    print(a,end =" ") 
    for i in range(1,n): 
        b=(a*(n-i))//i 
        print(b,end=" ") 
        a=b
   
n=int(input("enter :"))
NthRowPascelTriangle(n)  
