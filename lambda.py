add2 = lambda a,b : a+b
print(add2(3,2))
print(add2)

string = "Sunny"
print(lambda string : string)


numbers = [1,2,3,4]
squares = list(map(lambda a:a**2, numbers))
print(squares)

# list comp
squares_new = [i**2 for i in numbers]
print(squares_new)