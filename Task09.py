import Vector

def check_only_one_negative_element(vector):
    count = 0
    for element in vector:
        if element < 0:
            count += 1
    return count

def main():
    vector = Vector.input_vector_element(NUMBER_VECTOR_ELEMENTS=3)

    if check_only_one_negative_element(vector) == 1:
        msg = f"Vector {vector} has only one negative element"
    elif check_only_one_negative_element(vector) == 0:
        msg = f"All elements in vector {vector} are positive"
    else:
        msg = f"Vector {vector} has more than one negative element"

    print(msg)

main()