def reverse_integer(x):
    if x < 0:
        y = int(str(-x)[::-1]) * -1
    else:
        y = int(str(x)[::-1])
    return y

print(reverse_integer(123))   
print(reverse_integer(-456)) 
