

A = 125   
B = 5    

count = 0 

while A % B == 0:
    count += 1
    #A //= B  

if count > 0:
    print(f"{A} is divisible by {B} : {count} times")
else:
    print(f"{A} is not divisible by {B}")
