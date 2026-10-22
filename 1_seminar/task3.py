def func(n:list):
    result = []
    num = None
    counter = 1
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            counter += 1
            num = n[i]
        else:
            result.append((num, counter))
            counter = 1
            num = n[i + 1]
    result.append((num, counter))
    return result

def func_return(n:list):
    returned = []
    for i in range(len(n)):
        for j in range(n[i][1]):
            returned.append(n[i][0])
    return returned
a = func([1,1,1,2,2,3,3,3,3,4])
b = func_return(a)

print(a)
print(b)