from multiprocessing.dummy import Value


sqaure = {num:num**2 for num in range(1, 11)}
print(sqaure)

sqaure = {f"Square of {num} is":num**2 for num in range(1, 11)}
print(sqaure)

sqaure = {f"Suare of {num} is":num**2 for num in range(1, 11)}
for k,v in sqaure.items():
    print(f"{k} : {v}")

# string = "Harshit"
string = "harshit"
word_count = {char:string.count(char) for char in string}
print(word_count)

# stuff price in dollar
old_price = {'milk' : 1.02, 'coffee':2.5, 'bread':2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

