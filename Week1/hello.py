#Ask user for their name
name = input("What's your name? ").strip().title()

#strip() is used to remove extra spaces from left and right
#title() is used to convert string into a book title case (every word 1st char capital)

# print ("hello", name) # multiple args way to print

print (f"hello, {name}") #new way or f-string way to print


# if we  have to just print first or last name

# will use split method for that tos split a string

first, last = name.split(" ") #split by space

print (f"hello, {first}")