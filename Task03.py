import Vector

def check_all_elements_positive(vector):

    for element in vector:
        if element < 0:
            return False
    return True


def check_all_elements_negative(vector):
    for element in vector:
        if element > 0:
            return False
    return True

def main():
    vector = Vector.random_vector_elements()

    if check_all_elements_positive(vector):
        msg = f"All elements in {vector} are positive"
    elif check_all_elements_negative(vector):
        msg = f"All elements in {vector} are negative"
    else:
        msg = f"Vector {vector} has positive and negative elements"

    print(msg)

main()