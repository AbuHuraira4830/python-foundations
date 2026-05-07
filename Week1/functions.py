# A function to print the name of user input
# Also understanding of default parameters

def main():
    hello()         #when we pass no argument function added the default param "world" when defined 
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print(f"hello, {to}") #sideeffect (func returns no value)

main()