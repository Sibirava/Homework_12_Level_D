import Vector

def check_elements_vector_equal(vector):

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] == vector[j]:
                return False
    return True

def count_pairs_of_equal_elements(vector):
    count = 0

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] == vector[j]:
                count += 1
    return count

def main():

    vector = Vector.random_vector_elements()

    if check_elements_vector_equal(vector):
        msg = f"The elements in {vector} are not equal"
    else:
        msg = f"There are equal elements in {vector}. There are " \
              f"{count_pairs_of_equal_elements(vector)} equal pair(s) in vector"

    print(msg)

main()