print("Hello, world!")

def input_output():  
    print("Good morning, please enter your username.") 
    Username = str(input())
    # We will ask them for their username and allow them to insert their username 

    print("Good morning " + Username + ", please enter your age.")
    Age = int(input())
    # This allows the user to input their age 

    print("Hello " + Username + " you are currently " + str(Age) + ". Now please insert your height.")
    Height = float(input())
    # This will ask the user to insert their height 

    print(f"Hello {Username} you are {Age} years old and you are {Height} feet tall")
    # This will output the information the user inputted 

input_output()