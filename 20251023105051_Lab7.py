def rotating_array(size, start):
    array = []
    for number in range(size):
        number = start
        array.append(number)
        start = start - 3
    print(f"your original array list: {array}")
   
    even_index = array[::2]
    print(f"even index list: {even_index}")

    even_index = even_index[1:] + even_index[:1]
    print(f"even index list after rotation: {even_index}")

    array[::2] = even_index

    return array

Size = int(input("What size do you want your array list to be?: "))
Start = int(input("Where do you want to start from"))
print(f"Your array list after rotation: {rotating_array(Size, Start)}")