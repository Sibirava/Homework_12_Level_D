import Vector

def check_only_one_positive_element(vector):
    count = 0
    for element in vector:
        if element > 0:
            count += 1
    return count

def main():
    vector = Vector.input_vector_element(NUMBER_VECTOR_ELEMENTS=3)

    if check_only_one_positive_element(vector) == 1:
        msg = f"Vector {vector} has only one positive element"
    elif check_only_one_positive_element(vector) == 0:
        msg = f"All elements in vector {vector} are negative"
    else:
        msg = f"Vector {vector} has more than one positive element"

    print(msg)

main()