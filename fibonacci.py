# fibonacci number
def fibo(s):
    if s<0: print("Hey! It's invalid")
    elif s==0 :  return 0
    elif s==1 or s==2 :  return 1 
    else : return fibo(n-1) + fibo(n-2)
print(fibo(9))
