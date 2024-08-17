def duplicate_array(x):
    count = {}
    for i in x:
        if i in count:
            count[i] += 1 
        else:
            count[i] = 1
    dup_arr = [i for i, j in count.items() if j > 1]

    if dup_arr:
        return min(dup_arr)
    else:
        return None
    
arr1 = [4, 10, 5, 1, 11, 5, 1, 4, 1]
arr2 = [1,10,1,-1,10,-1]

print(duplicate_array(arr1))
print(duplicate_array(arr2))
    