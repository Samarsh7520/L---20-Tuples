def avgfun(num):
    list1=list(num)
    sum = 0
    for x in list1:
        sum=sum+x
        
    return sum

n = (23,24,46,18,39,48,74,3,35,30)
print("Tuple:",n)
print("Average: ",avgfun(n)/len(n))