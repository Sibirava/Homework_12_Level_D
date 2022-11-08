import Vector

def check_mutually_opposite_elements(vector):
    ls = []
    count = 0

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] == - vector[j]:
                count += 2
                ls.append(vector[i])
                ls.append(vector[j])
    return (ls, count)

def main():
    vector = Vector.random_vector_elements()
    ls, count = check_mutually_opposite_elements(vector)

    msg = f"They are {count} mutually opposite elements in {vector}. They are: {ls}"

    print(msg)

main()