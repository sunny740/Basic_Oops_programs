# without lc
import numbers


squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)


# with lc
squares = [i**2 for i in range(1, 11)]
print(squares)


# without
negative = []
for i in range(1, 11):
    negative.append(-i)
print(negative)


# with
negative = [-i for i in range(1, 11)]
print(negative)


# without
names = ["Sunny", "Soryann", "Mohit"]
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)


# with
new_list2 = [name[0] for name in names]
print(new_list2)


# without
fruits = ["Apple", "Mango", "Banana", "Cherry", "kiwi"]
new_list = []
for i in fruits:
    new_list.append(i)
print(new_list)


# with lc
fruits = ["Apple", "Mango", "Banana", "Cherry", "kiwi"]
# new_list = [i for i in fruits if "a" in i]
new_list = [i for i in fruits]
print(new_list)

# with lc
def reverse_string(l):
    return[name[::-1] for name in l]
print(reverse_string(['abc', 'tuv', 'xyz']))

# without lc
def reverse_string(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_string(['abc', 'tuv', 'xyz']))        

