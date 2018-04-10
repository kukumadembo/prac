 # This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

num1 = eval(input("First number: "))
num2 = eval(input("Sec number: "))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = eval(input("Enter choice(1/2/3/4):"))

if choice == 1:
   print(add(num1, num2))
   
elif choice == 2:
   print(subtract(num1, num2))

elif choice == 3:
   print(multiply(num1, num2))

elif choice == 4:
   print(divide(num1, num2))
else:
   print("Wrong seclection")
   
   
   
