def fibo(s):
    if s<0: print("Hey! It's invalid")
    elif s==0 :  return 0
    elif s==1 or s==2 :  return 1 
    else : return fibo(s-1) + fibo(s-2)
print(fibo(9))
