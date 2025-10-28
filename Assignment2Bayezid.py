def test_remove_duplicates_and_sort(numbers): 
    number_list = list(int(x) for x in numbers.split())
    remove_duplicate = list(set(number_list))
    sorted_list = sorted(remove_duplicate)

    print(f"Your number list before organization: {number_list}")
    print(f"Your number list after organization: {sorted_list}")

    return

numbers = (input("Give me a list of whole numbers to remove duplicates and sort them by order: "))
print(test_remove_duplicates_and_sort(numbers))

#---------------------------------------------------------------------------------------------------------- 

def test_cumulative_sum(number):
    number_list = list(int(x) for x in number.split())
    new_list = []
    new_total = 0
    for i in number_list:
        new_total += i
        new_list.append(new_total)

    return new_list 

number = (input("Give me a list of whole numbers for test cumulative sum: "))
print(test_cumulative_sum(number))

#---------------------------------------------------------------------------------------------------------- 

def slice_every_second(number): 
    number_list = list(int(x) for x in number.split())
    second_number = number_list[::2] 
    return second_number 

number = (input("Give a list of number to take every 2nd number from"))
print(slice_every_second(number))

#---------------------------------------------------------------------------------------------------------- 

def test_dot_product(L1, L2): 
    first_list = list(int(x) for x in L1.split())
    second_list = list(int(x) for x in L2.split())
    dot_list = [first_list, second_list]
    print(f"Your two list of numbers to dot product is {dot_list}")

    dot_product = 0
    for i in range(len(first_list)):
        dot_product += dot_list[0][i]*dot_list[1][i]

    return dot_product

first = (input("Insert your first list of numbers for dot product, space each whole number: "))
second = (input("Insert your second list of numbers for dot product, space each whole number: "))
print(test_dot_product(first, second))

#---------------------------------------------------------------------------------------------------------- 

def matrix_multiplication(list1, list2):
    first_list = list(int(x) for x in list1.split())
    second_list = list(int(x) for x in list2.split())
    first_matrix = [first_list[:2], first_list[2:]]
    second_matrix = [second_list[:2], second_list[2:]]

    multiplied_matrix_1 = []
    A = first_matrix[0][0]*second_matrix[0][0] + first_matrix[0][1]*second_matrix[1][0]
    B = first_matrix[0][0]*second_matrix[0][1] + first_matrix[0][1]*second_matrix[1][1]
    multiplied_matrix_1.append(A)
    multiplied_matrix_1.append(B)

    multiplied_matrix_2 = []
    C = first_matrix[1][0]*second_matrix[0][0] + first_matrix[1][1]*second_matrix[1][0]
    D = first_matrix[1][0]*second_matrix[0][1] + first_matrix[1][1]*second_matrix[1][1]
    multiplied_matrix_2.append(C)
    multiplied_matrix_2.append(D)

    multiplied_matrix = [multiplied_matrix_1, multiplied_matrix_2]

    return multiplied_matrix

first = (input("Insert your first list of numbers for dot product, space each whole number: "))
second = (input("Insert your second list of numbers for dot product, space each whole number: "))
print(matrix_multiplication(first, second))