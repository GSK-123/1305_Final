def array_target(num, x):
    left, right = 0, len(num) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if num[mid] == x:
            return mid
        elif num[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


num1 = [1, 3, 5, 6]
x1 = 5
print(array_target(num1, x1))
num2 = [1, 3, 5, 6]
x2 = 2
print(array_target(num2, x2)) 
