import Vector


def check_mostly_positive_element(vector):
    count = 0
    for element in vector:
        if element > 0:
            count += 1
    return count

def check_mostly_negative_element(vector):
    count = 0
    for element in vector:
        if element < 0:
            count += 1
    return count

def main():
    vector = Vector.random_vector_elements()
    count_positive = check_mostly_positive_element(vector)
    count_negative = check_mostly_negative_element(vector)

    if count_positive > count_negative:
        msg = f"Elements in {vector} are mostly positive"
    elif count_positive < count_negative:
        msg = f"Elements in {vector} are mostly negative"
    else:
        msg = f"Vector {vector} has equal count of positive and negative elements"

    print(msg)


main()
