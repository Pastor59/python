nums = [1,2,3,4,5,6]

def square(n):
    return n * n

#lambda n: n*n

print(list(map(square,nums)))

print(list(map(lambda n: n*n,nums)))
#print(list(map(function,nums)))