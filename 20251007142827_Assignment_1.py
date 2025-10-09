def maximum(x, y, z): 
    numbers = [x, y, z]
    highest = max(numbers)
    return highest 

x = int(input("Input your first number"))    
y = int(input("Input your second number")) 
z = int(input("Input your third number")) 

print(f"Your highest input is {maximum(x, y, z)}")

#------------------------------------------------------------

def minimum(Num1, Num2, Num3): 
    numbers = [Num1, Num2, Num3]
    lowest = min(numbers)
    return lowest 

a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))

print(f"Your lowest number is {minimum(a, b, c)}")

#------------------------------------------------------------

def check_number(Num): 
    if Num > 0: 
        result = ("The number inputted is positive")

    elif Num < 0: 
        result = ("The number inputted is negative")

    else:
        result = ("The number inputted is zero") 

    return result

Number = float(input("What number do you want to check"))

print(f"{check_number(Number)}")

#------------------------------------------------------------

def star_shape(rows): 
    for i in range(1, rows + 1):
        print("*"*i)
    return

row = int(input("How many rows of stars do you want to print (Whole numbers please)"))

print(f"{star_shape(row)}")

#------------------------------------------------------------

def counting(n): 
    i = 0 
    while i < n: 
        i += 1 
        if i % 3 == 0: 
            print(f"{i} is a multiple of three")

        else: 
            print(i)

    return 

count = int(input("What number do you want me to count"))
counting(count)

#------------------------------------------------------------

def adding(x, y): 
    list = []
    even_numbers = []
    for i in range(x, y+1): 
        list.append(i)

    for n in list: 
        if n % 2 == 0: 
            even_numbers.append(n)

    total = sum(even_numbers)
    return total 

j = int(input("Insert your first number"))
k = int(input("Insert your second number"))
print(adding(j, k))
