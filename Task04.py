import Vector


def check_all_elements_even(vector):
    for element in vector:
        if element % 2 == 1:
            return False
    return True


def check_all_elements_odd(vector):
    for element in vector:
        if element % 2 == 0:
            return False
    return True


def main():
    vector = Vector.random_vector_elements()

    if check_all_elements_odd(vector):
        msg = f"All elements in {vector} are odd"
    elif check_all_elements_even(vector):
        msg = f"All elements in {vector} are even"
    else:
        msg = f"Vector {vector} has even and odd elements"

    print(msg)


main()
