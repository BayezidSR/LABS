import math 

def polar_to_cartesian(r, theta_degrees):
    theta_radians = math.radians(theta_degrees) #Converts theta from degrees to radians 

    x = r* math.cos(theta_radians)
    y = r* math.sin(theta_radians)

    return (round(x, 5), round(y, 5)) #This will round our results but 5 decimal points

r = float(input("Insert the distance from the origin:" ))
theta_degrees = float(input("Insert the angle starting from the positive x-axis, in degrees:" ))
Coordinates = polar_to_cartesian(r, theta_degrees)
print(f"your coordinates from polar to cartesian is {Coordinates}")

def cartesian_to_polar(x, y): 

    r = math.sqrt(x**2 + y**2) 
    theta_degrees = math.degrees(math.atan2(y, x)) #Converts theta from radians to degrees

    return (round(r, 5), round(theta_degrees, 5)) #This will round our results but 5 decimal points

x = float(input("Insert your x axis:" ))
y = float(input("Insert your y axis:" ))
Polar = cartesian_to_polar(x, y) 
print(f"Your polar coordinates from cartesian to polar is {Polar}")

def oscillatory(T,A, phi, t):

    w = (2*math.pi)/T 
    x = A * math.cos(w*t + phi)

    return (round(x, 5))

A = float(input("Insert the maximum displacement from the equilibrium: ")) 
T = float(input("Insert the time it took for the oscillation motion to repeat: "))
phi = float(input("Insert your phase constant in radians: ")) 
t = float(input("Insert the time to check your position: ")) 
Position = oscillatory(t, A, phi, T)

print(f"The position at {t} seconds is {Position}") 