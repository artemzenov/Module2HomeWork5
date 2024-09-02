def get_matrix(n=0, m=0, value=0):
    matrix = list()
    
    for i in range(0, n):
        elem_matrix = list()
        
        for j in range(0, m):
            elem_matrix.append(value)
        
        matrix.append(elem_matrix)
    
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)

# def get_matrix(*args):
#   matrix = list()

#   for i in range(0, args[0]):
#       elem_matrix = list()

#       for j in range(0, args[1]):
#           elem_matrix.append(args[2])

#       matrix.append(elem_matrix)

#   return matrix


# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)

# print(result1)
# print(result2)
# print(result3)

# def get_matrix(**kwargs):
#   matrix = list()

#   for i in range(0, kwargs['n']):
#       elem_matrix = list()

#       for j in range(0, kwargs['m']):
#           elem_matrix.append(kwargs['value'])

#       matrix.append(elem_matrix)

#   return matrix


# result1 = get_matrix(n=2, m=2, value=10)
# result2 = get_matrix(n=3, m=5, value=42)
# result3 = get_matrix(n=4, m=2, value=13)

# print(result1)
# print(result2)
# print(result3)
