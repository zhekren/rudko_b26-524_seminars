def func(n: int, m: int):
    matrix = [[0 for _ in range(m)] for __ in range(n)]
    flag = 'right'
    index = 0
    numbers = [i for i in range(1, n*m + 1)]
    i = 0
    j = 0
    while (index < len(numbers)):
        if flag == 'right' and index != len(numbers):
            if (j < m - 1 and matrix[i][j + 1] == 0):
                matrix[i][j] = numbers[index]
                index += 1
                j += 1
            else:
                matrix[i][j] = numbers[index]
                index += 1
                i += 1
                flag = 'down'
        
        if flag == 'left' and index != len(numbers):
            if (j > 0 and matrix[i][j-1] == 0):
                matrix[i][j] = numbers[index]
                index += 1
                j -= 1
            else:
                matrix[i][j] = numbers[index]
                index += 1
                i -= 1
                flag = 'up'
            
        if flag == 'down' and index != len(numbers):
            if (i < n-1 and matrix[i+1][j] == 0):
                matrix[i][j] =numbers[index]
                index += 1
                i += 1
            else:
                matrix[i][j] = numbers[index]
                index += 1
                j -= 1
                flag = 'left'
        
        if flag == 'up' and index != len(numbers):
            if (i > 0 and matrix[i-1][j] == 0):
                matrix[i][j] = numbers[index]
                index += 1
                i -= 1
            else:
                matrix[i][j] = numbers[index]
                index += 1
                j += 1
                flag = 'right'
    for st in matrix:
        print(st)
    print('\n')

func(3,3)
func(3,5)
func(5,2)