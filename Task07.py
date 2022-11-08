import Vector

def check_at_least_one_negative_element(vector):
    count = 0
    for element in vector:
        if element < 0:
            count += 1
    return count

def main():
    vector = Vector.input_vector_element(NUMBER_VECTOR_ELEMENTS=5)

    if check_at_least_one_negative_element(vector) >= 1:
        msg = f"Vector {vector} has at least one negative element"
    else:
        msg = f"All elements in vector {vector} are positive"

    print(msg)
main()