
# 1. Simple program to add 2 integers
#------------------------------------------
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# 2.Round decimal values to nearest integer with round()
#------------------------------------------

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print (f"{z:,}") #print integers separated by ,

# print(z)


# 3.Round decimal values to 2 digts or 2 decimal places
#round (number, digits)
#------------------------------------------
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # z = round(x + y,2)
# # z = round( x /y, 2) 

# z = x /y
# print(f"{z:.2F}")


#4. square of a number
def main():
    x = int(input("What's x "))
    print ("Squared of x is", square(x))

def square(n):
    return n**2

main()