import Vector


def count_even_elements(vector):
    count = 0
    for element in vector:
        if element % 2 == 0:
            count += 1
    return count


def count_odd_elements(vector):
    count = 0
    for element in vector:
        if element % 2 == 1:
            count += 1
    return count


def main():
    vector = Vector.random_vector_elements()
    count_even = count_even_elements(vector)
    count_odd = count_odd_elements(vector)

    if count_even > count_odd:
        msg = f"Elements in {vector} are mostly even"
    elif count_even < count_odd:
        msg = f"Elements in {vector} are mostly odd"
    else:
        msg = f"Vector {vector} has equal amount of even and odd elements"

    print(msg)

main()