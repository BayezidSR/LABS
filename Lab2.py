def calculate_height(H0, t):
    #Gravity
    g = 9.8
    Height = H0 - 0.5 * g * (t**2) # time in seconds
    return Height

print("Insert your initial height when the object was thrown at max height, in meters")
H0 = float(input())

Height1 = calculate_height(H0, 1)
print(f"The height of the object at 1 second is {Height1}")

Height2 = calculate_height(H0, 2)
print(f"The height of the object at 2 seconds is {Height2}")

Height3 = calculate_height(H0, 3)
print(f"The height of the object at 3 seconds is {Height3}") 

def calculate_car_distance(t): 
    Distance = V0 * t #Distance = Velocity * Time 
    return Distance 

print("Insert the velocity of which the car was going at")
V0 = float(input())

Velocity1 = calculate_car_distance(1)
print(f"The distance the car travelled at 1 second is {Velocity1}")

Velocity2 = calculate_car_distance(2)
print(f"The distance the car travelled at 2 seconds is {Velocity2}")

Velocity3 = calculate_car_distance(3)
print(f"The distance the car travelled at 3 seconds is {Velocity3}")